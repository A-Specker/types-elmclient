import collections
import datetime
import logging
import lxml.etree as ET
from typing import Any, Dict, List, Optional, Tuple, Union

CHECKERROR: str = 'ERROR'
CHECKWARNING: str = 'WARNING'
CHECKINFO: str = 'INFO'

OT_URI_MISSING: Tuple[str, str]
OT_DUPLICATE_URI: Tuple[str, str]
OT_DUPLICATE_NAME: Tuple[str, str]
AD_URI_MISSING: Tuple[str, str]
AD_UNUSED: Tuple[str, str]
AD_DUPLICATE_URI: Tuple[str, str]
AD_DUPLICATE_NAME: Tuple[str, str]
AD_BASE_TYPE_CHECK_NEEDED: Tuple[str, str]
AT_UNUSED: Tuple[str, str]
AT_URI_MISSING: Tuple[str, str]
AT_ENUMVALUE_URI_MISSING: Tuple[str, str]
AT_DUPLICATE_URI: Tuple[str, str]
AT_DUPLICATE_NAME: Tuple[str, str]
AT_ENUMVALUE_DUPLICATE_NAME: Tuple[str, str]
AT_ENUMVALUE_DUPLICATE_URI: Tuple[str, str]
AT_ENUMVALUE_DUPLICATE_VALUE: Tuple[str, str]
LT_URI_MISSING: Tuple[str, str]
LT_DUPLICATE_URI: Tuple[str, str]
LT_DUPLICATE_NAME: Tuple[str, str]
OT_RENAMED: Tuple[str, str]
OT_URI_ADDED: Tuple[str, str]
OT_URI_REMOVED: Tuple[str, str]
OT_URI_CHANGED: Tuple[str, str]
OT_AD_REMOVED: Tuple[str, str]
OT_AD_ADDED: Tuple[str, str]
AD_RENAMED: Tuple[str, str]
AD_URI_ADDED: Tuple[str, str]
AD_URI_REMOVED: Tuple[str, str]
AD_URI_CHANGED: Tuple[str, str]
AD_WAS_MULTIVALUED: Tuple[str, str]
AD_BECAME_MULTIVALUED: Tuple[str, str]
AD_BASE_TYPE_URL_CHANGED: Tuple[str, str]
AT_RENAMED: Tuple[str, str]
AT_URI_ADDED: Tuple[str, str]
AT_URI_REMOVED: Tuple[str, str]
AT_URI_CHANGED: Tuple[str, str]
AT_BASE_TYPE_URL_CHANGED: Tuple[str, str]
AT_ENUM_REMOVED: Tuple[str, str]
AT_ENUM_ADDED: Tuple[str, str]
AT_ENUMVALUE_REMOVED: Tuple[str, str]
AT_ENUMVALUE_ADDED: Tuple[str, str]
AT_ENUMVALUE_RENAMED: Tuple[str, str]
AT_ENUMVALUE_URI_CHANGED: Tuple[str, str]
AT_ENUMVALUE_VALUE_CHANGED: Tuple[str, str]
LT_RENAMED: Tuple[str, str]
LT_URI_ADDED: Tuple[str, str]
LT_URI_REMOVED: Tuple[str, str]
LT_URI_CHANGED: Tuple[str, str]
OT_NOT_IN_REF: Tuple[str, str]
AD_NOT_IN_REF: Tuple[str, str]
AT_NOT_IN_REF: Tuple[str, str]
LT_NOT_IN_REF: Tuple[str, str]
OT_URI_INCONSISTENT: int
OT_NAME_INCONSISTENT: int
OT_PRESENCE_INCONSISTENT: int
AD_URI_INCONSISTENT: int
AD_NAME_INCONSISTENT: int
AD_PRESENCE_INCONSISTENT: int
AT_URI_INCONSISTENT: int
AT_NAME_INCONSISTENT: int
AT_PRESENCE_INCONSISTENT: int
AT_ENUMVALUE_URI_INSISTENT: int
AT_ENUMVALUE_NAME_INCONSISTENT: int
AT_ENUMVALUE_PRESENCE_INCONSISTENT: int
DUPLICATED_NAME: Tuple[str, str]
OT_RDFURI_NOT_IN_ALL_STREAMS: Tuple[str, str]
AD_RDFURI_NOT_IN_ALL_STREAMS: Tuple[str, str]
AT_RDFURI_NOT_IN_ALL_STREAMS: Tuple[str, str]
AT_ENUMVALUE_RDFURI_NOT_IN_ALL_STREAMS: Tuple[str, str]
LT_RDFURI_NOT_IN_ALL_STREAMS: Tuple[str, str]

def fstr(template: str) -> str: ...
def expand(errorname: str) -> Tuple[str, str, str]: ...

class _TypeChecker(object):
    pass

class OTChecker(_TypeChecker):
    pass

class ADChecker(_TypeChecker):
    pass

class ATChecker(_TypeChecker):
    pass

class _DNType(object):
    URL: Optional[str]
    URI: Optional[str]
    name: Optional[str]
    isused: bool
    title: str
    url: Optional[str]
    uri: Optional[str]
    label: Optional[str]
    modified: Optional[str]
    modifiedBy: Optional[str]

    def __init__(
        self,
        url: Optional[str],
        uri: Optional[str],
        name: Optional[str],
        label: Optional[str],
        isused: bool = False,
        modified: Optional[str] = None,
        modifiedBy: Optional[str] = None,
    ) -> None: ...
    def __repr__(self) -> str: ...

class OT(_DNType):
    attriburls: List[str]
    title: str = "OT"
    
    def __init__(
        self,
        url: Optional[str],
        uri: Optional[str],
        name: Optional[str],
        label: Optional[str],
        attriburls: List[str],
        modified: Optional[str] = None,
        modifiedBy: Optional[str] = None,
        isused: bool = False,
    ) -> None: ...

class AD(_DNType):
    aturl: Optional[str]
    ismultivalued: bool
    title: str = "AD"
    basetypeurl: Optional[str]
    
    def __init__(
        self,
        url: Optional[str],
        uri: Optional[str],
        name: Optional[str],
        label: Optional[str],
        aturl: Optional[str],
        ismultivalued: bool,
        modified: Optional[str] = None,
        modifiedBy: Optional[str] = None,
        isused: bool = False,
    ) -> None: ...

class AT(_DNType):
    basetypeurl: Optional[str]
    isenum: bool
    enumvalues: Dict[str, Any]
    title: str = "AT"

    def __init__(
        self,
        url: Optional[str],
        uri: Optional[str],
        name: Optional[str],
        label: Optional[str],
        basetypeurl: Optional[str],
        isenum: bool,
        enumvalues: Optional[Dict[str, Any]] = ...,
        modified: Optional[str] = ...,
        modifiedBy: Optional[str] = ...,
        isused: bool = ...,
    ) -> None: ...

class EnumValue(_DNType):
    value: Any
    def __init__(
        self,
        enum_u: Optional[str],
        label: Optional[str],
        value: Any,
        sameas: Optional[str],
    ) -> None: ...

class LT(_DNType):
    title: str
    def __init__(
        self,
        url: Optional[str],
        uri: Optional[str],
        name: Optional[str],
        label: Optional[str],
        modified: Optional[str] = None,
        modifiedBy: Optional[str] = None,
        isused: bool = False,
    ) -> None: ...

### spx: start below here

class TypeSystem(object):
    ots: Dict[str, OT]
    ads: Dict[str, AD]
    ats: Dict[str, AT]
    lts: Dict[str, LT]
    config_u: Optional[str]
    config_name: Optional[str]
    uris: Any
    names: Any
    otnames: Any
    adnames: Any
    atnames: Any
    ltnames: Any

    def __init__(self, config_name: Optional[str], config_u: Optional[str]) -> None: ...
    def __repr__(self) -> str: ...
    def load_ot(self, serverconnection: Any, url: str, iscacheable: bool = ..., isused: bool = ...) -> None: ...
    def load_ad(self, serverconnection: Any, url: str, iscacheable: bool = ..., isused: bool = ...) -> None: ...
    def load_at(self, serverconnection: Any, url: str, iscacheable: bool = ..., isused: bool = ...) -> None: ...
    def load_lt(self, serverconnection: Any, url: str, iscacheable: bool = ..., isused: bool = ...) -> None: ...
    def checkinternalconsistency(self) -> List[Any]: ...
    def checkagainstothertypesystem(
        self,
        theothertypesystem: "TypeSystem",
        verbose: bool = ...,
        comparewithref: bool = ...,
        allowmoreina: bool = ...,
    ) -> List[Any]: ...

class ComponentTypeSytem(object):
    localconfigtree: Any