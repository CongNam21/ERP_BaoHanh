
from odoo import models, fields, api, _


class HrEmployeeInherit(models.AbstractModel):
    _inherit = 'hr.employee.base'

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
