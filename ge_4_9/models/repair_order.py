from odoo import api, fields, models

class RepairOrder(models.Model):
    _inherit = 'repair.order'

    registry_id = fields.Many2one(comodel_name='motorcycle.registry', string='Motorcycle Registry', compute='_compute_registry_id', store=True)

    vin = fields.Char(related='lot_id.name', string='VIN', store=True)
    mileage = fields.Float(related='registry_id.current_mileage', string='Mileage', store=True)

    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer', related='registry_id.owner_id', store=True)
    sale_order_id = fields.Many2one(comodel_name='sale.order', string='Sale Order', related='registry_id.sale_id', store=True)
    # product_id = fields.Many2one(comodel_name='product.product', string='Product', related='registry_id.product_id', store=True)

    @api.depends('lot_id')
    def _compute_registry_id(self):
        for repair in self:
            entry = self.env['motorcycle.registry'].search([('vin', '=', repair.lot_id.name)], limit=1)
            if entry:
                repair.registry_id = entry.id
            else:
                repair.registry_id = False
    