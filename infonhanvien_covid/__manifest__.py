

{
    'name': 'Thông tin vacxin nhân viên',
    'version': '14.0.1',
    'summary': """Employee Covid Vaxin""",
    'description': "thông tin vaxin",
    'category': 'Generic Modules/Human Resources',
    'depends': ['hr'],
    'data': [
        'views/infovacine_view.xml',
        'views/trungtamvacine_view.xml',
        'views/hr_employee.xml',
        'views/menu.xml'
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
