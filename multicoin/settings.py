import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '24q_*&tn+5k_*6h6$nsccghwwb#8b%v4i)1h(wd08_02_-(czt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'True') == 'True'


ALLOWED_HOSTS = ['*']




JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Bulligon Signals Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Bulligon Signals",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Bulligon Signals",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "img/logo/logo-name.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "img/logo/icon-jazz.png",

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": "img/logo/logo-name-dark.png",

    # CSS classes that are applied to the logo above
    "site_logo_classes": ["logo"],

    "custom_css": "css/style.css",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "img/logo/icon-jazz.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome Admin!",

    # Copyright on the footer
    "copyright": "Bulligon Signals",
}


# Application definition

INSTALLED_APPS = [
            'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
     'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Users.apps.UsersConfig',
    'wallet.apps.WalletConfig',
    'company.apps.CompanyConfig',
    'myadmin.apps.MyadminConfig',
    'core.apps.CoreConfig',
    'crispy_forms',

    #3rd party
    'whitenoise.runserver_nostatic',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'multicoin.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates'), 
            os.path.join(BASE_DIR,'Users/templates'), 
            os.path.join(BASE_DIR,'templates/email'), 
            os.path.join(BASE_DIR,'templates/registration'),
            os.path.join(BASE_DIR,'templates/admin dashboard'),  
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'core.context.core',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'multicoin.wsgi.application'

AUTH_USER_MODEL = 'Users.User'
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


if DEBUG :
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            "OPTIONS": {
                "timeout": 30,
            }
        },
        "OPTIONS": {
        # ...
        "timeout": 30,
        # ...
    }
    }

else :
    # Replace the SQLite DATABASES configuration with PostgreSQL:
   

    DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost:5432/mydatabase')
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

"""
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
"""

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media")

STATICFILES_DIRS = [

os.path.join(BASE_DIR,"static")
]

SITE_NAME = "multicoin"

STATIC_ROOT = os.path.join(BASE_DIR,"asset")

STATIC_URL = '/static/'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


LOGIN_REDIRECT_URL = 'login-redirect'

LOGOUT_REDIRECT_URL = 'index'
STATIC_URL = '/static/'

#EMAIL FOR ZOHO
EMAIL_HOST  = "smtp.zoho.com"
EMAIL_PORT = "587"
#for other emails 
EMAIL_HOST_USER = "support@multicoin.ltd"
DEFAULT_FROM_EMAIL  = "support@multicoin.ltd"
EMAIL_HOST_PASSWORD = '#@Kyletech99'
EMAIL_HOST_USER_ALERT = "transaction@multicoin.ltd"
EMAIL_HOST_USER_SUPPORT = "support@multicoin.ltd"

#GODADDY and tawkto
#username : hmdzhamad3@gmail.com
#email :hmdzhamad3@gmail.com
#password : racpaxx44


EMAIL_USE_TLS = "True"

SITE_NAME = "multicoin LTD."
SITE_ADDRESS = "https://www.multicoin.ltd/"

FREE_PLAN_DURATION = 2  #in days
SUBSCRIPTION_DURATION = 365   #in days

DEFAULT_AUTO_FIELD='django.db.models.AutoField'