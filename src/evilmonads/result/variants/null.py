from dataclasses import dataclass
from typing import Never
from typing import final
from typing import override

from evilmonads.result.error import UnwrapError

from ..result import Result


@final
@dataclass(frozen=True)
class Null(Result[Never, None]):
    @override
    def unwrap(self, expected: object = None) -> Never:
        raise UnwrapError(self, expected)

    @override
    def unwrap_err(self, expected: object = None) -> None:
        return None
