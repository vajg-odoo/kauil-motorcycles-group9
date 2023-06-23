from odoo import api, fields, models

class StockLot(models.Model): 
    _inherit = "stock.lot"

    registry_number = fields.Many2one(comodel_name="motorcycle.registry", compute="_compute_registry_number", ondelete="cascade", store=True)
    
    @api.depends('name')
    def _compute_registry_number(self):
        for lot in self:
            matched_registry = self.env['motorcycle.registry'].search([('vin', '=', lot.name)], limit=1)
            if matched_registry:
                lot.registry_number = matched_registry
            else:
                lot.registry_number = False