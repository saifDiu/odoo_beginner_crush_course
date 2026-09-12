{
    'name': 'School Management',
    'category': 'School Management',
    'summary': 'School Management',
    'depends': ['base','portal'],
    'data': [
        'security/ir.model.access.csv',
        'security/sceurity.xml',
        'views/student_information.xml',
        'views/class_information.xml',
        'report/student_report.xml',
        'wizard/draft_reason.xml',
        'views/student_details_website_template.xml'
    ],
    'version': '19.0.0.1',
    'installable': True,
    'application': True,
}
