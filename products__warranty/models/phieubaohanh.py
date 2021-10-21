# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Phieubaohanh(models.Model):
     _name = 'phieubaohanh.sp'
     _description = 'Phiếu bảo hành'

     name = fields.Char(string='Mã BH', required=True, copy=False, readonly=True,
                             default=lambda seft: _('New'))
     namecus = fields.Many2one('res.partner', string="Khách hàng")
     product = fields.Many2many('product.template', string="Sản phẩm")
     supplier = fields.Char(string='Name Supplier', required=True)
     date = fields.Datetime(string='Ngày bảo hành', required=True)
     datereturn = fields.Datetime(string='Ngày trả máy', required=True)
     price = fields.Float(string='Phí sửa', required=True)
     tags = fields.Selection([
          ('Dt','Điện Thoại'),
          ('lap', 'LapTop'),
          ('mt','Máy tính bảng')
     ], required=True, default='Dt')
     receive = fields.Boolean(string = "Đã Nhận", required = True)
     name_employee = fields.Many2one('crm.team', string="Nhân viên")
     note = fields.Text(string= 'Description')

     @api.model
     def create(self, vals):
         if vals.get('name', ('New')) == ('New'):
             vals['name'] = self.env['ir.sequence'].next_by_code('phieubaohanh.sp') or _('New')
         res = super(Phieubaohanh, self).create(vals)
         return res


     def get_total(self, cr, uid, ids, field_name, arg, context):
         res = {}
         total = 0
         curat = self.browse(cr, uid, ids, context=context)
         for cura in curat:
             total += cura.curativedigit
             res[cura.id] = total
             return res

