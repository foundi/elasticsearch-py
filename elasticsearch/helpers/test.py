# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

# type: ignore

import time
import os
from unittest import TestCase, SkipTest

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError


def get_test_client(nowait=False, **kwargs):
    # construct kwargs from the environment
    kw = {"timeout": 30, "ca_certs": ".ci/certs/ca.pem"}
    if "PYTHON_CONNECTION_CLASS" in os.environ:
        from elasticsearch import connection

        kw["connection_class"] = getattr(
            connection, os.environ["PYTHON_CONNECTION_CLASS"]
        )

    kw.update(kwargs)
    client = Elasticsearch([os.environ.get("ELASTICSEARCH_HOST", {})], **kw)

    # wait for yellow status
    for _ in range(1 if nowait else 100):
        try:
            client.cluster.health(wait_for_status="yellow")
            return client
        except ConnectionError:
            time.sleep(0.1)
    else:
        # timeout
        raise SkipTest("Elasticsearch failed to start.")


def _get_version(version_string):
    if "." not in version_string:
        return ()
    version = version_string.strip().split(".")
    return tuple(int(v) if v.isdigit() else 999 for v in version)


class ElasticsearchTestCase(TestCase):
    @staticmethod
    def _get_client():
        return get_test_client()

    @classmethod
    def setup_class(cls):
        cls.client = cls._get_client()

    def teardown_method(self, _):
        # Hidden indices expanded in wildcards in ES 7.7
        expand_wildcards = ["open", "closed"]
        if self.es_version() >= (7, 7):
            expand_wildcards.append("hidden")

        self.client.indices.delete(
            index="*", ignore=404, expand_wildcards=expand_wildcards
        )
        self.client.indices.delete_template(name="*", ignore=404)
        self.client.indices.delete_index_template(name="*", ignore=404)

    def es_version(self):
        if not hasattr(self, "_es_version"):
            version_string = self.client.info()["version"]["number"]
            self._es_version = _get_version(version_string)
        return self._es_version
