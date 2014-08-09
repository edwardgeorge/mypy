from typing import Any, Iterable, typevar, Set, Dict, List, TextIO, Union, Tuple, Generic, Function
from asyncio.events import AbstractEventLoop
from asyncio.futures import Future
# __all__ = ['iscoroutinefunction', 'iscoroutine',
#            'as_completed', 'async',
#            'gather', 'shield',
#            ]

__all__ = ['coroutine', 'Task', 'sleep',
            'FIRST_COMPLETED', 'FIRST_EXCEPTION', 'ALL_COMPLETED',
            'wait', 'wait_for']

FIRST_EXCEPTION = 'FIRST_EXCEPTION'
FIRST_COMPLETED = 'FIRST_COMPLETED'
ALL_COMPLETED = 'ALL_COMPLETED'
T = typevar('T')
def coroutine(f: Any) -> Any: pass  # Here comes and go a function
def sleep(delay: float, result: T=None, loop: AbstractEventLoop=None) -> Future[T]: pass
def wait(fs: List[Any], *, loop: AbstractEventLoop=None,
    timeout: float=None, return_when: str=ALL_COMPLETED) -> Future[Tuple[Set[Future[T]], Set[Future[T]]]]: pass
def wait_for(fut: Future[T], timeout: float, *, loop: AbstractEventLoop=None) -> Future[T]: pass
# def wait(fs: Union[List[Iterable], List[Future[T]]], *, loop: AbstractEventLoop=None,
#     timeout: int=None, return_when: str=ALL_COMPLETED) -> Future[Tuple[Set[Future[T]], Set[Future[T]]]]: pass

class Task(Future[T], Generic[T]):
    _all_tasks = None  # type: Set[Task]
    _current_tasks = {}  # type: Dict[AbstractEventLoop, Task]
    @classmethod
    def current_task(cls, loop: AbstractEventLoop=None) -> Task: pass
    @classmethod
    def all_tasks(cls, loop: AbstractEventLoop=None) -> Set[Task]: pass
    # def __init__(self, coro: Union[Iterable[T], Future[T]], *, loop: AbstractEventLoop=None) -> None: pass
    def __init__(self, coro: Future[T], *, loop: AbstractEventLoop=None) -> None: pass
    def __repr__(self) -> str: pass
    def get_stack(self, *, limit: int=None) -> List[Any]: pass  # return List[stackframe]
    def print_stack(self, *, limit: int=None, file: TextIO=None) -> None: pass
    def cancel(self) -> bool: pass
    def _step(self, value: Any=None, exc: Exception=None) -> None: pass
    def _wakeup(self, future: Future[Any]) -> None: pass

