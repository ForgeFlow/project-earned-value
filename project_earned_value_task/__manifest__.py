##############################################################################
#
#    Copyright (C) 2019 Eficent (<http://www.eficent.com/>)
#              <contact@eficent.com>
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
    "name": "Earned Value Management using tasks",
    "version": "12.0.1.0.0",
    "author": "Eficent",
    "website": "https://github.com/Eficent/project-earned-value",
    "category": "Generic Modules/Projects & Services",
    "depends": [
        "project_gantt", "hr_timesheet",
    ],
    "description": """
        - 
    """,
    "data": [
        "security/ir.model.access.csv",
        "data/project_data.xml",
        "wizard/earned_value_view.xml",
        "view/project_evm_view.xml",
        "view/project_view.xml",
    ],
    'demo': [
        "data/project_demo_slides.xml",
    ],
    'installable': True,
}
