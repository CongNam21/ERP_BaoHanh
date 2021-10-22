# -*- coding: utf-8 -*-
{
    'name': "Khachhang BaoHanh",
    'summary': """khach hang""",
    'description': """khachhang information""",
    'author': "TGDD",
    'website': "https://BaohanhTgdd.com",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': [
        'crm',
        'base'
    ],
    'data': [
       'views/KhachhangBH.xml',
       'views/menu.xml'
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}