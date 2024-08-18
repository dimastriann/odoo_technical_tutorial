# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OdooTutorial(models.Model):
    _name = 'odoo.tutorial'
    _description = 'Odoo Technical Tutorial'

    name = fields.Char(string='Name')
    total = fields.Integer(string='Total')
    description = fields.Text(string='Description')
    user_id = fields.Many2one(string='User', comodel_name='res.users')
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         for record in self:
    #             record.value2 = float(record.value) / 100


class OdooModelTransient(models.TransientModel):
    _name = 'odoo.tutorial.transient'
    _description = "Odoo Tutorial Transient"


class OdooModelAbstract(models.AbstractModel):
    _name = 'odoo.tutorial.abstract'
    _description = "Odoo Tutorial Abstract"


