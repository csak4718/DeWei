# Sign up page
import webapp2
import cgi
import re

form="""
<form method="post">
    <b>Signup</b>
    <br>
    <br>

    <label> Username
    	<input type="text" name="username" value="%(username)s"><span style="color: red">%(username_error)s</span>
    </label>
    <br>

    <label> Password
    	<input type="password" name="password" value="%(password)s"><span style="color: red">%(password_error)s</span>
    </label>
    <br>

    <label> Verify Password
    	<input type="password" name="verify" value="%(verify)s"><span style="color: red">%(verify_error)s</span>
    </label>
    <br>

    <label> Email (optional)
    	<input type="text" name="email" value="%(email)s"><span style="color: red">%(email_error)s</span>
    </label>
    <br>

    <input type="submit">
</form>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
	return USER_RE.match(username)

PASSWORD_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
	return PASSWORD_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
	return EMAIL_RE.match(email)

def escape_html(s):
	return cgi.escape(s, quote = True)

class SignupHandler(webapp2.RequestHandler):
	def write_form(self, username_error="", password_error="", verify_error="", email_error="", 
						username="", password="", verify="", email=""):
		self.response.out.write(form % {"username_error": username_error,
										"password_error": password_error,
										"verify_error": verify_error,
										"email_error": email_error,
										"username": escape_html(username),
										"password": escape_html(password),
										"verify": escape_html(verify),
										"email": escape_html(email)})
	def get(self):
		self.write_form()
	def post(self):
		user_username = self.request.get('username')
		user_password = self.request.get('password')
		user_verify = self.request.get('verify')
		user_email = self.request.get('email')

		username = valid_username(user_username)
		password = valid_password(user_password)
		compare = (user_password == user_verify)
		
		if user_email == '':
			# user didn't enter email address
			
			if not (username and password and compare):
				if username:
					username_error=""
				else:
					username_error="That's not a valid username"

				if password:
					if compare:
						password_error=""
						verify_error=""
					else:
						password_error=""
						verify_error="Your passwords didn't match."
				else:
					password_error="That wasn't a valid password."
					verify_error=""

				self.write_form(username_error, password_error, verify_error, "", user_username, "", "", user_email)
			else:
				self.redirect("/unit2/welcome?username=" + user_username)
			
		else:
			email = valid_email(user_email)

			if not (username and password and compare and email):
				if username:
					username_error=""
				else:
					username_error="That's not a valid username"
				if email:
					email_error=""
				else:
					email_error="That's not a valid email"

				if password:
					if compare:
						password_error=""
						verify_error=""
					else:
						password_error=""
						verify_error="Your passwords didn't match."
				else:
					password_error="That wasn't a valid password."
					verify_error=""

				self.write_form(username_error, password_error, verify_error, email_error, user_username, "", "", user_email)

			else:
				self.redirect("/unit2/welcome?username=" + user_username)
				

class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Welcome, "+ self.request.get('username') + '!')


application = webapp2.WSGIApplication([('/unit2/signup', SignupHandler), 
									("/unit2/welcome", WelcomeHandler),], debug=True)
