import os
import cgi
import wsgiref.handlers

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db


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
	
class Fdb(db.Model):
  tema_id = db.StringProperty()
  author = db.UserProperty()
  content = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now =True)
  
  
  
class Fdb_main(db.Model):
	id = db.IntegerProperty()
	author_tema = db.UserProperty()
	first_date = db.DateTimeProperty(auto_now_add = True)
	content = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now =True)
	amount_mess = db.IntegerProperty()
	author_post = db.UserProperty()

class MainPage(webapp.RequestHandler):
	def get(self):
		tems = db.GqlQuery("SELECT * FROM Fdb_main")
		

		user = users.get_current_user()
		if user:
			login = reg(self.request)
			
			template_values = {'username': login['un'],
								'url_out': login['lo'],
								'tems': tems}
			path = os.path.join(os.path.dirname(__file__), 'forum_templ.html')
			self.response.out.write(template.render(path, template_values))
		else:
			login = reg(self.request)
			template_values = {'url': login,
							   'tems': tems}
			path = os.path.join(os.path.dirname(__file__), 'forum_templ.html')
			self.response.out.write(template.render(path, template_values))
			
			
class ForumMesPage(webapp.RequestHandler):
	def get(self):
                str = ""
		ppp = self.request.get('id')
		mesengers = db.GqlQuery("SELECT * FROM Fdb WHERE tema_id = '%s' " % ppp)
		tems = db.GqlQuery ("SELECT * FROM Fdb_main WHERE id = :1", int(self.request.get('id')))
		for name_theme in tems:
                    str = name_theme.content
		user = users.get_current_user()
		if user:
			login = reg(self.request)
			template_values = {'mesengers': mesengers,
								'username': login['un'],
								'url_out': login['lo'],
								'mess_tema_id': ppp,
                                'theme_name': str 
								}
			path = os.path.join(os.path.dirname(__file__), 'forum_tema.html')
			self.response.out.write(template.render(path, template_values))
		else:
			login = reg(self.request)
			template_values = {'mesengers': mesengers,
								'url': login,
								'mess_tema_id': ppp,
								'theme_name': str 
								}
			path = os.path.join(os.path.dirname(__file__), 'forum_tema.html')
			self.response.out.write(template.render(path, template_values))

		
class Forum_mes(webapp.RequestHandler):
	def post(self):
		mess = Fdb()
		mess.tema_id = self.request.get('mess_id')
		mess.author = users.get_current_user()
		mess.content = self.request.get('coment')
		
		mess.put()
		
		tems = db.GqlQuery("SELECT * FROM Fdb_main WHERE id = :1 ", int(self.request.get('mess_id')))
		for tema in tems:
			tema.amount_mess = tema.amount_mess + 1
			tema.author_post = users.get_current_user()
			tema.date
			tema.put()
			
		login = reg(self.request)	
		template_values = { 'go_to_tema': '/forum_id?id='+self.request.get('mess_id'),
							'username': login['un'],
							'url_out': login['lo']
						  }
		path = os.path.join(os.path.dirname(__file__), 'forum_mess_otp.html')
		self.response.out.write(template.render(path, template_values))
			

class Forum_tema(webapp.RequestHandler):
	def post(self):
		tema = Fdb_main()
		tema.content = self.request.get('tema_cont')
		tema.amount_mess = 0
		tema.author_tema = users.get_current_user()
		tema.author_post = users.get_current_user()
		tema.put()
		last_key = tema.key()
		tema.id = last_key.id()
		tema.put()
		#self.redirect('/forum?id='+ '%s' % id)
		self.redirect('/forum')

		
application = webapp.WSGIApplication(
                                     [('/forum', MainPage),
                                      ('/forum_id', ForumMesPage),
									  ('/forum_send',Forum_mes),
									  ('/forum_tema_send', Forum_tema),
									  ],
                                     debug=True)


def main():
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()
