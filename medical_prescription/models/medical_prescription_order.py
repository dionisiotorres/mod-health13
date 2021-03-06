# Copyright 2008 Luis Falcon <lfalcon@gnusolidario.org>
# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>).
# Copyright 2020 LabViv.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import fields, models, api


class MedicalPrescriptionOrder(models.Model):
    _name = 'medical.prescription.order'
    _description = 'Medical Prescription Order'

    @api.model
    def _get_default_name(self):
        return self.env['ir.sequence'].get('medical.prescription.order')

    name = fields.Char(required=True, default=_get_default_name)
    patient_id = fields.Many2one(
        comodel_name='medical.patient', string='Patient', required=True)
    physician_id = fields.Many2one(
        comodel_name='medical.practitioner', string='Physician', required=True)
    partner_id = fields.Many2one(
        comodel_name='res.partner', string='Pharmacy')
    prescription_order_line_ids = fields.One2many(
        comodel_name='medical.prescription.order.line',
        inverse_name='prescription_order_id', string='Prescription Order Line')
    notes = fields.Text()
    is_pregnant = fields.Boolean()
    is_verified = fields.Boolean()
    date_prescription = fields.Datetime(default=fields.Datetime.now())
