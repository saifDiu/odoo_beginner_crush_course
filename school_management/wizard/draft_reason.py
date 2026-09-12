from odoo import api, fields, models, tools, _


class ResetDraftWizard(models.TransientModel):
    _name = 'wizard.reset.draft'

    student_id = fields.Many2one('student.information', string='Student')
    reason = fields.Char(string='Reason')

    def button_draft(self):
        self.student_id.write({
            'status': 'draft',
        })
        self.student_id.message_post(
            body=f'Reset Reason for student - {self.reason}',
            subtype_xmlid='mail.mt_note',
        )
