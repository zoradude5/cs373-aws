import os, aws_settings
from django.shortcuts import render_to_response
from Cookie import SimpleCookie
from django.http import HttpResponseRedirect
import cgitb,boto
cgitb.enable()

sdb = None

#page rendering

def write_response(path, dict):#, login=None):
    resp = render_to_response(path, dict)
    #if login != None:
    #    set_login_info(resp,login)
    print resp

def redirect(path, login=None, logout=False):
    resp = HttpResponseRedirect(path)
    if login != None:
        set_login_info(resp,login)
    if logout == True:
        remove_login_info(resp)
    if resp.cookies: print resp.cookies
    print resp

def error():
    print """Content-type: text/html

<html><body>
error
</body></html>"""

#session

def set_login_info(resp,name):
    resp.set_cookie('name',name, domain='cs.utexas.edu', path='/~carlos/')

def remove_login_info(resp):
    resp.delete_cookie('name', domain='cs.utexas.edu', path='/~carlos/')

def get_login():
    if 'HTTP_COOKIE' in os.environ:
        c = SimpleCookie(os.environ['HTTP_COOKIE'])
        if 'name' in c:
            return c['name'].value

#DB

def get_domain(name="aws"):
    global sdb
    if sdb == None:
        sdb = boto.connect_sdb(aws_settings.aws_settings['KEY'], aws_settings.aws_settings['SECRET'])
    return sdb.get_domain(name)

def get_user(user_name=None):
    domain = get_domain('aws_users')
    if user_name == None:
        user_name = get_login()

    user = domain.get_item(user_name)
    if user == None and user_name != None: # we have cookie info , but no user in db
        user = domain.new_item(user_name)
        user['name'] = user_name
        user.save()
    if user != None:
        if 'pets' not in user:
            user['pets'] = []
        if type(user['pets']) != type([]):
            user['pets'] = [user['pets']]
    return user

def get_pets_with_likes():
    pets={}
    for pet in get_domain():
        pets[pet.name] = pet
    user = get_user()
    if user != None:
        for like in user['pets']:
            if like in pets:
               pets[like]['liked'] = True
                
    return pets.values()

def remove_pet(name):
    user = get_user()
    while name in user['pets']:
        user['pets'].remove(name)
    user.save()

def new_pet(name, type):
    domain = get_domain()
    entry = domain.new_item(name)
    entry['name'] = name
    entry['type'] = type
    entry.save()
    like_pet(name)
        

def like_pet(name):
    user = get_user()
    if user != None:
        user['pets'].append(name)
        user.save()





