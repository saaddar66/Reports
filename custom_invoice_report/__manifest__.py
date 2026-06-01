{
    'name': 'Custom Invoice Report',
    'version': '18.0.1.0.0',
    'summary': 'Custom Sales Invoice PDF Report',
    'depends': ['account', 'sale'],
    'data': [
        'report/report_action.xml',
        'report/report_template.xml',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
