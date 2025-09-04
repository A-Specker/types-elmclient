from lxml import etree as ET
from typing import Any, Dict, List, Optional, Tuple, Union, Mapping, Iterable, BinaryIO

JSONType = Union[dict[str, Any], list[Any], str, int, float, bool, None]
RequestDataType = Union[
    Mapping[str, str],
    Iterable[Tuple[str, str]],
    str,
    bytes,
    bytearray,
    BinaryIO, 
    Iterable[bytes],
    ET.Element,
    ET.ElementTree
    None,
]
ParamValue = Union[str, bytes, int, float, bool, None]
ParamsType = Optional[
    Union[
        Mapping[str, ParamValue],
        Iterable[Tuple[str, ParamValue]],
    ]
]