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
import datetime


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    age = fields.Integer(string="Age", compute='_compute_employee_age')
    age_details = fields.Char(compute='_compute_employee_age')

    @api.depends("birthday")
    def _compute_employee_age(self):
        for rec in self:
            if rec.birthday:
                rec.age = relativedelta(datetime.date.today(), rec.birthday).years
                currentDate = datetime.date.today()
                dob = datetime.date(rec.birthday.year, rec.birthday.month, rec.birthday.day)
                years = ((currentDate - dob).total_seconds() / (365.242 * 24 * 3600))
                yearsInt = int(years)
                months = (years - yearsInt) * 12
                monthsInt = int(months)
                days = (months - monthsInt) * (365.242 / 12)
                daysInt = int(days)
                rec.age_details = ('You are {0} years, {1} months, {2} days old.'.format(yearsInt, monthsInt, daysInt))
            else:
                rec.age = 0
                rec.age_details = ''
