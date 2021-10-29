# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class products__warranty(models.Model):
#     _name = 'products__warranty.products__warranty'
#     _description = 'products__warranty.products__warranty'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
