from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class StudentInformation(models.Model):
    _name = 'student.information'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Student Record'

    name = fields.Char(string='Name', required=True, tracking=True)
    roll_number = fields.Char(string='Roll Number', required=True, tracking=True)
    phone_number = fields.Char(string='Phone Number', required=True, tracking=True)
    email = fields.Char(string='Email')
    father_name = fields.Char(string='Father Name', required=True)
    mother_name = fields.Char(string='Mother Name')
    birth_certificate = fields.Char(string='Birth Certificate', tracking=True)
    address = fields.Char(string='Address', tracking=True)

    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    ], default='draft', string='Status', tracking=True)

    previous_record_ids = fields.One2many('student.school.history', 'student_id')
    image = fields.Binary(string='Image')
    student_documents_ids = fields.Many2many('ir.attachment', string='Attachments')
    student_notes = fields.Html(string='Notes')
    number_of_documents = fields.Integer(string='Number of Documents', compute='_get_number_of_documents')
    class_id = fields.Many2one('class.information', string='Class', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', tracking=True)

    @api.depends('student_documents_ids')
    def _get_number_of_documents(self):
        for record in self:
            record.number_of_documents = len(record.student_documents_ids.ids)

    def confirm_student(self):
        """
         Works fine for single record. Multiple, self (1,2,3).confirm_student()
        """
        for record in self:
            if record.status == 'draft':
                record.status = 'confirmed'

    def reset_student(self):
        for record in self:
            return {
                "name": 'Reset Reason',
                "type": "ir.actions.act_window",
                "target": "new",
                "views": [[False, "form"]],
                "res_model": "wizard.reset.draft",
                "context": {'default_student_id': record.id},
            }

    @api.constrains('phone_number')
    def _verify_phone_number(self):
        for student in self:
            existing_student = self.env['student.information'].search(
                [('phone_number', '=', student.phone_number), ('id', '!=', student.id)])
            if existing_student:
                raise ValidationError(_('Student with this phone number already exists.'))

    # def create(self, vals):
    #     res = super(StudentInformation, self).create(vals)
    #     existing_student = self.env['student.information'].search([('phone_number','=',vals['phone_number']),('id','!=',res.id)])
    #     if existing_student:
    #         raise ValidationError(_('Student with this phone number already exists.'))
    #     return res
