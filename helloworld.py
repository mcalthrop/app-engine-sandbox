__author__ = 'mcalthrop'

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class HelloWorld(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('hello there, world')

app = webapp.WSGIApplication(
    [
        ('/helloworld', HelloWorld)
    ],
    debug=True
)

run_wsgi_app(app)

