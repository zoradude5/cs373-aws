#!/lusr/bin/python

from util import *
import cgi

user = None

form = cgi.FieldStorage()
if 'name' in form:
    user = get_user(form['name'].value)
if user == None:
    user = get_user()


write_response('user.html', { 'user': user })
