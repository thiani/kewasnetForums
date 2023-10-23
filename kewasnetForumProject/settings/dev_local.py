# settings/dev_local.py

from .dev import *

# Add any local development-specific settings here

DEBUG = True  # Customize this setting for local development.

# Static Files Configuration
STATIC_URL = '/static/'  # URL prefix for static files
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # Path to the directory where collected static files will be stored
