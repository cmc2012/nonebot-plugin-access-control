from abc import ABC, abstractmethod
from typing import Optional, Collection, Generic, Generator, Type, TypeVar

from nonebot import Bot
from nonebot.internal.adapter import Event
from nonebot.internal.matcher import Matcher
from typing_extensions import overload, Literal

T_Service = TypeVar('T_Service', bound="IServiceBase", covariant=True)
T_ParentService = TypeVar('T_ParentService', bound=Optional["IServiceBase"], covariant=True)
T_ChildService = TypeVar('T_ChildService', bound="IServiceBase", covariant=True)


class IServiceBase(Generic[T_Service, T_ParentService, T_ChildService], ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError()

    @property
    def qualified_name(self) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def parent(self) -> Optional[T_ParentService]:
        raise NotImplementedError()

    @property
    def children(self) -> Collection[T_ChildService]:
        raise NotImplementedError()

    @abstractmethod
    def travel(self) -> Generator[T_Service, None, None]:
        raise NotImplementedError()

    @abstractmethod
    def find(self, name: str) -> Optional[T_Service]:
        raise NotImplementedError()

    @abstractmethod
    def patch_matcher(self, matcher: Type[Matcher]) -> Type[Matcher]:
        raise NotImplementedError()

    @overload
    async def check(self, bot: Bot, event: Event, with_default: Literal[True] = True) -> bool:
        ...

    @overload
    async def check(self, bot: Bot, event: Event, with_default: Literal[False]) -> Optional[bool]:
        ...

    @abstractmethod
    async def check(self, bot: Bot, event: Event, with_default: bool = True) -> Optional[bool]:
        raise NotImplementedError()