import re

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = 'registry_number'
    _sql_constraints = [
        ('vin_unique', 'UNIQUE(vin)', 'Another registration for this VIN Number already exists.')
    ]

    
    registry_number = fields.Char('Registry Number', copy=False, required=True, readonly=True, default='MRN0000')
    vin = fields.Char(string='VIN', required=True)
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    picture = fields.Image(string='Photograph')
    current_mileage = fields.Float(string='Current Mileage')
    license_plate = fields.Char(string='License Plate Number')
    certificate_title = fields.Binary(string='Certificate of Title')
    registry_date = fields.Date(string='Registration Date')

        
    @api.constrains('license_plate')
    def _check_license_plate_size(self):
        pattern = '^[A-Z]{1,3}\d{1,4}[A-Z]{0,2}$'
        for registry in self:
            if registry.license_plate:
                match = re.match(pattern, registry.license_plate)
                if not match:
                    raise ValidationError('Invalid License Plate')
                    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)