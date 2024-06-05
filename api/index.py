import os
import sys
from django.core.wsgi import get_wsgi_application

# Menambahkan direktori cyroom ke PYTHONPATH
current_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.join(current_path, '../cyroom')
sys.path.append(project_path)

# Mengatur variabel environment DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cyroom.settings')

# Mendapatkan WSGI application
application = get_wsgi_application()
