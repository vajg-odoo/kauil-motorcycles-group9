from odoo import api, fields, models

class MotorcycleRegistry(models.Model):
    _inherit = 'motorcycle.registry'

    lot_ids = fields.One2many(comodel_name='stock.lot', inverse_name='registry_entry', string='Lots')