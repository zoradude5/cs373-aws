
from aws_sensitive import *
import sys
sys.path.append('/u/carlos/pylib/lib/python2.6')


from django.conf import settings
settings.configure(DEBUG=True, TEMPLATE_DEBUG=True,
    TEMPLATE_DIRS=('/u/carlos/public_html/aws/html',))

aws_settings = { 'KEY': 'AKIAISQYCMLGVBLS5BVQ',
	'SECRET': SECRET}
