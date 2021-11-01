# -*- coding: utf-8 -*-
from odoo import models, api, fields, _, exceptions
import datetime
import odoo.addons.decimal_precision as dp


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
    ], string="Loại sản phẩm", required=True, default='Dt')
    receive = fields.Selection([
        ('dn', 'Đã Nhận'),
        ('cn', 'Chưa Nhận'),
    ], string="Tình trạng", required=True, default='cn')
    name_employee = fields.Many2one('crm.team', string="Nhân viên")
    lydo = fields.Text(string='Lý do hư hỏng')
    image = fields.Binary(string='Images')
    bp = fields.Text(string='Bộ phận cần thay')

    amount_discount = fields.Monetary(string='Discount', store=True, readonly=True, compute='_amount_all',
                                      digits=dp.get_precision('Account'), track_visibility='always')

    def _check_dates(self):
        today_date = datetime.date.today()
        for SaleCustomer in self:
            if SaleCustomer.date:
                date = fields.Datetime.to_datetime(SaleCustomer.date).date()
                check = str(int((today_date - date).days / 365))
                if check < 0: SaleCustomer.date = "Ngày phải lớn hơn ngày hiện tại"
            else:
                SaleCustomer.date = ""

    @api.depends('order_line.price_total')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = amount_tax = amount_discount = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
                amount_discount += (line.product_uom_qty * line.price_unit * line.discount) / 100
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_discount': amount_discount,
                'amount_total': amount_untaxed + amount_tax,
            })

