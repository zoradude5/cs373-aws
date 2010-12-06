#!/lusr/bin/python

from util import *
import cgitb,cgi
cgitb.enable()

form = cgi.FieldStorage()
action = form['action'].value

if action == 'login':
    redirect('index.cgi', login=form['name'].value)
elif action == 'logout':
    redirect('index.cgi', logout=True)
elif action == 'pet':
    new_pet(form['name'].value,form['type'].value)
    redirect('index.cgi')
elif action == 'like':
    like_pet(form['name'].value)
    redirect('index.cgi')
elif action == 'unlike':
    remove_pet(form['name'].value)
    redirect('index.cgi')
else:
    error()
