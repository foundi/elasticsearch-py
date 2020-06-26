# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Generator, Dict, Any
from elasticsearch import (
    Elasticsearch,
    Transport,
    RequestsHttpConnection,
    ConnectionPool,
)
from elasticsearch.helpers import scan, streaming_bulk, reindex, bulk


es = Elasticsearch([{"host": "localhost", "port": 9443}], transport_class=Transport,)
t = Transport(
    [{}],
    connection_class=RequestsHttpConnection,
    connection_pool_class=ConnectionPool,
    sniff_on_start=True,
    sniffer_timeout=0.1,
    sniff_timeout=1,
    sniff_on_connection_fail=False,
    max_retries=1,
    retry_on_status={100, 400, 503},
    retry_on_timeout=True,
    send_get_body_as="source",
)


def sync_gen() -> Generator[Dict[Any, Any], None, None]:
    yield {}


def scan_types() -> None:
    for _ in scan(
        es,
        query={"query": {"match_all": {}}},
        request_timeout=10,
        clear_scroll=True,
        scroll_kwargs={"request_timeout": 10},
    ):
        pass
    for _ in scan(
        es,
        raise_on_error=False,
        preserve_order=False,
        scroll="10m",
        size=10,
        request_timeout=10.0,
    ):
        pass


def streaming_bulk_types() -> None:
    for _ in streaming_bulk(es, sync_gen()):
        pass
    for _ in streaming_bulk(es, sync_gen().__iter__()):
        pass
    for _ in streaming_bulk(es, [{}]):
        pass
    for _ in streaming_bulk(es, ({},)):
        pass


def bulk_types() -> None:
    _, _ = bulk(es, sync_gen())
    _, _ = bulk(es, sync_gen().__iter__())
    _, _ = bulk(es, [{}])
    _, _ = bulk(es, ({},))


def reindex_types() -> None:
    _, _ = reindex(
        es, "src-index", "target-index", query={"query": {"match": {"key": "val"}}}
    )
    _, _ = reindex(
        es, source_index="src-index", target_index="target-index", target_client=es
    )
    _, _ = reindex(
        es,
        "src-index",
        "target-index",
        chunk_size=1,
        scroll="10m",
        scan_kwargs={"request_timeout": 10},
        bulk_kwargs={"request_timeout": 10},
    )
