from odoo import models, fields, api, _


class VaccineCentre(models.Model):
    _name = 'hr.employee.vaccine.centre'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Vaccine Centre'
    _rec_name = 'name'

    name = fields.Char(string=_("Tên trung tâm"), required=1)
    contact_details = fields.Char(string=_("Địa chỉ"))
    other_info = fields.Text(string=_("Thông tin khác"))
