import logging
import urllib
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union, overload

from elmclient import JazzTeamServer, JTSApp 
from requests.structures import CaseInsensitiveDict

from lxml import etree as ET

import requests.exceptions

from . import rdfxml
from . import oslcqueryapi
from . import utils
from . import httpops
from . import _validate
from . import _project

from .elmclient_types import ParamsType, RequestDataType

class _App(httpops.HttpOperations_Mixin, _validate.Validate_Mixin):
    domain: str
    project_class: Optional[Type[_App]]
    artifact_formats: List[str]
    reportablerest_baseurl: str
    supports_reportable_rest: bool
    reportable_rest_status: str
    majorVersion: Optional[str]
    version: Optional[str]
    contextroot: str
    baseurl: str
    jts: Optional[JTSApp]
    server: JazzTeamServer
    project_areas_xml: Optional[ET.ElementTree]
    _projects: Optional[Dict[str, str | Dict[str, Any]]]
    headers: Dict[str, str]
    cmServiceProviders: str
    iid: Optional[str]
    hooks: List[function]
    default_query_resource: Optional[str]

    def __init__(self, server: JazzTeamServer, contextroot: str, *, jts: Optional[JTSApp] = ...) -> None: ...
    def retrieve_cm_service_provider_xml(self) -> ET.ElementTree: ...
    def retrieve_oslc_catalog_xml(self) -> Optional[ET.ElementTree] : ...
    def _get_headers(self, headers: Optional[Dict[str, str]] = None) -> Dict[str, str]: ...
    def _get_request(
        self,
        verb: str,
        reluri: str = '',
        *,
        params: ParamsType = None,
        headers: Optional[Dict[str, str]] = None,
        data: RequestDataType = None
    ) -> httpops.HttpRequest: ...
    def _get_oslc_headers(self, headers: Optional[Dict[str, str]] = None) -> Dict[str, str]: ...
    def find_projectname_from_uri(self, name_or_uri: str) -> Optional[str]: ...
    def is_project_uri(self, uri: str) -> bool: ...
    def is_server_uri(self, uri: str) -> bool: ...
    def reluri(self, reluri: str = '') -> str: ...
    def _load_projects(self, include_archived: bool = False, force: bool = False) -> None: ...
    def find_project(self, projectname_or_uri: str, include_archived: bool = False) -> Optional[Type[_project._Project]]: ...
    def is_uri(self, name_or_uri: str) -> bool: ...
    def list_projects(self) -> List[Dict[str, str | Dict[str, Any]]]: ...
    def report_type_system(self) -> str: ...
    
    def get_query_capability_uri(self, resource_type: Optional[str] = None, context: Optional[Type[_App]] = None) -> str: ...
    def get_query_capability_uris(self, resource_type: Optional[str] = None, context: Optional[Type[_App]] = None) -> Dict[str, str]: ...
    def get_query_capability_uri_from_xml(self, capabilitiesxml: ET.ElementTree, resource_type: str, context: Optional[Type[_App]]) -> str: ...
    def get_query_capability_uris_from_xml(self, capabilitiesxml: ET.ElementTree, context: Optional[Type[_App]]) -> Dict[str, str]: ...
    
    @overload
    def get_factory_uri_from_xml(
        self,
        factoriesxml: ET.ElementTree,
        resource_type: str,
        context: Optional[Type[_App]],
        return_shapes: bool = False
    ) -> str: ...
    @overload
    def get_factory_uri_from_xml(
        self,
        factoriesxml: ET.ElementTree,
        resource_type: str,
        context: Optional[Type[_App]],
        return_shapes: bool = True
    ) -> Tuple[str, List[str]]: ...
    # default
    def get_factory_uri_from_xml(
        self,
        factoriesxml: ET.ElementTree,
        resource_type: str,
        context: Optional[Type[_App]],
        return_shapes: bool = False
    ) -> Union[str, Tuple[str, List[str]]]: ...
    
    def get_factory_uris_from_xml(self, factoriesxml: ET.ElementTree, context: Optional[Type[_App]]) -> Dict[str, str]: ...
    def is_user_uri(self, uri: str) -> bool: ...
    def user_uritoname_resolver(self, uri: str) -> str: ...
    def is_user_name(self, name: str) -> bool: ...
    def user_nametouri_resolver(self, name: str, raiseifinvalid: bool = True) -> Optional[str]: ...
    def resolve_project_nametouri(self, name: str, raiseifinvalid: bool = True) -> Optional[str]: ...
    def is_accessible(self, uri: str) -> bool: ...

class JTSApp(_App):
    domain: str
    project_class: Optional[Type[_App]]
    supports_configs: bool
    supports_components: bool
    supports_reportable_rest: bool

    def __init__(self, server: JazzTeamServer, contextroot: str, jts: Any = ...) -> None: ...
    def find_project(self, projectname: str) -> None: ...