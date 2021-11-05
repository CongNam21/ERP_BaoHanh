from odoo import api, fields, models
from datetime import datetime

class Import(models.Model):
    _inherit = "stock.picking"
    _description = ""

    nhomsp = fields.Many2one('product.category', string="Nhóm sản phẩm")
    ngaytao_phieu = fields.Date(string='Ngày tạo phiếu ', default=datetime.today(), readonly="1")

