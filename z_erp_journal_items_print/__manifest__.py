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
    'name': 'Journal Items Report in PDF and XLS',
    'version': '14.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Accounting',
    'description':
        """        
        This Module will helps to print the selected journal items in PDF and Xls.
    """,
    'summary': 'This Module will helps to print the selected journal items in PDF and Xls.',
    'depends': ['account','web'],
    'images': ['static/description/JI_14.png'],
    'data': [
        'security/ir.model.access.csv',
        'report/journal_items_print.xml',
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
    'price': 9.5,
    'currency': 'EUR',

}
