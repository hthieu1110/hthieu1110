from distutils.core import setup

setup(
    name = 'hthieu_family',
    version = '1.0',
    packages = ['family', 'family.templates', 'family.templates.family', 'family.templatetags', 'family.album',
                'family.photo', 'common', 'common.templates', 'common.templates.common', 'vendor',
                'vendor.debug_toolbar', 'vendor.debug_toolbar.management', 'vendor.debug_toolbar.management.commands',
                'vendor.debug_toolbar.panels', 'vendor.debug_toolbar.templatetags', 'vendor.debug_toolbar.toolbar',
                'vendor.debug_toolbar.utils', 'vendor.debug_toolbar.utils.compat', 'vendor.debug_toolbar.utils.sqlparse'
        , 'vendor.debug_toolbar.utils.sqlparse.engine', 'vendor.debug_toolbar.utils.tracking'],
    url = 'family.hthieu.com',
    license = 'MIT',
    author = 'hthieu1110',
    author_email = 'tronghieu.ha@gmail.com',
    description = 'My family album'
)
