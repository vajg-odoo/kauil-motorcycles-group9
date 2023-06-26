from odoo import api, fields, models
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    warehouse_id = fields.Many2one(required = True, store = True, copy = True, compute = '_compute_warehouse_id', readonly=True)
    
    @api.depends("partner_shipping_id")
    def _compute_warehouse_id(self):
        warehouses = self.env['stock.warehouse'].search([]).filtered(lambda r: r.code != "WH")
        for sale_order in self:
            customer_address = self._compute_geolocations(sale_order.partner_shipping_id)
            closest_warehouse = sorted(warehouses, key = lambda wh: self._compute_distance_to_customer(wh, customer_address))[0]
            sale_order.warehouse_id = closest_warehouse
            
    def _compute_distance_to_customer(self, warehouse, customer_location):
        warehouse_location = self._compute_geolocations(warehouse.partner_id)
        distance_to_customer = geodesic(warehouse_location, customer_location).miles
        
        return distance_to_customer
        
    
    def _compute_geolocations(self, res_partner):
        geolocator = Nominatim(user_agent="http")
        geolocation =  geolocator.geocode(res_partner.contact_address_complete)
        return geolocation.latitude, geolocation.longitude
        