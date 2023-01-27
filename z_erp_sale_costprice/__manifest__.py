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
    'name': 'Sale Cost Price Restriction',
    'version': '14.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Sales',
    'description':
        """        
        This Module will helps to restrict the sales order confirmation below the product cost price.
    """,
    'summary': 'This Module will helps to restrict the sales order confirmation below the product cost price.',
    'depends': ['base','sale_management'],
    'images': ['static/description/cost_odoo_14.png'],
    'data': [],
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
