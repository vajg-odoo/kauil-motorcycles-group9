from odoo import api, fields, models

class StockLot(models.Model):
    _inherit = "stock.lot"
    
    @api.model
    def _get_next_serial(self, company, product):
        product_tmpl_id = product.product_tmpl_id
        if product_tmpl_id.detailed_type == "motorcycle" and product_tmpl_id.tracking != "none":
            if product_tmpl_id.make and product_tmpl_id.model and product_tmpl_id.year:
                vin_number = product_tmpl_id.make[ :2].upper() + product_tmpl_id.model + str(product_tmpl_id.year)[-2 :]
                return vin_number + self.env["ir.sequence"].next_by_code("stock.lot.serial")
        else:
            return super(StockLot, self)._get_next_serial(company, product)