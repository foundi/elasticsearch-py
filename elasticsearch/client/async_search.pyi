# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional, Union, Collection
from .utils import NamespacedClient

class AsyncSearchClient(NamespacedClient):
    def delete(
        self,
        id: Any,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def get(
        self,
        id: Any,
        keep_alive: Optional[Any] = ...,
        typed_keys: Optional[Any] = ...,
        wait_for_completion_timeout: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def submit(
        self,
        body: Optional[Any] = ...,
        index: Optional[Any] = ...,
        _source: Optional[Any] = ...,
        _source_excludes: Optional[Any] = ...,
        _source_includes: Optional[Any] = ...,
        allow_no_indices: Optional[Any] = ...,
        allow_partial_search_results: Optional[Any] = ...,
        analyze_wildcard: Optional[Any] = ...,
        analyzer: Optional[Any] = ...,
        batched_reduce_size: Optional[Any] = ...,
        default_operator: Optional[Any] = ...,
        df: Optional[Any] = ...,
        docvalue_fields: Optional[Any] = ...,
        expand_wildcards: Optional[Any] = ...,
        explain: Optional[Any] = ...,
        from_: Optional[Any] = ...,
        ignore_throttled: Optional[Any] = ...,
        ignore_unavailable: Optional[Any] = ...,
        keep_alive: Optional[Any] = ...,
        keep_on_completion: Optional[Any] = ...,
        lenient: Optional[Any] = ...,
        max_concurrent_shard_requests: Optional[Any] = ...,
        preference: Optional[Any] = ...,
        q: Optional[Any] = ...,
        request_cache: Optional[Any] = ...,
        routing: Optional[Any] = ...,
        search_type: Optional[Any] = ...,
        seq_no_primary_term: Optional[Any] = ...,
        size: Optional[Any] = ...,
        sort: Optional[Any] = ...,
        stats: Optional[Any] = ...,
        stored_fields: Optional[Any] = ...,
        suggest_field: Optional[Any] = ...,
        suggest_mode: Optional[Any] = ...,
        suggest_size: Optional[Any] = ...,
        suggest_text: Optional[Any] = ...,
        terminate_after: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        track_scores: Optional[Any] = ...,
        track_total_hits: Optional[Any] = ...,
        typed_keys: Optional[Any] = ...,
        version: Optional[Any] = ...,
        wait_for_completion_timeout: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
