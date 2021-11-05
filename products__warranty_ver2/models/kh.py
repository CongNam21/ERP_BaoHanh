# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class partner(models.Model):
    _inherit = "res.partner"
    _description = "Extend res.partner model"

    # channel_ids = fields.Many2many('mail.channel','mail_channel_profile_partner','partner_id','channel_id', copy=False)

    timebh = fields.Date(string='Warranty period', required=False)
    typekh = fields.Selection([
        ('khmoi', 'New customer'),
        ('khcu', 'Old Customer')], string='Type', default='khmoi')
    chinhsachbh = fields.Selection([
        ('bhtd', 'Lifetime warranty for the company'),
        ('bhtc', 'Custom warranty for retail customers')], string='Warranty Policy')
