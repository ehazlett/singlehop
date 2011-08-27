import requests
from functools import wraps
import settings
import urllib
try:
    import simplejson as json
except ImportError:
    import json

class SingleHopError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class SingleHopModule(object):
    """
    Base class for SingleHop modules

    """
    def __init__(self, api_key=None, client_id=None, password=None, \
        endpoint_url=None, module=None):
        self._api_key = api_key
        self._client_id = client_id
        self._password = password
        self._endpoint_url = endpoint_url
        self._module = module
        # load defaults if needed
        if not self._api_key:
            self._api_key = settings.API_KEY
        if not self._client_id:
            self._client_id = settings.CLIENT_ID
        if not self._password:
            self._password = settings.PASSWORD
        if not self._endpoint_url:
            self._endpoint_url = settings.ENDPOINT_URL
    
    def _login_required(func):
        '''Decorator to check that auth credentials exist'''
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self._api_key or not self._client_id or not self._password:
                raise SingleHopError('You must specify an API key, client ID, and password')
            return func(self, *args, **kwargs)
        return wrapper
        
    @property # getter for _api_key
    def api_key(self):
        return self._api_key
    @property # getter for _client_id
    def client_id(self):
        return self._client_id
    @property # getter for _password
    def password(self):
        return self._password
    @property # getter for _endpoint_url
    def endpoint_url(self):
        return self._endpoint_url
    @property # getter for module
    def module(self):
        return self._module

    @_login_required
    def do_request(self, command=None, data=None):
        """
        Makes a request to the SingleHop API
    
        :keyword command: Module command to run
        :keyword data: Data to send
        :rtype: Response as JSON
    
        """
        request = {}
        # build auth dict
        _auth = {
            'key': self._api_key,
            'user': self._client_id,
            'password': self._password,
        }
        request['auth'] = _auth
        # build module dict
        _module = {
            'module': self._module,
            'command': command,
        }
        request['module'] = _module
        if data:
            if not isinstance(data, dict):
                raise SingleHopError('Data must be specified as a dict')
            request['data'] = data
        js = json.dumps(request).replace(' ', '%20')
        resp = requests.get(self._endpoint_url + js, timeout=10.0)
        return resp

