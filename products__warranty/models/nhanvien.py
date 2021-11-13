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
    email = fields.Char(string='email cá nhân', required=True)
    certifi = fields.Char(string='Chứng chỉ khác', required=True,
                          default="Nhập vào các chứng chỉ khác nếu có")

    employee_vaccination_ids = fields.One2many('vaccination.detail', 'employee_id', string=_("Thông tin vacine"))
    vaccine_dose_count = fields.Integer(string=_("Liều"), compute='_compute_vaccination_status')
    vaccine_note = fields.Text(string='Thông tin khác')
    vaccination_status = fields.Selection(
        selection=[('no', 'Chưa tiêm'), ('full', 'Đã tiêm')],
        compute='_compute_vaccination_status', string="Vaccination Status")

    @api.depends('employee_vaccination_ids.vaccine_id')
    def _compute_vaccination_status(self):
        for employee in self:
            if len(employee.employee_vaccination_ids) == 0:
                employee.vaccination_status = 'no'
            else:
                employee.vaccination_status = 'full'
            employee.vaccine_dose_count = len(employee.employee_vaccination_ids)




