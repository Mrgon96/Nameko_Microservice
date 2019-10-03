from nameko.rpc import rpc

class HelloService:
    name = "hello_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)

