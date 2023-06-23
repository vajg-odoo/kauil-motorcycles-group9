from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit = "stock.picking"

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