from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    name = fields.Char(compute='_compute_name', precompute=True)

    @api.depends('brand', 'make', 'model')
    def _compute_name(self):
        for record in self:
            if record.detailed_type == 'motorcycle':
                record.name = ' '.join([record.brand, record.make, record.model])
            else:
                record.name = record.name
