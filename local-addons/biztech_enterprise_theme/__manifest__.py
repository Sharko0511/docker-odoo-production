{
    'name': 'Enterprise Theme',
    'version': '16.0.1.0.1',
    'summary': 'Enterprise Theme',
    'license': 'AGPL-3',
    'author': 'Biztech Computer',
    'maintainer': 'Biztech Computer',
    'website': 'https://biztechbh.biz',
    'depends': [
        'web'
    ],
    'category': 'Branding',
    'description': """
           Odoo Enterprise Theme
    """,
    'assets': {
        'web._assets_primary_variables': [
            '/biztech_enterprise_theme/static/src/scss/primary_variables_custom.scss',
        ],
        'web.assets_common': [
            '/biztech_enterprise_theme/static/src/scss/fields_extra_custom.scss',
        ],
        'web._assets_secondary_variables': [
            '/biztech_enterprise_theme/static/src/scss/secondary_variables.scss',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': ['static/description/icon.png'],
    
}
