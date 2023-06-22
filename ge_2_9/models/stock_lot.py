from odoo import fields,api,models

class StockLot(models.Model):
    _inherit = 'stock.lot'
    
    registry_entry = fields.Many2one(comodel_name='motorcycle.registry', string='Motorcycle Registry', ondelete='cascade')

            