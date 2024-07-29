# -*- coding: utf-8 -*-
#############################################################################

{
    "name": "My Custom Theme",
    "description": """Minimalist and elegant backend theme for Odoo 16, Backend Theme, Theme""",
    "summary": "My Custom Theme V16 is an attractive theme for backend",
    "category": "Themes/Backend",
    "version": "16.0.1.0.0",
    'author': 'Quang',
    'company': 'Quang',
    'maintainer': 'Quang',
    'website': "",
    "depends": ['base', 'web', 'mail'],
    "data": [
        'security/ir.model.access.csv',
        'views/icons.xml',
        'views/layout.xml',
        'views/theme.xml',
        'views/assets.xml',
        'data/theme_data.xml',
    ],
    'assets': {
        'web.assets_backend': {
            '/my_custom_theme/static/src/scss/theme.scss',
            '/my_custom_theme/static/src/js/systray.js',
            '/my_custom_theme/static/src/js/load.js',
            # '/my_custom_theme/static/src/js/chrome/sidebar_menu.js',
            '/my_custom_theme/static/src/xml/systray.xml',
            # '/my_custom_theme/static/src/xml/top_bar.xml',
        },
        'web.assets_frontend': {
            '/my_custom_theme/static/src/scss/login.scss',
            '/my_custom_theme/static/src/scss/login.scss',
        },
    },
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.png',
    ],
    'license': 'LGPL-3',
    # 'pre_init_hook': 'test_pre_init_hook',
    # 'post_init_hook': 'test_post_init_hook',
    'installable': True,
    'application': False,
    'auto_install': False,
}
