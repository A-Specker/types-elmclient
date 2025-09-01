##
## © Copyright 2021- IBM Inc. All rights reserved
# SPDX-License-Identifier: MIT
##

import codecs
import html.parser
import http
import json
import lxml.etree as ET
import requests
import tqdm
from typing import Any, Dict, List, Optional, Tuple, Union, Mapping, Iterable, BinaryIO, overload

from .elmclient_types import JSONType, RequestDataType, ParamsType, ParamValue


COOKIE_SAVE_FILE: str
logger: Any
is_windows: bool

def quote(s: str) -> str: ...
def to_curl(request: requests.Request, compressed: bool = False, verify: bool = True) -> str: ...

AP_PREFIX: str

def find_encoding(response: requests.Response, encoding: Optional[str]) -> str: ...
def to_text(response: Optional[Union[requests.Response, str, bytes]], encoding: Optional[str] = None, errors: str = 'replace') -> str: ...
def to_text_strict(response: Optional[Union[requests.Response, str, bytes]], encoding: Optional[str] = None) -> str: ...
def to_binary_xml(text: Union[str, bytes], encoding: Optional[str] = None, errors: str = 'xmlcharrefreplace') -> bytes: ...
def to_binary(text: Union[str, bytes], encoding: Optional[str] = None, errors: str = 'strict') -> bytes: ...
# TODO: requests.cookies is not a class
def getcookievalue(cookies: requests.cookies, cookiename: str, defaultvalue: Optional[str] = None) -> Optional[str]: ...
def findbasepagelink(linkheader: Optional[str], rel: str) -> Optional[str]: ...

class _FormParser(html.parser.HTMLParser):
    is_in_form: bool
    method: Optional[str]
    action: Optional[str]
    name: str
    passwrod: str  # note: typo preserved from implementation

    def __init__(self) -> None: ...
    def handle_starttag(self, tagname: str, attrs: List[Tuple[str, str]]) -> None: ...

class HttpOperations_Mixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    
    def execute_get_xml(self, reluri: str, *, params: Optional[Dict[str, str]] = None,
                        headers: Optional[Dict[str, str]] = None, **kwargs: Any) -> ET.ElementTree: ...
    @overload
    def execute_get_rdf_xml(self, reluri: str, *, params: Optional[Dict[str, str]] = None,
                            headers: Optional[Dict[str, str]] = None,
                            return_etag: bool = True,
                            return_headers: bool = False,
                            merge_linked_pages: bool = False,
                            warn_linked_pages: bool = True,
                            **kwargs: Any) -> Tuple[ET.ElementTree, str]: ...
    @overload
    def execute_get_rdf_xml(self, reluri: str, *, params: Optional[Dict[str, str]] = None,
                            headers: Optional[Dict[str, str]] = None,
                            return_etag: bool = False,
                            return_headers: bool = True,
                            merge_linked_pages: bool = False,
                            warn_linked_pages: bool = True,
                            **kwargs: Any) -> Tuple[ET.ElementTree, Dict[str, str]]: ...
    @overload
    def execute_get_rdf_xml(self, reluri: str, *, params: Optional[Dict[str, str]] = None,
                            headers: Optional[Dict[str, str]] = None,
                            return_etag: bool = False,
                            return_headers: bool = False,
                            merge_linked_pages: bool = False,
                            warn_linked_pages: bool = True,
                            **kwargs: Any) -> ET.ElementTree: ...
    # default signature for linters
    def execute_get_rdf_xml(self, reluri: str, *, params: Optional[Dict[str, str]] = None,
                            headers: Optional[Dict[str, str]] = None,
                            return_etag: bool = False,
                            return_headers: bool = False,
                            merge_linked_pages: bool = False,
                            warn_linked_pages: bool = True,
                            **kwargs: Any) -> Union[ET.ElementTree, Tuple[ET.ElementTree, str], Tuple[ET.ElementTree, Dict[str, str]]]: ...
    
    def execute_put_rdf_xml(self, reluri: str, *, data: RequestDataType = None,
                            params: Optional[Dict[str, str]] = None,
                            headers: Optional[Dict[str, str]] = None,
                            **kwargs: Any) -> requests.Response: ... 
    
    def execute_post_rdf_xml(self, reluri: str, *, data: RequestDataType = None,
                             params: ParamsType = None,
                             headers: Optional[Dict[str, str]] = None,
                             put: bool = False,
                             **kwargs: Any) -> requests.Response: ...  
    
    def execute_post_json(self, reluri: str, *, data: RequestDataType = None,
                          params: ParamsType = None,
                          headers: Optional[Dict[str, str]] = None,
                          put: bool = False,
                          **kwargs: Any) -> requests.Response: ...
    
    def execute_delete(self, reluri: str, *, params: ParamsType = None,
                       headers: Optional[Dict[str, str]] = None,
                       **kwargs: Any) -> requests.Response: ...
    @overload
    def execute_get_json(self, reluri: str, *, params: ParamsType = None,
                         headers: Optional[Dict[str, str]] = None,
                         return_etag: bool = False,
                         **kwargs: Any) -> JSONType: ...
    @overload
    def execute_get_json(self, reluri: str, *, params: ParamsType = None,
                         headers: Optional[Dict[str, str]] = None,
                         return_etag: bool = True,
                         **kwargs: Any) -> Tuple[JSONType, str]: ...
    # default
    def execute_get_json(self, reluri: str, *, params: ParamsType = None,
                         headers: Optional[Dict[str, str]] = None,
                         return_etag: bool = False,
                         **kwargs: Any) -> Union[JSONType, Tuple[JSONType, str]]: ...
    @overload
    def execute_get_json_soap(self, reluri: str, *, params: ParamsType = None,
                              headers: Optional[Dict[str, str]] = None,
                              return_etag: bool = False,
                              **kwargs: Any) -> JSONType: ...
    @overload
    def execute_get_json_soap(self, reluri: str, *, params: ParamsType = None,
                              headers: Optional[Dict[str, str]] = None,
                              return_etag: bool = True,
                              **kwargs: Any) -> Tuple[JSONType, str]: ...
    # default
    def execute_get_json_soap(self, reluri: str, *, params: ParamsType = None,
                              headers: Optional[Dict[str, str]] = None,
                              return_etag: bool = False,
                              **kwargs: Any) -> Union[Tuple[JSONType, str], JSONType]: ...
    
    def execute_get_binary(self, reluri: str, *, params: ParamsType = None,
                           headers: Optional[Dict[str, str]] = None,
                           **kwargs: Any) -> requests.Response: ...
    
    def execute_post_content(self, uri: str, *, params: ParamsType = None,
                             data: RequestDataType = None,
                             headers: Optional[Dict[str, str]] = None,
                             put: bool = False,
                             **kwargs: Any) -> requests.Response: ...
    
    def execute_get(self, reluri: str, *, params: ParamsType = None,
                    headers: Optional[Dict[str, str]] = None,
                    **kwargs: Any) -> bytes: ...
    
    def execute_get_raw(self, reluri: str, *, params: ParamsType = None,
                        headers: Optional[Dict[str, str]] = None,
                        **kwargs: Any) -> requests.Response: ...
    
    def wait_for_tracker(self, location: str, *, interval: float = 1.0,
                         progressbar: bool = False, msg: str = 'Waiting for tracker',
                         useJson: bool = False, returnFinal: bool = False) -> Union[requests.Response, str]: ...
    
    def record_action(self, action: str) -> None: ...
    
    # internal helpers
    def _get_get_request(self, reluri: str = '', *, params: ParamsType = None,
                         headers: Optional[Dict[str, str]] = None) -> HttpRequest : ... # maybe quote this
    
    def _get_post_request(self, reluri: str = '', *, params: ParamsType = None,
                          headers: Optional[Dict[str, str]] = None,
                          data: RequestDataType = None,
                          put: bool = False) -> HttpRequest: ... # maybe quote this
    
    def _get_delete_request(self, reluri: str = '', *, params: ParamsType = None,
                            headers: Optional[Dict[str, str]] = None) -> HttpRequest: ... # maybe quote this

def chooseconfigheader(configurl: str) -> str: ...

class HttpRequest:
    _req: requests.Request
    _session: requests.Session

    def __init__(self, session: requests.Session, verb: str, uri: str, *, params: ParamsType = None,
                 headers: Optional[Dict[str, str]] = None,
                 data: RequestDataType = None) -> None: ...
    
    def get_user_password(self, url: Optional[str] = None) -> Tuple[str, str]: ...
    def get_app_password(self, url: str) -> Optional[str]: ...
    def execute(self, no_error_log: bool = False, close: bool = False, **kwargs: Any) -> requests.Response: ...
    
    def log_redirection_history(self, response: requests.Response, intent: str, action: Optional[str] = None, donotlogbody: bool = False) -> None: ...
    def _log_request(self, request: requests.Request, donotlogbody: bool = False, intent: Optional[str] = None,
                     action: Optional[str] = None) -> str: ...
    def _log_response(self, response: requests.Response, action: Optional[str] = None) -> str: ...
    def _callers(self) -> str: ...
    def _is_retryable_error(self, e: requests.RequestException) -> bool: ...
    def get_auth_path(self, request_url: str, response: requests.Response) -> str: ...
    def _execute_request(self, *, no_error_log: bool = False, close: bool = False,
                         cacheable: bool = True, **kwargs: Any) -> requests.Response: ...
    def _execute_one_request_with_login(self, *, no_error_log: bool = False,
                                        close: bool = False, donotlogbody: bool = False,
                                        retry_get_after_login: bool = True,
                                        remove_headers: Optional[List[str]] = None,
                                        remove_parameters: Optional[List[str]] = None,
                                        intent: Optional[str] = None,
                                        action: Optional[str] = None,
                                        automaticlogin: bool = True,
                                        showcurl: bool = False,
                                        keepconfigurationcontextheader: bool = False) -> requests.Response: ... # spx correct return
    
    # login/authorization
    def _login(self, auth_url: str) -> None: ...
    def _jsa_login(self, auth_url: str, ap_redirect_url: Optional[str], url: str) -> Optional[requests.Response]: ...
    def _authorize(self, auth_url: str) -> None: ...
    def _jazz_form_authorize(self, request_url: str, prev_request: requests.Request, prev_response: requests.Response) -> requests.Response: ...
