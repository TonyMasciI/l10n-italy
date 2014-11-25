# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Associazione Odoo Italia
#    (<http://www.odoo-italia.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################

{
    "name": "Pec Messages",
    "version": "1.0",
    "author": "Odoo Italian Community",
    "category": "Certified Mailing",
    "website": "http://www.odoo-italia.org",
    "description": """
Pec Messages Management
------------
    Mail PEC Management via Alias

Authors:
------------
    """,
    'images': [],
    'depends': [
        'fetchmail', 'mail','l10n_it_pec'
    ],
    'init_xml': [],
    'data': [
        "fetchmail/view.xml",
        "mail/view.xml",
    ],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'active': False,
}
