import json
from nameko.web.handlers import http

class API:
    name = 'api'

    @http('GET', '/hello')
    def get_method(self):
        return json.dumps({'hello':'Mrgon96'})