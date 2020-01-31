# Copyright 2020 ForgeFlow S.L. (https://www.forgeflow.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)

{
    "name": "Earned Value Management using tasks",
    "version": "12.0.1.0.0",
    "author": "ForgeFlow",
    "license": "LGPL-3",
    "website": "https://github.com/ForgeFlow/project-earned-value",
    "category": "Generic Modules/Projects & Services",
    "depends": [
        "project_gantt", "hr_timesheet", "analytic_resource_plan"
    ],
    "summary": """
        PM Book - Earned value management
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
