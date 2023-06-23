from odoo import fields,api,models
from odoo.exceptions import ValidationError
class StockLot(models.Model):
    _inherit = 'stock.lot'
    
    registry_id = fields.One2many(comodel_name='motorcycle.registry', inverse_name='lot_id')

    @api.constrains('registry_id')
    def _check_registry_id(self):
        for lot in self:
            if len(lot.registry_id) > 1:
                raise ValidationError('Lot can only have one registry id')
            

