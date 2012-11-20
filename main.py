#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
__author__ = 'mcalthrop'

import cgi
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/html'

            templateValues = {
                'userNickname': user.nickname()
            }

            path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
            self.response.out.write(template.render(path, templateValues))
        else:
            self.redirect(users.create_login_url(self.request.uri))

class GuestbookPage(webapp.RequestHandler):
    def common(self):
        self.response.out.write('<p>Go <a href="/">home</a>.</p></body></html>')

    def post(self):
        self.response.out.write('<html><body>You wrote:<pre>')
        self.response.out.write(cgi.escape(self.request.get('content')))
        self.response.out.write('</pre></body></html>')
        self.common()

    def get(self):
        self.response.out.write('<html><body><p>You ain\'t written nuffink yet.</p>')
        self.common()

app = webapp.WSGIApplication(
    [
        ('/', MainPage),
        ('/sign', GuestbookPage)
    ],
    debug=True
)

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()

