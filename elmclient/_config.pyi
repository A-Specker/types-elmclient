from typing import Any, Union, Optional, List


BASELINE: int = 1
STREAM: int = 2
CHANGESET: int = 3


class _Config:
    configtype: Optional[int] = None

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def is_stream(self) -> bool: ...
    def is_baseline(self) -> bool: ...
    def is_changeset(self) -> bool: ...


class _Stream(_Config):
    configtype: int = STREAM
    from_baseline: Optional["_Baseline"]
    baselines: List["_Baseline"]
    changesets: List["_Changeset"]

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def create_baseline(self) -> None: ...
    def create_changeset(self) -> None: ...

class _Baseline(_Config):
    configtype: int = BASELINE
    instream: Optional[_Stream]
    streams: List[_Stream]

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def create_stream(self) -> None: ...

class _Changeset(_Config):
    configtype: int = CHANGESET
    instream: Optional[_Stream]

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def deliver(self) -> None: ...
    def discard(self) -> None: ...
