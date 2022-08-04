# -*- coding: utf-8 -*-
# from odoo import http


# class ClinicManagement(http.Controller):
#     @http.route('/clinic_management/clinic_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clinic_management/clinic_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clinic_management.listing', {
#             'root': '/clinic_management/clinic_management',
#             'objects': http.request.env['clinic_management.clinic_management'].search([]),
#         })

#     @http.route('/clinic_management/clinic_management/objects/<model("clinic_management.clinic_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clinic_management.object', {
#             'object': obj
#         })
