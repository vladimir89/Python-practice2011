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

class History(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), 'history.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), 'history.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values))  

class Contact(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), 'contact.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), 'contact.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 
	  
class Teachers(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), 'teachers.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), 'teachers.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 

  
  
class Applicants(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), 'applicants.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), 'applicants.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 
	
class Course1(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), '1course.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), '1course.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 
	
class Course2(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), '2course.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), '2course.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 
	
class Course3(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), '3course.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), '3course.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 
	
class Course4(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), '4course.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), '4course.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 

class Bachelors(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), 'bachelors.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), 'bachelors.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 
	
class Masters(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), 'masters.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), 'masters.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 
	
class Ip(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), 'ip.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), 'ip.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 
	
class Simplex(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), 'simplex.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), 'simplex.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 
	
class Translate(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), 'translate.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), 'translate.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 
	
class Slu(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), 'slu.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), 'slu.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 
	
class Video(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), 'video.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), 'video.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 
	
	
class Games(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      login = reg(self.request)
      template_values = {'username': login['un'],
                         'url_out': login['lo']}
      #path = get_template('main.html')
      path = os.path.join(os.path.dirname(__file__), 'games.html')
      self.response.out.write(template.render(path, template_values))
    else:
      login = reg(self.request)
      template_values = {'url': login}
      path = os.path.join(os.path.dirname(__file__), 'games.html')
      #path = get_template('main.html')
      self.response.out.write(template.render(path, template_values)) 
	
application = webapp.WSGIApplication(
                                     [('/history', History),
                                      ('/contact', Contact),
									  ('/teachers', Teachers),
									  ('/applicants', Applicants),
									  ('/1course', Course1),
									  ('/2course', Course2),
									  ('/3course', Course3),
									  ('/4course', Course4),
									  ('/bachelors', Bachelors),
									  ('/masters', Masters),
									  ('/ip', Ip),
									  ('/simplex', Simplex),
									  ('/translate', Translate),
									  ('/slu', Slu),
									  ('/video', Video),
									  ('/games', Games),
                                      #('/forum', ForumPage),
                                      #('/forum_id', ForumMesPage)],
                                      #('/url', Reg)],
                                       ],
                                     debug=True)

def main():
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()
