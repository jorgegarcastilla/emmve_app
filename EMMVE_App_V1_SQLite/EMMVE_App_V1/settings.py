"""
Django settings for EMMVE_App_V1 project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#mpb6_*-hw)i0vk%^4u^5bklq*+n1-lwgnknie27ndvqq=y)j8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'registration.apps.RegistrationConfig',#J.G.CASTILLA : DEBE REGISTRARSE LA PRIMERA YA QUE ESTAMOS SOBREESCRIBIENDO TEMPLATES POR DEFECTO DE DJANGO
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'poblaciones.apps.poblacionesConfig',
    'aulas.apps.aulasConfig',
    'core.apps.CoreConfig',
    'redesSociales.apps.redesSocialesConfig',
    'noticias.apps.NoticiasConfig',
    'asignaturas.apps.AsignaturasConfig',
    'docentes.apps.DocentesConfig',
    'disponibilidades.apps.DisponibilidadesConfig',
    'alumnos.apps.AlumnosConfig',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'EMMVE_App_V1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'registration.processors.context_dict', #J.G.CASTILLA : PARA DEFINIR OBJETOS GLOBALES RELATIVOS AL USUARIO
                'redesSociales.processors.context_dict', #J.G.CASTILLA : PARA DEFINIR OBJETOS GLOBALES RELATIVOS A LAS REDES SOCIALES.
            ],
        },
    },
]

WSGI_APPLICATION = 'EMMVE_App_V1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

#J.G.CASTILLA : CONFIGURACIÓN DE LA BASE DE DATOS CON POSTGRESQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

#J.G.CASTILLA : CONFIGURACIÓN DEL SERVIDOR WEB EN ESPAÑOL
LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#J.G.CASTILLA : RUTAS DE LOS FICHEROS MEDIA PARA EL SERVIDOR WEB DJANGO EN MODO DEBUG.
MEDIA_URL = '/media/' # Los ficheros los almacenará en la carpeta raiz del proyecto con nombre "media"
MEDIA_ROOT = os.path.join(BASE_DIR,"media") # Se le indica la ruta completa de la carpeta "media"

#J.G.CASTILLA : CONFIGURACIÓN DE UN BUZON DE MAIL VIRTUAL BASADO EN FICHEROS PARA PROBAR EN MODO DEBUG.
#Emails
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = os.path.join(BASE_DIR,"sent_emails")
    # EMAIL_HOST = 'smtp.mailtrap.io'
    # EMAIL_HOST_USER = '8ee23761e7542a'
    # EMAIL_HOST_PASSWORD = '545fa5d3f4ab60'
    # EMAIL_PORT = '2525'
else:
    # Aqui utilizar email real para producción 
    pass

# J.G.CASTILLA : RUTAS PARA EL CONTROL DE ACCESOS
LOGOUT_REDIRECT_URL = 'home'

# J.G.CASTILLA : PERSONALIZACIÓN DE CKEDITOR
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
        ]
    }
}