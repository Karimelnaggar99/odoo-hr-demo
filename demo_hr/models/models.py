# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class demo_hr(models.Model):
#     _name = 'demo_hr.demo_hr'
#     _description = 'demo_hr.demo_hr'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
