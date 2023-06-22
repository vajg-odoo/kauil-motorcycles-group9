from odoo import fields,api,models

class MotorcycleRegistry(models.Model):
    _inherit = 'motorcycle.registry'

    # adding the one2many field
    # adding contrain on stock_ids, so it only allow one record to exist
    stock_ids = fields.One2many(comodel_name='stock.lot', ondelete='restrict', inverse_name = 'registry_id')

    # for here, we grab 'stock_ids' and using it to compute our result and show it to users
    stock_id = fields.Many2one(comodel_name='stock.lot', ondelete='restrict', compute="")


    @api.constrains('stock_ids')
    def _one_stock_ids(self):
        # adding logic that only allow one stock_ids exist
        # so user can not create one more
    

    @api.depends('vin')
    def _compute_from_stock_ids(self):
        



