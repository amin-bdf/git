# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2022 Zone4Erp SSolutions (<zone4erp@gmail.com>).
#
#    For Module Support : zone4erp@gmail.com
#
##############################################################################

{
    'name': 'Accounts Backlog Posting Restrictions',
    'version': '14.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Accounting',
    'description':
        """        
        This Module will helps to restrict accounts backlog entry posting based on the user level configuration.
    """,
    'summary': 'This Module will helps to restrict accounts backlog entry posting '
               'based on the user level configuration.',
    'depends': ['account'],
    'images': ['static/description/bb_Odoo_14_banner.png'],
    'data': [
        'views/res_users_view.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'author': 'Zone4Erp Solutions',
    'website': 'zone4erp@gmail.com',
    'maintainer': 'Zone4Erp Solutions',
    'support': 'zone4erp@gmail.com',
    'price': 5,
    'currency': 'USD',

}
