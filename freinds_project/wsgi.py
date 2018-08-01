import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freinds_project.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'ConfigClass')

from configurations.wsgi import get_wsgi_application


application = get_wsgi_application()
