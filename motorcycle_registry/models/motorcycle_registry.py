from odoo import api, fields, models


class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = 'registry_number'
    
    registry_number = fields.Char('Registry Number', required=True)
    vin = fields.Char(string='VIN', required=True)
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    picture = fields.Image(string='Photograph')
    current_mileage = fields.Float(string='Current Mileage')
    license_plate = fields.Char(string='License Plate Number')
    certificate_title = fields.Binary(string='Certificate of Title')
    registry_date = fields.Date(string='Registration Date')