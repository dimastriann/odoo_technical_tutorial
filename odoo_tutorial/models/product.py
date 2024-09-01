from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    custom_barcode = fields.Char()

    def generate_custom_barcode(self):
        return self.write({'custom_barcode': self.custom_barcode})
