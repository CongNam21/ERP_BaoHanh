# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Loaispbh(models.Model):
    _name = "loaisp"
    _description = "loai san pham"

    name = fields.Char('Tên loại sản phẩm', required=True)
    description = fields.Text('Mô tả')
    #year = fields.Date('', required=False)
    soluong = fields.Integer('Số lượng sản phẩm')
    sp_image = fields.Binary("Loại sản phẩm", attachment=True, help="loai san pham")
    owner_id = fields.Many2one('hr.employee', string='Nhân Viên')
    thoigianbh = fields.Selection([
        ('1', '6 tháng'),
        ('2', '12 tháng'),
        ('3', '36 tháng')], string='Thời gian bảo hành', default='1')
    product_ids = fields.Many2many(comodel_name='product.product',
                                string="Danh sách sản phẩm",
                                relation='product_rel',
                                column1='col_dt_id',
                                column2='col_product_id')
    brands_ids = fields.One2many('my_module', 'danhsachbrand_id', string="Hãng")


class Child(models.Model):
    _name = 'my_module'

    danhsachbrand_id = fields.Many2one('res.company', ondelete='cascade', string="Hãng sản xuất")


