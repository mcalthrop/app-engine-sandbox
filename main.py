#!/usr/bin/env python

__author__ = 'mcalthrop'

import cgi
import os

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/html'

            templateValues = {
                'userNickname': user.nickname()
            }

            templateFile = os.path.join(os.path.dirname(__file__), 'templates', 'home.template.html')
            self.response.out.write(template.render(templateFile, templateValues))
        else:
            self.redirect(users.create_login_url(self.request.uri))

app = webapp.WSGIApplication(
    [
        ('/', MainPage)
    ],
    debug=True
)

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()

