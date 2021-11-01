# -*- coding: utf-8 -*-
{
    'name': 'Products Warranty',
    'version': '0.1',
    'summary': 'Products Warranty Software',
    'sequence': 10,
    'description': """Products Warranty Software""",
    'category': 'Productivity',
    'depends': [
        'sale',
        'crm'
    ],
    'website': 'https://www.odoomates.tech',
    'data': [
        'data/data.xml',
        'views/baogia.xml',
        'views/sanpham.xml',
        'views/kh.xml',
        'views/chuanhan.xml',
        'views/danhan.xml',
        'reports/report_template.xml',
        'reports/report.xml',
    ],
    'demo': [
        'demo/demo.xml'
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
