# -*- coding: utf-8 -*-
##############################################################################
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2022 Zone4Erp SSolutions (<zone4erp@gmail.com>).
#    For Module Support : zone4erp@gmail.com
##############################################################################
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError,UserError
from datetime import datetime, timedelta, date


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        res = super(AccountMove, self).action_post()
        for invoice in self:
            back_date_allowed = self.env.user.back_dated_days
            if back_date_allowed > 0:
                if invoice.invoice_date:
                    back_date = date.today() - timedelta(days=back_date_allowed)
                    if invoice.invoice_date < back_date:
                        raise UserError(_("Alert !! You are not allowed to post back dated entry...!"))
                if invoice.date:
                    back_date = date.today() - timedelta(days=back_date_allowed)
                    if invoice.date < back_date:
                        raise UserError(_("Alert !! You are not allowed to post back dated entry...!"))
            else:
                if invoice.invoice_date:
                    back_date = date.today()
                    if invoice.invoice_date != back_date:
                        raise UserError(_("Alert !! You are not allowed to post back dated entry...!"))
                if invoice.date:
                    back_date = date.today()
                    if invoice.date != back_date:
                        raise UserError(_("Alert !! You are not allowed to post back dated entry...!"))
        return res
