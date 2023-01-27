from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _competitor_count(self):
        for line in self:
            competitor_ids = self.env['competitor.price'].search([('competitor_id', '=', line.id)])
            line.competitor_price_count = len(competitor_ids)

    def competitor_price_button(self):
        self.ensure_one()
        return {
            'name': 'Competitor Price',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'competitor.price',
            'domain': [('competitor_id', '=', self.id)],
        }

    competitor_price_count = fields.Integer(string='Competitor Price', compute='_competitor_count')
    is_competitor = fields.Boolean('Is Competitor.?')
