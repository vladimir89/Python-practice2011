import os
import cgi
import wsgiref.handlers

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

#TMPL_ROOT = os.path.join(os.path.dirname(__file__), 'main')

#def get_template(template_name):
  #return os.path.join(TMPL_ROOT, template_name)

def reg(request):
  user = users.get_current_user()
  if user:
    name = user.nickname()
    lurl_out = users.create_logout_url(request.uri)
    un_and_lo = {'un': name,
                 'lo': lurl_out}
    return un_and_lo
  else:
    lurl = users.create_login_url(request.uri)
    return lurl 

class MainPage(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), 'main.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), 'main.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values))

'''class Reg(webapp.RequestHandler):
  def get(self):
    lurl = users.create_login_url(self.request.uri)
    template_values = {'url': lurl}

    path = os.path.join(os.path.join(os.path.dirname(__file__), 'template'), 'url.html')
    self.response.out.write(template.render(path, template_values))'''
class ForumPage(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'forum_templ.html')
    self.response.out.write(template.render(path, None))

class ForumMesPage(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'forum_tema.html')
    self.response.out.write(template.render(path, None))


application = webapp.WSGIApplication(
                                     [('/.*', MainPage),
                                      
                                      #('/forum', ForumPage),
                                      #('/forum_id', ForumMesPage)],
                                      #('/url', Reg)],
                                       ],
                                     debug=True)

def main():
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()
