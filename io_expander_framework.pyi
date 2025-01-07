# Copyright (c) 2024 - 2025 Kevin G. Schlosser

from typing import Union, Optional, ClassVar

EXIO1: int = ...
EXIO2: int = ...
EXIO3: int = ...
EXIO4: int = ...
EXIO5: int = ...
EXIO6: int = ...
EXIO7: int = ...
EXIO8: int = ...

class Pin(object):
    IN: ClassVar[int] = ...
    OUT: ClassVar[int] = ...

    _id: int = ...
    _mode: int = ...
    _buf: bytearray = ...
    _mv: memoryview = ...

    def __init__(self, id: int, mode: int = -1, value: Optional[int] = None):
        ...

    def init(self, mode: int = -1, value: Optional[int] = None):
        ...

    def value(self, x: Optional[int] = None) -> Optional[int]:
        ...

    def __call__(self, x: Optional[int] = None) -> Optional[int]:
        ...

    def on(self) -> None:
        ...

    def off(self) -> None:
        ...

    def low(self) -> None:
        ...

    def high(self) -> None:
        ...

    def mode(self, mode: Optional[int] = None) -> Optional[int]:
        ...

    def _set_dir(self, direction: int):
        ...

    def _set_level(self, level: Union[int, float]):
        ...

    def _get_level(self) -> Optional[Union[int, float]]:
        ...
