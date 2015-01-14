#!/usr/bin/env python
# -*- encoding: utf-8 -*-
##############################################################################
#
##############################################################################

from osv import osv, fields
from tools.translate import _

class res_user_team(osv.osv):

    _name = 'res.user.team'

    _columns = {
        'name': fields.char('Team', size=64, required=True),
    }

res_user_team()


class project_task(osv.osv):

    _inherit = 'project.task'

    _columns = {
        'team_id': fields.many2one('res.user.team', 'Project'),
    }

project_task()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
