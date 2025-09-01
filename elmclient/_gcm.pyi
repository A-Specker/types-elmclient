# gcm.pyi
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
import lxml.etree as ET
import requests
from . import _app, _project, _typesystem, oslcqueryapi, rdfxml, utils, server

_hook_beforequery: Callable[[Dict[str, str]], Dict[str, Any]]

class GCMProject(_project._Project):
    hooks: List[Callable[[Dict[str, Any]], Dict[str, Any]]]
    _components: Optional[Dict[str, Dict[str, Any]]]
    _configurations: Optional[Dict[str, Any]]
    default_query_resource: str = 'oslc_config:Configuration'
    services_uri: Optional[str]
    services_xml: Optional[ET._Element]

    def __init__(
        self,
        name: str,
        project_uri: str,
        app: _app._App,
        is_optin: bool = False,
        singlemode: bool = False,
        defaultinit: bool = True,
    ) -> None: ...
    
    def find_local_component(self, name_or_uri: str) -> Optional[Any]: ...
    def list_components(self) -> List[str]: ...
    def load_components_and_configurations(self, force: bool = False) -> Optional[Tuple[int, int]]: ...
    def _load_types(self, force: bool = False) -> None: ...
    def _load_type_from_resource_shape(self, el: ET._Element, supershape: Optional[Tuple[str,str]] = None) -> int: ...
    def _generic_load_type_from_resource_shape(self, el: ET._Element, supershape: Optional[Tuple[str,str]] = None) -> int: ...
    def _get_typeuri_rdf(self, uri: str) -> ET._Element: ...
    def app_resolve_uri_to_name(self, uri: str) -> Optional[str]: ...
    def resolve_uri_to_name(
        self,
        uri: str,
        prefer_same_as: bool = True,
        dontpreferhttprdfrui: bool = True
    ) -> Optional[str]: ...
    def resolve_property_name_to_uri(self, name: str, exception_if_not_found: bool = True) -> Optional[str]: ...

class GCMComponent(GCMProject):
    pass

@utils.mixinomatic
class GCMApp(_app._App, oslcqueryapi._OSLCOperations_Mixin, _typesystem.Type_System_Mixin):
    domain: str
    project_class: type[GCMProject]
    supports_configs: bool
    supports_components: bool
    supports_reportable_rest: bool
    relprefixes: Tuple[Tuple[str,str], ...]
    identifier_name: str
    identifier_uri: str
    rootservices_xml: ET._Element
    serviceproviders: str
    default_query_resource: str
    hooks: List[Any]
    iid: Optional[str]

    def __init__(self, server: Any, contextroot: str, jts: Optional[Any] = None) -> None: ...
    def _get_headers(self, headers: Optional[Dict[str,str]] = None) -> Dict[str,str]: ...
    def get_query_capability_uris_from_xml(self, capabilitiesxml: ET._Element, context: Any) -> Dict[str,str]: ...
    def check_valid_config_uri(self, uri: str, raise_exception: bool = True) -> bool: ...
    def load_types(self, force: bool = False) -> None: ...
    def _load_types(self, force: bool = False) -> None: ...
    def _load_type_from_resource_shape(self, el: ET._Element, supershape: Optional[Tuple[str,str]] = None) -> int: ...
    def _generic_load_type_from_resource_shape(self, el: ET._Element, supershape: Optional[Tuple[str,str]] = None) -> int: ...
    def _get_typeuri_rdf(self, uri: str) -> ET._Element: ...
    def resolve_uri_to_name(
        self,
        uri: str,
        prefer_same_as: bool = True,
        dontpreferhttprdfrui: bool = True
    ) -> Optional[str]: ...
    def resolve_property_name_to_uri(self, name: str, exception_if_not_found: bool = True) -> Optional[str]: ...
