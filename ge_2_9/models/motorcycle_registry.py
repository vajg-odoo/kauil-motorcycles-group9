from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _inherit = 'motorcycle.registry'

    lot_id = fields.Many2one(comodel_name='stock.lot', string='Lot', compute='_compute_registry_id', store=True) 
    sale_id = fields.Many2one(comodel_name='sale.order', string='Sale Order', store=True)

    owner_id = fields.Many2one(comodel_name='res.partner',related='sale_id.partner_id')

    @api.depends('vin')
    def _compute_registry_id(self):
        for registry in self:
            matched_lot = self.env['stock.lot'].search([('name', '=', registry.vin)], limit=1)
            if matched_lot:
                registry.lot_id = matched_lot.id
            else:
                registry.lot_id = False

    