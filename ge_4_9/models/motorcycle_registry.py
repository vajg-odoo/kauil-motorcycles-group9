from odoo import api, fields, models

class MotorcycleRegistry(models.Model):
    _inherit = 'motorcycle.registry'

    repair_order_ids = fields.One2many(comodel_name='repair.order', inverse_name='registry_id', string='Repair Orders')

    def action_view_repair_order(self):
        return {
            'name': 'Repair Orders',
            'type': 'ir.actions.act_window',
            'res_model': 'repair.order',
            'view_mode': 'tree,form',
            'domain': [('registry_id', '=', self.id)],
        }