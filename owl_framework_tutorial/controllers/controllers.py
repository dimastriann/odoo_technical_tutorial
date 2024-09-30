# -*- coding: utf-8 -*-
# from odoo import http


# class OwlFrameworkTutorial(http.Controller):
#     @http.route('/owl_framework_tutorial/owl_framework_tutorial', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/owl_framework_tutorial/owl_framework_tutorial/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('owl_framework_tutorial.listing', {
#             'root': '/owl_framework_tutorial/owl_framework_tutorial',
#             'objects': http.request.env['owl_framework_tutorial.owl_framework_tutorial'].search([]),
#         })

#     @http.route('/owl_framework_tutorial/owl_framework_tutorial/objects/<model("owl_framework_tutorial.owl_framework_tutorial"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('owl_framework_tutorial.object', {
#             'object': obj
#         })

