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
    'name': 'Employee Probation Notification',
    'version': '14.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Human Resources',
    'description':
        """
        This Module add below functionality into odoo

        1. This module helps you to add a Employee Date Of joining,Probation Months,Probation Completion Days.
        2. Once Employee Probation Completed automatically employee will get an email.

    """,
    'summary': 'Module For Employee Probation Notification',
    'depends': ['hr'],
    'images': ['static/description/EPN_Odoo_14_banner.png'],
    'data': [
        'data/cron_data.xml',
        'data/mail_data.xml',
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
