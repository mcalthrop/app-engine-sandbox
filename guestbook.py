__author__ = 'mcalthrop'

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class GuestbookPage(webapp.RequestHandler):
    def post(self):
        templateValues = {
            'comments': self.request.get('content')
        }
        templateFile = os.path.join(os.path.dirname(__file__), 'templates', 'signed.template.html')
        self.response.out.write(template.render(templateFile, templateValues))

    def get(self):
        templateFile = os.path.join(os.path.dirname(__file__), 'templates', 'notsigned.template.html')
        self.response.out.write(template.render(templateFile, {}))

app = webapp.WSGIApplication(
    [
        ('/sign', GuestbookPage)
    ],
    debug=True
)

def main():
    run_wsgi_app(app)

main()

