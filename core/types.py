from typing import Any, Callable, Iterable, Protocol, runtime_checkable

Environ = dict[str, Any]

StartResponse = Callable[[str, list[tuple[str, str]]], None]
WSGIApp = Callable[[Environ, StartResponse], Iterable[bytes]]

Handler = Callable[..., Any]

@runtime_checkable
class HandlerProtocol(Protocol):
    def __call__(self, request: Any, **kwargs: Any) -> Any: ...

@runtime_checkable
class MiddlewareProtocol(Protocol):
    def process(self, request: Any, next_handler: HandlerProtocol) -> Any: ...
