# -*- coding: utf-8 -*-
from odoo import models, fields


class ManagementStaff(models.Model):
    _inherit = 'hr.employee'
    _description = "Day la mot form quan ly nhan vien ke thua"
    sale_test=fields.Char(String='test',required=True,default="mo ta")
    language = fields.Char(string='Ngôn ngữ',required=True, default="Nhập vào các loại ngôn ngữ có thể sử dụng trong công việc")
    english = fields.Selection([('1', 'Beginner'), ('2', 'High Beginner'), ('3', 'Low Intermediate')
                                   , ('4', 'Intermediate'), ('5', 'High Intermediate'), ('6', 'Low Advanced')
                                , ('7', 'Advanced')], string='Trình độ tiếng anh',
                               required=True,
                               default='1')
    iden=fields.Char(string='Số CMND/CCCD',required=True)
    email=fields.Char(string='email cá nhân',required=True)
    certifi = fields.Char(string='Chứng chỉ khác', required=True,
                           default="Nhập vào các chứng chỉ khác nếu có")