from odoo import fields,api,models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        res = super(StockPicking, self).button_validate()

        for move in self.move_line_ids:
            if move.product_id.detailed_type == "motorcycle":
                if not self.env['motorcycle.registry'].search([('vin', '=', move.lot_id.name)]):
                    self.env['motorcycle.registry'].create({
                        'sale_id': self.sale_id.id,
                        'vin': move.lot_id.name,
                    })

        return res