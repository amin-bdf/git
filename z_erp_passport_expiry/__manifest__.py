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
    'name': 'Passport Expiry Notification',
    'version': '14.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Human Resources',
    'description':
        """
        This module will helps to manage the passport information of the employee and the expiry notification of the passport based on
            the expiry date and notification days configurations..!

    """,
    'summary': 'Module For Employee Passport Expiry Notification',
    'depends': ['hr','base'],
    'images': ['static/description/PEP_14.png'],
    'data': [
        'data/cron_data.xml',
        'data/mail_data.xml',
        'views/res_config.xml',
        'views/employee_view.xml'
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
    'currency': 'USD',

}
