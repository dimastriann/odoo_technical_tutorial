from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    custom_barcode = fields.Char()
