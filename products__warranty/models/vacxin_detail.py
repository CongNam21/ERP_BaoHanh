from odoo import models, fields, _, api


class thongtin(models.Model):
    _name = 'vaccination.detail'
    _description = "Vaccination Details"

    employee_id = fields.Many2one('hr.employee')
    sequence = fields.Integer(string='Sequence', default=10)

    vaccine_id = fields.Many2one('hr.employee.vaccine.info', string=_("Vaccine"), ondelete='restrict')
    vaccination_centre_id = fields.Many2one('hr.employee.vaccine.centre', string=_("Trung tâm tiêm chủng"),
                                            ondelete='restrict')
    vaccine_dose = fields.Char(string=_("Liều lượng"))
    dose_date = fields.Date(string=_("Ngày tiêm"))
    vaccinated_country_id = fields.Many2one('res.country', string='Quốc gia')
    vaccine_certificate_ids = fields.Binary("vacince Image", attachment=True, help="Xác nhận tiêm vacine")