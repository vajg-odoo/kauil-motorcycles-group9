from odoo import api, fields, models

class StockLot(models.Model): 
    _inherit = "stock.lot"

    def _get_next_serial(self, company, product):
        prod_tmpl_id = product.product_tmpl_id
        if prod_tmpl_id.detailed_type == 'motorcycle' and product.tracking != 'none':
            if prod_tmpl_id.make and prod_tmpl_id.model and prod_tmpl_id.year:
                vin_part = prod_tmpl_id.make + prod_tmpl_id.model + str(prod_tmpl_id.year)[-2:]
                return vin_part + self.env['ir.sequence'].next_by_code('stock.lot.serial')
        else:
            return super(StockLot, self)._get_next_serial(company, product)