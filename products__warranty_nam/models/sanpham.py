from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    name = fields.Char(string='Tên sản phẩm', required=True)
    date = fields.Datetime(string='Ngày bán', required=True)
    hang = fields.Selection([
          ('apple','Apple'),
          ('ss', 'SamSung'),
          ('vv', 'Vivo'),
          ('sm', 'Xiaomi'),
          ('Dell','Dell')
     ], required=True, default='apple')
    bh = fields.Boolean(string='Còn bảo hành', default=True)


