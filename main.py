__author__ = 'mcalthrop'

import page

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(page.Page):
    def __init__(self, request, response):
        page.Page.__init__(self, request, response, 'index.template.html')

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

# EOF