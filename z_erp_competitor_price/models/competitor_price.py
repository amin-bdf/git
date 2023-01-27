from odoo import models, fields, api, _


class CompetitorPriceSource(models.Model):
    _name = 'competitor.price.source'
    _description = 'Competitor Price Source'

    name = fields.Char('Name',required=1)


class CompetitorPrice(models.Model):
    _name = 'competitor.price'
    _description = 'Competitor Price'

    @api.model
    def _get_user_currency(self):
        currency_id = self.env['res.users'].browse(self._uid).company_id.currency_id
        return currency_id or self._get_euro()

    name = fields.Char('Name')
    date = fields.Date('Date',default=fields.Date.context_today)
    competitor_id = fields.Many2one('res.partner', 'Competitor',domain="[('is_competitor', '=', True)]")
    source_id = fields.Many2one('competitor.price.source','Source')
    product_id = fields.Many2one('product.product', 'Product')
    uom_id = fields.Many2one('uom.uom', string='Unit of Measure',related='product_id.uom_id')
    price = fields.Float('Amount')
    note = fields.Text('Notes')
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company.id)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, default=lambda self: self._get_user_currency())

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code(
                'competitor.price.seq') or 'New'
        result = super(CompetitorPrice, self).create(vals)
        return result
