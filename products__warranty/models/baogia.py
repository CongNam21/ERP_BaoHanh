# -*- coding: utf-8 -*-
from odoo import models, api, fields, _, exceptions
import datetime


class SaleCustomer(models.Model):
    _inherit = 'sale.order'
    _description = "Day la mot form bao gia sua ke thua"

    date = fields.Date(string='Ngày nhận máy', required=True, default=lambda self: fields.Date.today())
    datereturn = fields.Date(string='Ngày trả máy', required=True)
    lsp = fields.Many2one('product.category', string="Loại sản phẩm")
    receive = fields.Selection([
        ('dn', 'Đã Nhận'),
        ('cn', 'Chưa Nhận'),
    ], string="Tình trạng", required=True, default='cn')
    name_employee = fields.Many2one('hr.employee', string="Nhân viên")
    lydo = fields.Text(string='Lý do hư hỏng')
    image = fields.Binary(string='Hình ảnh')
    returns = fields.Boolean(string="Đã trả", required=False)
    lk_lines = fields.One2many('lk.lines', 'lk_id')
    service = fields.Selection([('home', 'Nhận máy tại nhà'), ('store', 'Nhận máy tại cửa hàng')], string='Dịch vụ',
                               required=True,
                               default='store')

    # product_id = fields.Many2many(comodel_name='product.product',
    #                                string="Linh kiện thay",
    #                                relation='product_rel',
    #                                column1='col_dt_id',
    #                                column2='col_product_id')

    class LKLines(models.Model):
        _name = "lk.lines"
        product_id = fields.Many2one('product.template', string="Tên linh kiện")
        product_qty = fields.Char(string="Số Lượng")
        ghichu = fields.Text(string='Ghi Chú')
        lk_id = fields.Many2one('sale.order')

