# -*- coding: utf-8 -*-
# from odoo import http


# class ProductsWarranty(http.Controller):
#     @http.route('/products__warranty/products__warranty/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/products__warranty/products__warranty/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('products__warranty.listing', {
#             'root': '/products__warranty/products__warranty',
#             'objects': http.request.env['products__warranty.products__warranty'].search([]),
#         })

#     @http.route('/products__warranty/products__warranty/objects/<model("products__warranty.products__warranty"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('products__warranty.object', {
#             'object': obj
#         })
