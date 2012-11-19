__author__ = 'mcalthrop'

import webapp2

class HelloWorld(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('hello world!')

app = webapp2.WSGIApplication([
    ('/helloworld', HelloWorld)
], debug=True)
