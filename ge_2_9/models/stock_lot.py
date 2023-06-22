from odoo import fields,api,models

class StockLot(models.Model):
    _inherit = 'stock.lot'

    # adding the Many2one field to it

    registry_id = fields.Many2one(comodel_name='motorcycle.registry', ondelete='restrict', string='Motorcyle Registry')

