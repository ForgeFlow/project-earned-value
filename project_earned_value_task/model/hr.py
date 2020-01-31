# Copyright 2020 ForgeFlow S.L. (https://www.forgeflow.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)

from odoo import models, api, exceptions, _


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.model
    def get_employee_cost(self, user_id):
        employee_ids = self.search([('user_id', '=', user_id)])
        if not employee_ids:
            raise exceptions.Warning(
                _('Error!: No employee is assigned to user.'))
        for employee in employee_ids:
            if not employee.timesheet_cost:
                raise exceptions.Warning(
                    _('Error!: No timesheet cost is assigned to employee %s.'),
                    (employee.name,))
            return employee.timesheet_cost

