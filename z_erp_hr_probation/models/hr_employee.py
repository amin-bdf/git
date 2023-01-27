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


class hr_employee(models.Model):
    _inherit = 'hr.employee'

    joining_date = fields.Date(string="Date of Joining", track_visibility='onchange')
    employee_status = fields.Selection([
        ('trainee', 'Trainee'),
        ('probation', 'Probation'),
        ('permanent', 'Permanent'),
        ('notice_period', 'Notice Period'),
        ('temporary', 'Temporary')
    ], 'Employee Status', track_visibility='onchange', default='probation')
    date_of_permanency = fields.Date(string="Date of Permanency", track_visibility='onchange')
    probation_months = fields.Integer('Probation Month', default='6', track_visibility='onchange')

    @api.onchange('joining_date', 'probation_months')
    def onchange_date_of_joining(self):
        for line in self:
            if line.employee_status == 'probation':
                if line.joining_date and line.probation_months:
                    line.date_of_permanency = line.joining_date + relativedelta(months=+line.probation_months)

    @api.model
    def send_probation_notification(self):
        today = fields.Date.context_today(self)
        probation_employees = self.env['hr.employee'].search([('date_of_permanency', '!=', False),
                                                              ('employee_status', '=', 'probation'),
                                                              ('work_email', '!=', False),
                                                              ('date_of_permanency', '=', today)])
        if probation_employees:
            for employee in probation_employees:
                ir_model_data = self.env['ir.model.data']
                ctx = dict()
                try:
                    template_id = ir_model_data.get_object_reference('z_erp_hr_probation',
                                                                     'employee_probation_notification_template')[1]
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
                    'subject': 'Successful Completion of Probation Period',
                })
                mail_id = self.env['mail.template'].browse(template_id).with_context(ctx).send_mail(employee.id,
                                                                                                    force_send=True)
                employee.employee_status = 'permanent'


