# Copyright 2016 LasLabs Inc.
# Copyright 2020 LabViv.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import api, models


class MedicalMedicament(models.Model):
    _inherit = 'medical.medicament'

    @api.model
    def create(self, vals):
        if not vals.get('type'):
            vals['type'] = 'product'
        return super(MedicalMedicament, self).create(vals)
