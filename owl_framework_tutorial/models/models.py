# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class owl_framework_tutorial(models.Model):
#     _name = 'owl_framework_tutorial.owl_framework_tutorial'
#     _description = 'owl_framework_tutorial.owl_framework_tutorial'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

