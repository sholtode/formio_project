# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from odoo import api, fields, models, _
from odoo.addons.formio.models.formio_builder import STATE_CURRENT as BUILDER_STATE_CURRENT
from odoo.addons.formio.utils import get_field_selection_label


class Form(models.Model):
    _inherit = 'formio.form'

    project_task_id = fields.Many2one('project.task', string='Project Aufgabe', readonly=True)

    def _prepare_create_vals(self, vals):
        vals = super(Form, self)._prepare_create_vals(vals)
        builder = self._get_builder_from_id(vals.get('builder_id'))
        res_id = self._context.get('active_id')

        if not builder or not builder.res_model_id.model == 'project.task':
            return vals

        project_task = self.env['project.task'].browse(res_id)
        vals['project_task_id'] = res_id
        vals['res_partner_id'] = project_task.partner_id.id

        action = self.env.ref('project.act_project_project_2_project_task_all')
        url = '/web?#id={id}&view_type=form&model={model}&action={action}'.format(
            id=res_id,
            model='project.task',
            action=action.id)

        vals['res_act_window_url'] = url
        vals['res_name'] = project_task.name
        return vals

    @api.onchange('builder_id')
    def _onchange_builder_domain(self):
        res = super(Form, self)._onchange_builder_domain()
        if self._context.get('active_model') == 'project.task':
            res_model_id = self.env.ref('project.model_project_task').id
            domain = [
                ('state', '=', BUILDER_STATE_CURRENT),
                ('res_model_id', '=', res_model_id),
            ]
            res['domain'] = {'builder_id': domain}
        return res
