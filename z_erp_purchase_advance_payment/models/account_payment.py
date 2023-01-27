from odoo import models, fields, api, _


class account_payment(models.Model):
    _inherit = "account.payment"

    purchase_id = fields.Many2one('purchase.order','Purchase Order')
