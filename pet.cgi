#!/lusr/bin/python

from util import *
import cgi

form = cgi.FieldStorage()
name = form['name'].value
domain = get_domain('aws_users')
users = domain.select('select name from aws_users where pets="%s"' % name)

write_response('pet.html', { 'name': name, 'users': users })
