from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    name = fields.Char(string='Tên sản phẩm', required=True)
    date = fields.Datetime(string='Ngày nhận máy', required=True, default = lambda self: fields.Date.today())
    hang = fields.Selection([
          ('apple','Apple'),
          ('ss', 'SamSung'),
          ('vv', 'Vivo'),
          ('sm', 'Xiaomi'),
          ('Dell','Dell')
     ], required=True, default='apple')
    bh = fields.Boolean(string='Bảo hành', default=True)
    nsx = fields.Many2one('hang.sp', string="Nhà sản xuất")


