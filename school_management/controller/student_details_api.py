
from odoo.http import Controller, request, route


class StudentDetailsAPI(Controller):

    @route('/student', type='http', auth='user', website=True)
    def get_student_details_data(self, **kwargs):
        students = request.env['student.information'].sudo().search([])
        values = {
            'students': students,
        }
        return request.render('school_management.portal_my_student_details', values)

    @route('/student/<int:student_id>', type='http', auth='user', website=True)
    def get_student_detail_data(self, student_id, **kwargs):
        student = request.env['student.information'].sudo().browse(student_id)
        if not student.exists():
            return request.not_found()
        values = {
            'student': student,
        }
        return request.render('school_management.portal_student_details', values)
