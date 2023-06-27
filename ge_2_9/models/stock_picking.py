from odoo import fields,api,models

class StockPicking(models.Model):

    _inherit = 'stock.picking' # or do we just use the type instead

    # suppose this function being called.
        # we need to grab the records with xml id as 	stock.stock_location_customers



        # first, get the records within self that have stock.stock_location_customers
        # within all these records, I will try to get the field call
        # move_line_nosuggest_ids since it is the one that might map to Detials Operations

        # and within the list it returns,

        # I check if product.type is motorcycle, if it is, create a motorcycle record 

    def button_validate(self):
        res = super(StockPicking, self).button_validate()

        if self.location_dest_id == self.env.ref("stock.stock_location_customers"):
            for move in self.move_line_ids:
                print(move)
                if (move.product_id.product_tmpl_id.detailed_type == 'motorcycle'):
                    if not self.env['motorcycle.registry'].search([('vin', '=', move.lot_id.name)]):
                        self.env['motorcycle.registry'].create({
                            'sale_id': self.origin,
                            'vin': move.lot_id.name,
                        })
        return res
        

