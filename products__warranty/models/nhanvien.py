from odoo import _, models, fields, api
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _inherit = "hr.employee"

    job = fields.Selection([
        ('one', 'Sửa máy'),
        ('two', 'Vệ sinh máy'),
        ('three', 'Bán hàng'),
        ('four', 'Tư vấn'),
        ('five', 'Kiểm tra máy'),
        ("six", "Thay linh kiện")], string='Công việc', required=True, default='one')
    x_date_start = fields.Date("Ngày bắt đầu làm việc", required=True)
    language = fields.Char(string='Ngôn ngữ', required=True,
                           default="Nhập vào các loại ngôn ngữ có thể sử dụng trong công việc")
    english = fields.Selection([('1', 'Beginner'), ('2', 'High Beginner'), ('3', 'Low Intermediate')
                                   , ('4', 'Intermediate'), ('5', 'High Intermediate'), ('6', 'Low Advanced')
                                   , ('7', 'Advanced')], string='Trình độ tiếng anh',
                               required=True,
                               default='1')
    iden = fields.Char(string='Số CMND/CCCD', required=True)
    email = fields.Char(string='Email cá nhân', required=True)
    certifi = fields.Char(string='Chứng chỉ khác', required=True,
                          default="Nhập vào các chứng chỉ khác nếu có")





