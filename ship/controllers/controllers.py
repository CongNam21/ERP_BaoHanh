# -*- coding: utf-8 -*-
# from odoo import http


# class Ship(http.Controller):
#     @http.route('/ship/ship/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ship/ship/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ship.listing', {
#             'root': '/ship/ship',
#             'objects': http.request.env['ship.ship'].search([]),
#         })

#     @http.route('/ship/ship/objects/<model("ship.ship"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ship.object', {
#             'object': obj
#         })
