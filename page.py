__author__ = 'mcalthrop'

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class Page(webapp.RequestHandler):
    templateName = ''
    templateFile = ''
    templateValues = {}

    def __init__(self, request, response, templateName = None, templateValues = None):
        if templateName is None:
            templateName = ''
        if templateValues is None:
            templateValues = {}

        self.templateName = templateName
        self.templateValues = templateValues

        # call super
        webapp.RequestHandler.__init__(self, request, response)

    def render(self):
        if self.templateName:
            self.templateFile = os.path.join(os.path.dirname(__file__), 'templates', self.templateName)
            self.response.out.write(template.render(self.templateFile, self.templateValues))

    def get(self):
        self.render()

    def post(self):
        self.render()

# EOF