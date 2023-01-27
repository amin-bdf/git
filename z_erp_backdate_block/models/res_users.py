# -*- coding: utf-8 -*-
##############################################################################
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2022 Zone4Erp SSolutions (<zone4erp@gmail.com>).
#    For Module Support : zone4erp@gmail.com
##############################################################################
from odoo import api, fields, models, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    back_dated_days = fields.Integer('Back Dated Entry Days', default=0)
