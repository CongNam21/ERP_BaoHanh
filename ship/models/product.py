# -*- coding: utf-8 -*-

from odoo import models, fields, api
#
#
class Ship(models.Model):
    _name = 'product.template'
    _description = 'ship hang'
    Color = fields.Char("Color")
    type = fields.Selection(
        [('hop', 'Hộp'), ('cai', 'Cái'), ('chiec', 'Chiếc'), ('may', 'Máy')], "Unit")
    Capacity = fields.Selection(
        [('32gb', '32GB'), ('64gb', '64GB'),('128gb', '128GB'), ('256gb', '256GB'),('512gb', '512GB')], "Capacity")
    amount = fields.Integer("Số Lượng")
    Insurance = fields.Char("Insurance")
    description = fields.Text()
    product = fields.Many2many('product.product', string="Sản phẩm")
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
