# -*- coding: utf-8 -*-
{
    'name' : 'Products Warranty',
    'version' : '0.1',
    'summary': 'Products Warranty Software',
    'sequence': 10,
    'description': """Products Warranty Software""",
    'category': 'Productivity',
    'depends': [
        'product',
        'sale',
        'crm',
        'hr',
        'stock'
    ],
    'website': 'https://www.odoomates.tech',
    'data': [
        'data/data.xml',
        'views/baogia.xml',
        'views/sanpham.xml',
        'views/kh.xml',
        'views/pbh.xml',
        'views/lsp.xml',
        'views/chuanhan.xml',
        'views/danhan.xml',
        'views/nhanvien.xml',
        'views/bt.xml',
        'views/hang.xml',
        'views/nhapkho.xml',
        'views/thongtintiem.xml',
        'views/trungtamvacxin.xml',
        'reports/report_template.xml',
        'reports/report.xml',
        'reports/report_pbh.xml',
        'reports/report_template_pbh.xml',
    ],
    'demo': [
        'demo/demo.xml'
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}