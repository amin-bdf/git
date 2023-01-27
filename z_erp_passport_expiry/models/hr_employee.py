# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2022 Zone4Erp SSolutions (<zone4erp@gmail.com>).
#
#    For Module Support : zone4erp@gmail.com
#
##############################################################################

from odoo import api, fields, models, _
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError, UserError
from odoo import api, fields, models,_
from datetime import datetime, date
from odoo.fields import Date
from odoo import http, tools
from odoo.exceptions import ValidationError, UserError
from dateutil.relativedelta import relativedelta



class Company(models.Model):
    _inherit = "res.company"

    passport_expiry_notify_days = fields.Integer(string="Passport Expiry Notification before", default=10)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    passport_expiry_notify_days = fields.Integer(string="Passport Expiry Notification before",
                                                 related='company_id.passport_expiry_notify_days', readonly=False)


class hr_employee(models.Model):
    _inherit = 'hr.employee'

    passport_issue = fields.Date(string="Passport Issue Date", track_visibility='onchange')
    passport_expiry = fields.Date(string="Passport Expiry Date", track_visibility='onchange')
    passport_issue_place = fields.Char(string="Passport Issue Place", track_visibility='onchange')

    @api.onchange('passport_issue', 'passport_expiry')
    def onchange_passport_date(self):
        for line in self:
            if line.passport_issue and line.passport_expiry:
                if line.passport_issue > line.passport_expiry:
                    raise ValidationError(_('Passport Expiry date should be greater than passport Issue Date..!'))

    @api.model
    def send_passport_expiry_notification(self):
        today = fields.Date.context_today(self)

        passport_having_employees = self.env['hr.employee'].search([('passport_expiry', '!=', False)])
        if passport_having_employees:
            for employee in passport_having_employees:
                diff_days = (employee.passport_expiry - today).days
                if diff_days < employee.company_id.passport_expiry_notify_days:
                    ir_model_data = self.env['ir.model.data']
                    ctx = dict()
                    try:
                        template_id = ir_model_data.get_object_reference('z_erp_passport_expiry',
                                                                         'employee_passport_expiry_notification_template')[1]
                    except ValueError:
                        template_id = False
                    current_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
                    current_url += '/web#id=%d&view_type=form&model=%s' % (employee.id, employee._name)

                    ctx.update({
                        'default_model': 'hr.employee',
                        'default_res_id': employee.id,
                        'default_use_template': bool(template_id),
                        'default_template_id': template_id,
                        'default_composition_mode': 'comment',
                        'email_to': employee.work_email,
                        'email_cc': employee.parent_id.work_email,
                        'email_to_name': employee.name,
                        'url': current_url,
                        'company': employee.company_id.name,
                        'subject': 'Passport Expiry Notification',
                    })
                    mail_id = self.env['mail.template'].browse(template_id).with_context(ctx).send_mail(employee.id,
                                                                                                        force_send=True)


