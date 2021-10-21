# -*- coding: utf-8 -*-
{
    'name' : 'Products Warranty',
    'version' : '0.1',
    'summary': 'Products Warranty Software',
    'sequence': 10,
    'description': """Products Warranty Software""",
    'category': 'Productivity',
    'depends': [
        'product'
    ],
    'website': 'https://www.odoomates.tech',
    'data': [
        'data/data.xml',
        'views/phieubaohanh.xml',
        'views/sanpham.xml'
    ],
    'demo': [
        'demo/demo.xml'
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}