#!/lusr/bin/python

from util import *


write_response('index.html', { 'entries': get_pets_with_likes(), 'users': get_domain('aws_users') , 'user_name': get_login() })
