from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Cell(_message.Message):
    __slots__ = ("alive", "color")
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    alive: bool
    color: int
    def __init__(self, alive: bool = ..., color: _Optional[int] = ...) -> None: ...

class CellRow(_message.Message):
    __slots__ = ("cells",)
    CELLS_FIELD_NUMBER: _ClassVar[int]
    cells: _containers.RepeatedCompositeFieldContainer[Cell]
    def __init__(self, cells: _Optional[_Iterable[_Union[Cell, _Mapping]]] = ...) -> None: ...

class Grid(_message.Message):
    __slots__ = ("width", "height", "rows")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    rows: _containers.RepeatedCompositeFieldContainer[CellRow]
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., rows: _Optional[_Iterable[_Union[CellRow, _Mapping]]] = ...) -> None: ...
