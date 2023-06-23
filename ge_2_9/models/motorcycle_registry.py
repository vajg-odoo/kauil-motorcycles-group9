from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _inherit = "motorcycle.registry"
    _sql_constraints = [
        ('vin_unique', 'unique(vin)', 'VIN must be unique!'),
    ]

    lot_ids = fields.One2many(comodel_name="stock.lot", inverse_name="registry_number")
    lot_id = fields.Many2one(comodel_name="stock.lot", compute="compute_lot", inverse="lot_inverse")
    sale_id = fields.Char(String="Sale Id")

    @api.constrains('lot_id')
    def _check_lot_ids_singular(self):
        if self.lot_id:
            raise ValidationError('Odoopsie! Only one order is allowed per registry entry.')

    @api.depends('lot_ids')
    def compute_lot(self):
        for registry in self: 
            if len(registry.lot_ids) > 0:
                registry.lot_id = registry.lot_ids[0]

    def lot_inverse(self):
        for registry in self: 
            registry.lot_ids = registry.lot_id