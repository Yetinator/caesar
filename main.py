#!/usr/bin/env python
import os
import webapp2
import jinja2
template_dir=os.path.join(os.path.dirname(__file__), 'templates')#creates a path
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))#assigns path to the environment
from caesar import *
from helpers import *

class Handler(webapp2.RequestHandler):
    """
        Magic handler
    """
    def write(self, *a, **kw):
        """
        Writes whatever I tell it.  I'm the boss.  
        """
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        """
            creates a jinja template object out of thin air and pukes it into 
            the calling function. (in this case render() so it can later be 
            written)
        """
        t = jinja_env.get_template(template)
        return t.render(params)
       
    def render(self, template, **kw):
        """
            calls the write method and the render_str function
        """
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        """
            Good for the inital document call
        """
        
        self.render('userForm.html')
        
    def post(self):
        """
            reforms the page after user input
        """
        message = self.request.get('message')
        rot= int(self.request.get('rot'))
        output = encrypt(message, rot)
        self.render('userForm.html', userin=output)

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
