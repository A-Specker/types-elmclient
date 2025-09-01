import argparse
import logging
import lxml.etree as ET
import requests
from typing import Any, Dict, List, Optional, Tuple, Type, Union
from elmclient import utils

from elmclient import _app
from elmclient import _project
from elmclient import _typesystem
from elmclient import server
from elmclient import resource


def callers() -> str: ...

class CCMProject(_project._Project, resource.Resources_Mixin):
    default_query_resource: str
    typesystem_loaded: bool

    def __init__(self, name: str, project_uri: str, app: _app._App, is_optin: bool, singlemode: bool) -> None: ...
    def _load_types(self, force: bool = False) -> None: ...
    def _load_type_from_resource_shape(self, el: ET.Element, supershape: Any = None) -> Optional[int]: ...
    def app_resolve_uri_to_name(self, uri: str) -> Optional[str]: ...
    def get_missing_uri_title(self, uri: str) -> Optional[str]: ...
    def type_name_from_uri(self, uri: str) -> str: ...
    def resource_id_from_uri(self, uri: str) -> str: ...
    def is_resource_uri(self, uri: str) -> bool: ...
    def is_type_uri(self, uri: str) -> bool: ...
    def resolve_uri_to_name(self, uri: str, trytouseasid: bool = False) -> Optional[str]: ...

@utils.mixinomatic
class CCMApp(_app._App, _typesystem.No_Type_System_Mixin):
    domain: str = 'ccm'
    project_class: Type[CCMProject] = CCMProject
    supports_configs: bool = False
    supports_components: bool = False
    reportablerestbase: str = 'rpt/repository'
    supports_reportable_rest: bool = True
    reportable_rest_status: str = "Application supports Reportable REST but represt for ccm not fully tested/working"
    artifact_formats: List[str] = [
        'foundation',
        'scm',
        'build',
        'apt',
        'workitem'
    ]
    identifier_name: str = 'id'
    identifier_uri: str = 'dcterms:identifier'
    _rr_queryable: List[str] = [
        'workitem/projectArea/name',
        'workitem/workItem/id',
        'workitem/workItem/type/id',
        'workitem/workItem/target/name',
        'workitem/workItem/tags',
        'workitem/workItem/state/id',
        'workitem/workItem/state/group',
    ]
    _rr_unqueryable: List[str] = [
        'workitem/workItem/type',
        'workitem/workItem/teamArea',
    ]

    rootservices_xml: ET.Element
    serviceproviders: str

    def __init__(self, server: _app.JazzTeamServer, contextroot: str, jts: Optional[_app.JTSApp] = None) -> None: ...
    def _get_headers(self, headers: Optional[Dict[str, str]] = None) -> Dict[str, str]: ...
    @classmethod
    def add_represt_arguments(cls, subparsers: argparse._SubParsersAction, common_args: argparse.ArgumentParser) -> None: ...
    def process_represt_arguments(self, args: argparse.Namespace, allapps: List[Type[_app._App]]) -> Tuple[str, Dict[str, str], Dict[str, str]]: ...

class AMProject(CCMProject):
    default_query_resource: str = 'oslc_am:Resource'
    def __init__(self, name: str, project_uri: str, app: _app._App, is_optin: bool, singlemode: bool) -> None: ...

@utils.mixinomatic
class AMApp(_app._App, _typesystem.No_Type_System_Mixin):
    domain: str = "am"
    project_class: Type[AMProject]
    supports_configs: bool = False
    supports_components: bool = False
    supports_reportable_rest: bool = False
    reportable_rest_status: str = "Application does not support Reportable REST"
    identifier_uri: str = 'dcterms:identifier'
    
    rootservices_xml: ET.Element
    serviceproviders: str = 'oslc_am:amServiceProviders'

    def __init__(self, server: server.JazzTeamServer, contextroot: str, jts: Optional[_app.JTSApp] = None) -> None: ...
    def _get_headers(self, headers: Optional[Dict[str, str]] = None) -> Dict[str, str]: ...