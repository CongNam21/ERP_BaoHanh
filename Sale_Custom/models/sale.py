# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleCustomer(models.Model):
    _inherit = 'sale.order'
    _description = "Day la mot form bao gia sua ke thua"
    sale_test=fields.Char(String='test',required=True,default="mo ta")
    service = fields.Selection([('home', 'Sửa chữa tại nhà'), ('store', 'Sửa chữa tại cửa hàng')],string='Dịch vụ', required=True,
                              default='store')
    insurance = fields.Selection([('still', 'Còn bảo hành'), ('over', 'Hết bảo hành')], string='Chế độ',
                               required=True,
                               default='still')