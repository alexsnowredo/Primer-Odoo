# -*- coding: utf-8 -*-
# from odoo import http


# class Developer(http.Controller):
#     @http.route('/developer/developer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/developer/developer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('developer.listing', {
#             'root': '/developer/developer',
#             'objects': http.request.env['developer.developer'].search([]),
#         })

#     @http.route('/developer/developer/objects/<model("developer.developer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('developer.object', {
#             'object': obj
#         })
