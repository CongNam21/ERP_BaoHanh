# -*- coding: utf-8 -*-

from odoo import models, fields, api
#
#
class Ship(models.Model):
    _name = 'ship.ship'
    _description = 'ship hang'

    name = fields.Char("Tên Sản Phẩm")
    type = fields.Selection(
        [('hop', 'Hộp'), ('chai', 'Chai'), ('goi', 'Gói'), ('lo', 'Lọ')], "Đơn Vị")
    amount = fields.Integer("Số Lượng")
    person = fields.Char("Họ Tên Người Nhận")
    description = fields.Text()
    address = fields.Text("Địa Chỉ")
    phone = fields.Char("Số điện thoại")
    product = fields.Many2many('product.product', string="Sản phẩm")
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
