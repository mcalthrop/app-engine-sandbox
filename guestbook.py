__author__ = 'mcalthrop'

import page

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class GuestbookPage(page.Page):
    def get(self):
        user = users.get_current_user()

        if user:
            self.templateName = 'notsigned.template.html'
            self.templateValues = {
                'userNickname': user.nickname()
            }
            # call super
            page.Page.get(self)
        else:
            self.redirect(users.create_login_url(self.request.uri))

    def post(self):
        user = users.get_current_user()

        self.templateName = 'signed.template.html'
        self.templateValues = {
            'userNickname': user.nickname(),
            'comments': self.request.get('content')
        }
        # call super
        page.Page.post(self)

app = webapp.WSGIApplication(
    [
        ('/sign', GuestbookPage)
    ],
    debug=True
)

def main():
    run_wsgi_app(app)

main()

# EOF