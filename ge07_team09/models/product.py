from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit="product.template"
    
    name = fields.Char(string="Product Name", readonly=False, store=True, compute="_computeName", required=True, precompute=True)
    
    @api.depends("make", "model", "year")
    def _computeName(self):
        for record in self:
            if record.detailed_type == "motorcycle":
                record.name = f"{str(record.year)} {record.make} {record.model}"
            else:
                record.name = record.name
        