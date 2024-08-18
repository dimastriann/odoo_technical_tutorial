# -*- coding: utf-8 -*-
# from odoo import http


# class OdooTutorial(http.Controller):
#     @http.route('/odoo_tutorial/odoo_tutorial', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_tutorial/odoo_tutorial/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_tutorial.listing', {
#             'root': '/odoo_tutorial/odoo_tutorial',
#             'objects': http.request.env['odoo_tutorial.odoo_tutorial'].search([]),
#         })

#     @http.route('/odoo_tutorial/odoo_tutorial/objects/<model("odoo_tutorial.odoo_tutorial"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_tutorial.object', {
#             'object': obj
#         })

