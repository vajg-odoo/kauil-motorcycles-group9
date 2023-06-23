from odoo import fields,api,models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _inherit = 'motorcycle.registry'

    # adding the one2many field
    # adding contrain on stock_ids, so it only allow one record to exist
    stock_ids = fields.One2many(comodel_name='stock.lot', inverse_name = 'registry_id', 
                                string='Stock Ids' # Distinct label)

    # for here, we grab 'stock_ids' and using it to compute our result and show it to users
    stock_id = fields.Many2one(comodel_name='stock.lot', ondelete='restrict', 
                               compute="_compute_from_stock_ids", string='Primary Stock' # Distinct label)


    @api.constrains('stock_ids')
    def _one_stock_ids(self):   
        self.ensure_one()   
        # adding logic that only allow one stock_ids exist
        # so user can not create one more
        for registry_entry in self:
            if registry_entry.stock_ids:
                if len(self.stock_ids) >= 2:
                    raise ValidationError('Odoopsie! Only one stock number for one motorcycle model')

    @api.depends('stock_ids')
    def _compute_from_stock_ids(self):
        # only return the top 1 elem
        for registry_entry in self:
            if registry_entry.stock_ids:
                self.stock_id = self.stock_ids[:1]
                return self.stock_ids[:1]
            




