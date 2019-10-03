import json
from nameko.web.handlers import http
from werkzeug.wrappers import Response

class HttpService:
    name = "http_service"

    @http('GET', '/get/<int:value>')
    def get_method(self, request, value):
        return json.dumps({'Number': value})

    @http('POST', '/post')
    def do_post(self, request):
        return u"received: {}".format(request.get_data(as_text=True))

    @http('GET,PUT,POST,DELETE', '/multi')
    def do_multi(self, request):
        return request.method

    @http('GET', '/user')
    def get_user(self, request):
        # return 202, json.dumps({'Username': 'Mrgon96'})
        return Response(json.dumps(({"Username":"Mrgon96"})), status=202)



