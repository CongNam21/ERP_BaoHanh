# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Phieubaohanh(models.Model):
     _name = 'pbh.sp'
     _description = 'Phiếu bảo hành'

     name = fields.Char(string='Mã BH', required=True, copy=False, readonly=True,
                             default=lambda seft: _('New'))
     namecus = fields.Many2one('res.partner', string="Khách hàng")
     product = fields.Many2one('product.template', string="Sản phẩm")
     phieusua = fields.Many2one('sale.order', string="Mã phiếu sửa")
     sup = fields.Many2one('hang.sp', string="Nhà sản xuất")
     date = fields.Datetime(string='Ngày kích hoạt', required=True)
     loaisp = fields.Many2one('product.category',string="Loại sản phẩm")
     active = fields.Boolean(string = "Đã kích hoạt", required = True)
     gc = fields.Text(string= 'Ghi chú')
     img = fields.Binary(string='Hình ảnh')
     # product_id = fields.Many2many(comodel_name='product.product',
     #                                string="Linh kiện thay",
     #                                relation='product_rel',
     #                                column1='col_dt_id',
     #                                column2='col_product_id')
     lkbh_lines = fields.One2many('lkbh.lines', 'lkbh_id')

     class LKLines(models.Model):
         _name = "lkbh.lines"
         productlk_id = fields.Many2one('product.template', string="Tên linh kiện")
         productlk_qty = fields.Char(string="Số Lượng")
         exp = fields.Char(string='Hạn bảo hành', required=True)
         ghichu = fields.Text(string='Ghi Chú')

         lkbh_id = fields.Many2one('pbh.sp')

     @api.model
     def create(self, vals):
         if vals.get('name', ('New')) == ('New'):
             vals['name'] = self.env['ir.sequence'].next_by_code('pbh.sp') or _('New')
         res = super(Phieubaohanh, self).create(vals)
         return res

