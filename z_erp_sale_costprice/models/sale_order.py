# -*- coding: utf-8 -*-
##############################################################################
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2022 Zone4Erp SSolutions (<zone4erp@gmail.com>).
#    For Module Support : zone4erp@gmail.com
##############################################################################
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for line in self:
            for sale_line in self.order_line:
                currency_value = round(sale_line.price_unit / line.currency_id.rate, 2)
                if currency_value < sale_line.product_id.standard_price:
                    raise UserError(_('Alert !! For %s unit price(%s) %s is lesser than the cost price(%s) %s . Please check and confirm..!') % (
                                        sale_line.product_id.name, sale_line.price_unit,line.currency_id.name,
                                    sale_line.product_id.standard_price,line.currency_id.name))
        return res
