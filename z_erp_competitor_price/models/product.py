from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _competitor_count(self):
        for line in self:
            competitor_ids = self.env['competitor.price'].search([('product_id.product_tmpl_id', '=', line.id)])
            line.competitor_price_count = len(competitor_ids)

    def competitor_price_button(self):
        self.ensure_one()
        return {
            'name': 'Competitor Price',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'competitor.price',
            'domain': [('product_id.product_tmpl_id', '=', self.id)],
        }
    competitor_price_count = fields.Integer(string='Competitor Price', compute='_competitor_count')


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def _competitor_count(self):
        for line in self:
            competitor_ids = self.env['competitor.price'].search([('product_id', '=', line.id)])
            line.competitor_price_count = len(competitor_ids)

    def competitor_price_button(self):
        self.ensure_one()
        return {
            'name': 'Competitor Price',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'competitor.price',
            'domain': [('product_id', '=', self.id)],
        }

    competitor_price_count = fields.Integer(string='Competitor Price', compute='_competitor_count')
