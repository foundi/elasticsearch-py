# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import (
    Generator,
    Optional,
    Union,
    Any,
    Mapping,
    Tuple,
    Iterable,
    AsyncIterable,
    List,
    Collection,
    Callable,
)
import logging
from ..client import Elasticsearch
from ..serializer import Serializer

logger: logging.Logger

def expand_action(data: Any) -> Tuple[str, Any]: ...
def _chunk_actions(
    actions: Any, chunk_size: int, max_chunk_bytes: int, serializer: Serializer
) -> Generator[Any, None, None]: ...
def _process_bulk_chunk(
    client: Elasticsearch,
    bulk_actions: Any,
    bulk_data: Any,
    raise_on_exception: bool = ...,
    raise_on_error: bool = ...,
    *args: Any,
    **kwargs: Any
) -> Generator[Tuple[bool, Any], None, None]: ...
def streaming_bulk(
    client: Elasticsearch,
    actions: Union[Iterable[Any], AsyncIterable[Any]],
    chunk_size: int = ...,
    max_chunk_bytes: int = ...,
    raise_on_error: bool = ...,
    expand_action_callback: Callable[[Any], Tuple[str, Any]] = ...,
    raise_on_exception: bool = ...,
    max_retries: int = ...,
    initial_backoff: Union[float, int] = ...,
    max_backoff: Union[float, int] = ...,
    yield_ok: bool = ...,
    *args: Any,
    **kwargs: Any
) -> Generator[Tuple[bool, Any], None, None]: ...
def bulk(
    client: Elasticsearch,
    actions: Iterable[Any],
    stats_only: bool = ...,
    *args: Any,
    **kwargs: Any
) -> Tuple[int, Union[int, List[Any]]]: ...
def parallel_bulk(
    client: Elasticsearch,
    actions: Iterable[Any],
    thread_count: int = ...,
    chunk_size: int = ...,
    max_chunk_bytes: int = ...,
    queue_size: int = ...,
    expand_action_callback: Callable[[Any], Tuple[str, Any]] = ...,
    *args: Any,
    **kwargs: Any
) -> Generator[Tuple[bool, Any], None, None]: ...
def scan(
    client: Elasticsearch,
    query: Optional[Any] = ...,
    scroll: str = ...,
    raise_on_error: bool = ...,
    preserve_order: bool = ...,
    size: int = ...,
    request_timeout: Optional[Union[float, int]] = ...,
    clear_scroll: bool = ...,
    scroll_kwargs: Optional[Mapping[str, Any]] = ...,
    **kwargs: Any
) -> Generator[Any, None, None]: ...
def reindex(
    client: Elasticsearch,
    source_index: Union[str, Collection[str]],
    target_index: str,
    query: Any = ...,
    target_client: Optional[Elasticsearch] = ...,
    chunk_size: int = ...,
    scroll: str = ...,
    scan_kwargs: Optional[Mapping[str, Any]] = ...,
    bulk_kwargs: Optional[Mapping[str, Any]] = ...,
) -> Tuple[int, Union[int, List[Any]]]: ...
