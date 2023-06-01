from odoo import api, fields, models


class MotorcycleRegister(models.Model):
    _name = 'motorcycle.register'
    _description = 'Motorcycle Register'
    
    register_number = fields.Char('Register Number', required=True)
    vin = fields.Char(string='VIN', required=True)
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    picture = fields.Image(string='Photograph')
    current_mileage = fields.Float(string='Current Mileage')
    license_plate = fields.Char(string='License Plate Number')
    certificate_title = fields.Binary(string='Certificate of Title')
    register_date = fields.Date(string='Registration Date')