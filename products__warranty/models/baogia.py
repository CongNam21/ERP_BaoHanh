# -*- coding: utf-8 -*-
from odoo import models, api, fields,_, exceptions
import datetime


class SaleCustomer(models.Model):
    _inherit = 'sale.order'
    _description = "Day la mot form bao gia sua ke thua"


    name = fields.Char(string='Mã BH', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    namecus = fields.Many2one('res.partner', string="Khách hàng")
    product = fields.Many2many('product.template', string="Sản phẩm")
    date = fields.Date(string='Ngày nhận máy', required=True)
    datereturn = fields.Date(string='Ngày trả máy', required=True)
    sp = fields.Selection([
        ('Dt', 'Điện Thoại'),
        ('lap', 'LapTop'),
        ('mt', 'Máy tính bảng')
    ],string="Loại sản phẩm", required=True, default='Dt')
    receive = fields.Selection([
        ('dn', 'Đã Nhận'),
        ('cn', 'Chưa Nhận'),
    ], string="Tình trạng", required=True, default='cn')
    name_employee = fields.Many2one('crm.team', string="Nhân viên")
    lydo = fields.Text(string='Lý do hư hỏng')
    image = fields.Binary(string='Images')
    bp = fields.Text(string='Bộ phận cần thay')


