
import routes.middleware  
import webob.dec  
import webob.exc


class Controller(object):  
    @webob.dec.wsgify  
    def __call__(self, req):  
        return webob.Response("Hello Router!!!")

class Router(object):
    def __init__(self):
        self._mapper = routes.Mapper()
        self._mapper.connect('/spch',
                             controller = Controller(),
                             action = 'index',
                             condition = {'method': ['GET']})
        self._router = routes.middleware.RoutesMiddleware(self._dispatch, self._mapper)

    @classmethod  
    def app_factory(cls, global_config, **local_config):    
        return cls()  
     
    @webob.dec.wsgify  
    def __call__(self, req):  
        return self._router  
 
    @staticmethod  
    @webob.dec.wsgify  
    def _dispatch(req):  
        match = req.environ['wsgiorg.routing_args'][1]  
                  
        if not match:  
            return webob.exc.HTTPNotFound()  
          
        app = match['controller']    
        return app
