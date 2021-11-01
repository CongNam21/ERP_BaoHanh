# -*- coding: utf-8 -*-
{
    'name': "Quanlisanpham",
    'summary': """loai san pham""",
    'description': """product""",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
        'hr'
    ],
    'data': [
        'views/loaisp_views.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
