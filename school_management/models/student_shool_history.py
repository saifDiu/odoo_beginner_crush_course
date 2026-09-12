from odoo import api, fields, models

class OtherSchool(models.Model):
    _name = 'others.school'
    _description = 'Other School'

    name = fields.Char(string='Name', required=True)


class StudentSchoolHistory(models.Model):
    _name = 'student.school.history'
    _description = 'Student School History'

    student_id = fields.Many2one('student.information')
    other_school_id = fields.Many2one('others.school', string='Other School', required=True)
    passing_year = fields.Char(string='Passing Year', required=True)
    class_name = fields.Char(string='Class', required=True)
