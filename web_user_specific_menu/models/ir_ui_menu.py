# -*- coding: utf-8 -*-
##############################################################################
#
#    Module for Odoo
#    Copyright (C) 2015 SYLEAM Info Services (<Alexandre MOREAU>)
#              Alexandre MOREAU <alexandre.moreau@syleam.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    @api.model
    @api.returns('ir.ui.menu')
    def get_user_roots(self):
        super(IrUiMenu, self).create()
        menu_domain = [('parent_id', '=', self.env.user.menu_id.id)]
        return self.search(menu_domain)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
