from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit='sale.order'

    is_new_customer = fields.Boolean( compute="_compute_is_new_customer", required=True, store = True)
    
    @api.depends("partner_id")
    def _compute_is_new_customer(self):
        self.is_new_customer = True
        for sale_order in self:
            partner_id = sale_order.partner_id
            if not self.partner_id:
                self.is_new_customer = False
            for other_sale_orders in (partner_id.sale_order_ids - self):
                for product in other_sale_orders.order_line:
                    if product.product_type == "motorcycle":
                        self.is_new_customer = False
        return
    
    def apply_motorcycle_discount(self):
        for sale_order in self:
            for product in sale_order.order_line:
                if product.product_type == "motorcycle":
                    discount = 2500
                    discount_percentage = discount / product.price_subtotal * 100
                    product.discount = discount_percentage