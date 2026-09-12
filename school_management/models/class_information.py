from odoo import api, fields, models


class ClassInformation(models.Model):
    _name = 'class.information'

    name = fields.Char(string="Name")
    class_teacher_id = fields.Many2one('res.partner',string="Teacher",required=True)
    number_of_seat = fields.Integer(string="Number of Seat",required=True)