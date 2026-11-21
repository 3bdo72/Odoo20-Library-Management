{
    'name': 'Library Management',
    'version': '1.0.0',
    'category': 'Services',
    'summary': 'Manage books, members and loans in a library',
    'author': 'Abdelrahman Soliman',
    'license': 'LGPL-3',
    'depends': ['base'],
    "data": [
        "security/ir.access.csv",
        "views/base_menu.xml",
        "views/library_book_views.xml"
    ],
    'installable': True,
    'application': True,
}
