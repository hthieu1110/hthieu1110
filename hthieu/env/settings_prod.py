DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hthieu',                      # Or path to database file if using sqlite3.
        'USER': 'hthieu_dev',                      # Not used with sqlite3.
        'PASSWORD': 'hthieu_dev',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/Users/hthieu1110/Sites/django_projects/hthieu/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/Users/hthieu1110/Sites/hthieu/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8rw5!#_qv6bg%@9ph@(wh0qbtnvsjz5yr=im!h_!7hz_i53!8('

