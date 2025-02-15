"""
WSGI config for Soil_Analysis_and_Crop_Reccommendation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Soil_Analysis_and_Crop_Reccommendation.settings')

application = get_wsgi_application()
