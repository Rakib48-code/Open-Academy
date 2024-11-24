{
    'name': "Open Academy",
    'sequence': '-100',
    'version': '1.0',
    'depends': ['base'],
    'author': "Rakib Hasan",
    'category': 'Education',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/open_academy_menu.xml',
        'views/course_view_menu.xml',
        'views/session_view.xml',
        'views/partner.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
