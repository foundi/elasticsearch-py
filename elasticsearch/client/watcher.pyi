# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional, Union, Collection
from .utils import NamespacedClient

class WatcherClient(NamespacedClient):
    def ack_watch(
        self,
        watch_id: Any,
        action_id: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def activate_watch(
        self,
        watch_id: Any,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def deactivate_watch(
        self,
        watch_id: Any,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def delete_watch(
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
    def execute_watch(
        self,
        body: Optional[Any] = ...,
        id: Optional[Any] = ...,
        debug: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def get_watch(
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
    def put_watch(
        self,
        id: Any,
        body: Optional[Any] = ...,
        active: Optional[Any] = ...,
        if_primary_term: Optional[Any] = ...,
        if_seq_no: Optional[Any] = ...,
        version: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def start(
        self,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def stats(
        self,
        metric: Optional[Any] = ...,
        emit_stacktraces: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def stop(
        self,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
