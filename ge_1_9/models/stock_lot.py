from odoo import fields,api,models

class StockLot(models.Model):
    _inherit = 'stock.lot'
    
    @api.model
    def _get_next_serial(self, company, product):
        if product.product_tmpl_id.detailed_type == 'motorcycle' and product.tracking != "none":
            if product.product_tmpl_id.make and product.product_tmpl_id.model and product.product_tmpl_id.year:
                # Using make,model,year but sidenote motorcycle_registry uses brand,make,model 
                vin_str = str(product.product_tmpl_id.make) + str(product.product_tmpl_id.model) + str(product.product_tmpl_id.year)
                vin_str += str(self.env['ir.sequence'].next_by_code('stock.lot.serial'))
                return vin_str
        else:
            return super(StockLot, self)._get_next_serial(company, product)

            