from odoo import models, fields, api, _


class VaccineInfo(models.Model):
    _name = 'hr.employee.vaccine.info'
    _description = 'Chi tiet vaxin'
    _rec_name = 'name'

    name = fields.Char(string=_("Tên vacine"), required=1)
    dose = fields.Integer(string=_("Liều"), default=1, help="Số liều")
    period = fields.Integer(string=_("Khoảng cách thời gian tiêm giữa các mũi"), default=30, help="Khoảng cách thời gian tiêm giữa các mũi")
    country_id = fields.Many2one('res.country', string='Country of Origin')
    vaccine_details = fields.Html(string=_("Chi tiết vacine"))