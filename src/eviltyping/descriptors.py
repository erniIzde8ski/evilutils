"""
Descriptor protocol, as a set of Protocols. See:

https://docs.python.org/3/howto/descriptor.html#descriptor-protocol
"""

__all__ = ["Destructor", "Getter", "Setter"]


from typing import Protocol
from typing import overload


class Getter[RT_g, Owner](Protocol):
    @overload
    def __get__(self, instance: Owner, /) -> RT_g: ...

    @overload
    def __get__(self, instance: Owner | None, owner: type[Owner], /) -> RT_g: ...

    def __get__(
        self, instance: Owner | None, owner: type[Owner] | None = None, /
    ) -> RT_g:
        """
        Implementation of a non-data descriptor. See:

        https://docs.python.org/3/reference/datamodel.html#object.__get
        """
        ...


class Setter[IT, RT_d, Owner](Protocol):
    def __set__(self, instance: Owner, value: IT, /) -> RT_d: ...


class Destructor[RT_d, Owner](Protocol):
    def __delete__(self, instance: Owner, /) -> RT_d: ...
