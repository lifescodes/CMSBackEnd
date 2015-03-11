"""
WSGI config for lifecode project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os
import sys
import site

#specification for domain and project name
domain = 'api.lifecode.loc'
project_name = 'lifecode'

# defining apache path, domain path on apache base, and project path within virtualenv
base_path = '/var/www/django/'
domain_path = os.path.join(base_path, domain)
project_path = os.path.join(domain_path, project_name)
env_path = os.path.join(domain_path,'env/')
activate_path = os.path.join(env_path,'bin/activate_this.py')
sitedir_path = os.path.join(env_path, 'local/lib/python2.7/site-packages/')

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir(sitedir_path)

# add base system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

# Add the app's directory to the PYTHONPATH
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lifecode.settings.base")

# add project, domain and apache path to system
sys.path.append(project_path)
sys.path.append(domain_path)
sys.path.append(base_path)

# Activate your virtual env
activate_env=os.path.expanduser(activate_path)
execfile(activate_env, dict(__file__=activate_path))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
