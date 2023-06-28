from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    name = fields.Char(compute="_compute_name", store="True")

    @api.depends('make', 'model', 'year', 'detailed_type')
    def _compute_name(self):
        # just notice this information is available in motorcycle
        for record in self:
            if record.detailed_type == "motorcycle":
                # suppose the type is correct, use year, make, model to make the name
                record.name = str(record.year) + str(record.make) + str(record.model)
            else:
                # set the default name for it
                # I just copy the original version
                record.name = ""



        # def _get_next_serial(self, company, product):
        #     prod_tmpl_id = product.product_tmpl_id
        #     if prod_tmpl_id.detailed_type == 'motorcycle' and product.tracking != 'none':
        #         if prod_tmpl_id.make and prod_tmpl_id.model and prod_tmpl_id.year:
        #             vin_part = prod_tmpl_id.make + prod_tmpl_id.model + str(prod_tmpl_id.year)[-2:]
        #             return vin_part + self.env['ir.sequence'].next_by_code('stock.lot.serial')
        #     else:
        #         return super(StockLot, self)._get_next_serial(company, product)