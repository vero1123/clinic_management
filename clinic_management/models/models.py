# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools import date_utils, float_compare, float_round, float_is_zero

class ResPatient(models.Model):
    _name = 'res.patient'
    _description = 'res.patient'

    partner_id = fields.Many2one('res.partner',string='patient name')
    age = fields.Integer(string='Age')
    gender = fields.Char(string='gender')
    bloodtype = fields.Char(string='Blood Type')
    height = fields.Float(string='Height')
    weight = fields.Float(string='Weight')
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')

class ResClinic(models.Model):
    _name ='res.clinic'
    _description = 'res.clinic'

    clinic_name = fields.Char(string='clinic name')
    clinic_no = fields.Integer(string='clinic no')
    doctor_ids = fields.Many2many('res.users',string='doctor')


class patientappointment(models.Model):
    _name = 'patient.appointment'
    _description = 'patient.appointment'
    _rec_name = 'seq_request'

    name =fields.Char(string='name')
    seq_request = fields.Char(default=lambda self: ('New'), readonly=1, string='order reference', index=True)

    patient_id =fields.Many2one('res.patient',string='patient name')
    clinic_id =fields.Many2one('res.clinic',string='clinic number')
    doctor_ids =fields.Many2many('res.users',string='doctors name')
    date =fields.Date(string='Date',default=datetime.today())
    notes =fields.Text(string='Notes')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
        ('delete', 'Delete') ], string='Status', readonly=True, default='draft')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_cancel(self):
        self.state = 'cancel'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def unlink(self):
        if self.state == 'confirm':
            raise UserError('You Cannot Delete  as it is in Confirm State.')
        return super(patientappointment, self).unlink()

    # @api.onchange('clinic_id')
    # def onchange_clinic_id(self):
    #    res = {}
    #    res['domain']={'doctor_id':[('clinic_id','=',self.clinic_id.id)]}
    #    print(res)
    #    return res

    @api.onchange('clinic_id')
    def onchange_set_domain_doctor_id(self):
        # for rec in self:
            clinic_object = self.env['res.clinic'].search([['clinic_name', '=' , self.clinic_id.clinic_name]])
            print(clinic_object.doctor_ids)
            self.doctor_ids = clinic_object.doctor_ids.ids

        # doctor_list = []
        #
        # for data in clinic_object:
        #     doctor_list.appeand(data.clinic_id.id)
        # print(doctor_list)
        # res = {}
        # res['domain'] = {'doctor_id':[('id','in',doctor_list)]}
        # print(res)


        # this is method to create sequence number
    @api.model
    def create(self, vals):
        Sequence = self.env['ir.sequence']
        vals['seq_request'] = Sequence.next_by_code('patient.appointment')
        return super(patientappointment, self).create(vals)
        print(super(patientappointment, self).create(vals))