# -*- coding: utf-8 -*-
# from odoo import http


# class DemoHr(http.Controller):
#     @http.route('/demo_hr/demo_hr', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_hr/demo_hr/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_hr.listing', {
#             'root': '/demo_hr/demo_hr',
#             'objects': http.request.env['demo_hr.demo_hr'].search([]),
#         })

#     @http.route('/demo_hr/demo_hr/objects/<model("demo_hr.demo_hr"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_hr.object', {
#             'object': obj
#         })
