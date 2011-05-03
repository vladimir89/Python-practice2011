import wsgiref.handlers
import os

from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.ext import webapp

class MainPage(webapp.RequestHandler):
    def get(self):
        comentt = self.request.get('coment')
        template_values = {'cont': comentt}
        path = os.path.join(os.path.dirname(__file__), 'form.html')
        self.response.out.write(template.render(path, template_values))
    


'''class Mess_store(db.Model):
    author = db.UserProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class Write_on_store(webapp.RequestHandler):
    def post(self):
        coment = Mess_store()

        coment.author = self.request.get('Vasya')
        coment.content = self.request.get('Hello all!!!')

        coment.put()
        self.redirect('/')

class InStore (webapp.RequestHandler):
    #def __init__():
        
    def post(self):
        self.response.out.write('<html><body>You wrote:<pre>')
        self.response.out.write(self.request.get('comentt'))
        self.response.out.write('</pre></body></html>')'''

application = webapp.WSGIApplication([('/', MainPage)], debug=True)       
        
def main():
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()
