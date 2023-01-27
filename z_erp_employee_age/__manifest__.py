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
    'name': 'Employee Age with Details',
    'version': '14.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Human Resources',
    'description':
        """        
        This Module will helps to show employee age with details Age, Month and Days, based on the employee date of 
        birth, employee age will automatically displayed.
    """,
    'summary': 'This Module will helps to show employee age with details Age, Month and Days, based on the employee '
               'date of birth, employee age will automatically displayed.',
    'depends': ['hr'],
    'images': ['static/description/EA_Odoo_14_banner_new1.png'],
    'data': [
        'views/hr_employee.xml'
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
