from odoo import models, fields, api, _


class Hang(models.Model):
    _name = 'hang.sp'
    _description = 'Hãng sản xuất'

    name = fields.Char(string='Tên nhà sản xuất', required=True)
    loaisanp = fields.Many2one('product.category', string="Loại sản phẩm")
    ghic = fields.Text(string='Ghi chú')
