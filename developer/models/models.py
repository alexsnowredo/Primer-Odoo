# -*- coding: utf-8 -*-

from odoo import models, fields


class developer(models.Model):
    _name = 'developer.developer'
    _description = 'developer.developer'

    name = fields.Char()
    Fecha_1 = fields.Date()
    Fecha_nacimiento = fields.Date()
