# -*- coding: utf-8 -*-
##############################################################################
#
#    Smart Solution bvba
#    Copyright (C) 2010-Today Smart Solution BVBA (<http://www.smartsolution.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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

{
    "name" : "Project Team",
    "version" : "1.0",
    "author" : "Smart Solution (fabian.semal@smartsolution.be)",
    "category" : "Generic Modules/Project",
    "description": """
    Add the concept of Team of users to the project task
""",
    "depends" : ["project"],
    "init_xml" : [
        ],
    "update_xml" : [
        'project_team_view.xml',
        ],
    "active": False,
    "installable": True
}
