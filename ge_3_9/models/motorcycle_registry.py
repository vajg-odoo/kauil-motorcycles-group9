from odoo import api, fields, models


class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _inherit = ['motorcycle.registry', 'portal.mixin']


    def action_view_registry(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': self.get_portal_url(),
        }
    
    def _compute_access_url(self):
        super(MotorcycleRegistry, self)._compute_access_url()
        for motorcycle in self:
            motorcycle.access_url = f'/my/registries/{motorcycle.id}'


