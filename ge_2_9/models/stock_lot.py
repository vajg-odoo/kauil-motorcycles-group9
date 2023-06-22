from odoo import fields,api,models

class StockLot(models.Model):
    _inherit = 'stock.lot'

    # adding the Many2one field to it

    registry_id = fields.Many2one(comodel_name='motorcycle.registry', ondelete='restrict', string='Motorcyle Registry')
    
    # Adding a unique constraint on the registry_id field
    _sql_constraints = [
        ('registry_id_unique', 'UNIQUE(registry_id)', _('A motorcycle registry can only be linked to one stock lot.')),
    ]
