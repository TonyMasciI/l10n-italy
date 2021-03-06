# Copyright 2014 Davide Corio <davide.corio@abstract.it>
# Copyright 2015-2016 Lorenzo Battistini - Agile Business Group
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Italian Localization - Fiscal payment term',
    'version': '12.0.1.0.0',
    'category': 'Localization/Italy',
    'summary': 'Electronic invoices payment',
    'author': 'Davide Corio, Agile Business Group, Innoviu, '
              'Odoo Italia Network, Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/l10n-italy',
    'license': 'LGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/fatturapa_data.xml',
        'views/account_view.xml',
    ],
    'installable': True
}
