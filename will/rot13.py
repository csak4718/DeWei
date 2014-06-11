# ROT13
import webapp2
import cgi

form="""
<form method="post">
	<b>Enter some text to ROT13:<b>
	<br>
	<textarea name="text" rows="5" cols="50">%(answer)s</textarea>
	
	<br>
	<input type="submit">
</form>
"""

def escape_html(s):
	return cgi.escape(s, quote = True)

def rot13(string):
	rot_string =""
	alphabets='abcdefghijklmnopqrstuvwxyz'
	up_alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	for j in range(0, len(string)):
		if string[j].isalpha():
			if string[j].islower():
				position = alphabets.find(string[j])
				new_position = (position+13)%26 # a @index 0 -> n @index 13
				rot_string += alphabets[new_position]
			else:
				position = up_alphabets.find(string[j])
				new_position = (position+13)%26
				rot_string += up_alphabets[new_position]
		else:
			rot_string += string[j]

	return rot_string

class rot13Handler(webapp2.RequestHandler):
	def write_form(self, answer=""):
		self.response.out.write(form % {"answer": answer})

	def get(self):
		self.write_form()

	def post(self):
		user_text = self.request.get('text')
		#print user_text
		self.write_form(escape_html(rot13(user_text)))


application = webapp2.WSGIApplication([('/unit2/rot13', rot13Handler)], debug=True)
