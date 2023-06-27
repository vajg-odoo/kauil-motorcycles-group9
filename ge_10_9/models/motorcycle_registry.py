import re

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
        _inherit = 'motorcycle.registry'

        