# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OdooTutorial(models.Model):
    _name = "odoo.tutorial"
    _inherit = ["odoo.tutorial.abstract", "mail.thread"]
    _description = "Odoo Technical Tutorial"

    name = fields.Char(string="Name", default="New", index=True, size=100, trim=True)
    total = fields.Integer(string="Total", tracking=True)
    description = fields.Text(string="Description", translate=True)
    user_id = fields.Many2one(string="User", comodel_name="res.users", ondelete="restrict", tracking=True)
    total_compute = fields.Float(
        compute="_compute_total", store=True, string="Total Compute", tracking=True
    )
    tags_ids = fields.Many2many(
        comodel_name="res.partner.category",
        relation="odoo_tutorial_res_partner_category_rel",
        column1="odoo_tutorial_id",
        column2="partner_category_id",
        string="Tags",
    )
    odoo_tutorial_line = fields.One2many(
        comodel_name="odoo.tutorial.line",
        inverse_name="odoo_tutorial_id",
        string="Odoo Tutorial"
    )
    active = fields.Boolean(string='Active', default=True)
    company_id = fields.Many2one(comodel_name="res.company", string="Company", tracking=True)

    # part 2
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
    price_total = fields.Monetary(
        compute="_compute_total",
        store=True,
        string="Price Total",
        currency_field="currency_id",
        tracking=True,
    )
    attachment = fields.Binary(string="Attachment", attachment=False)
    icon_image = fields.Image(string="Icon Image", max_height=1024, max_width=1024)
    note = fields.Html(string="Note")
    date_only = fields.Date(string="On Date", default=fields.Date.today())
    start_date = fields.Datetime(string="Start Date", default=fields.Datetime.now())
    end_date = fields.Datetime(string="End Date")
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("ready", "Ready"),
            ("done", "Done"),
            ("cancel", "Cancel")
        ],
        string="Status", default="draft", required=True, tracking=True
    )
    ref = fields.Reference(string="Reference", selection=[("res.partner", "Partner")])
    model_name = fields.Char(string="Model")  # odoo.tutorial
    res_id = fields.Many2oneReference(string="Res ID", model_field="model_name")

    @api.depends("total")
    def _compute_total(self):
        for record in self:
            record.total_compute = float(record.total)
            record.price_total = record.total_compute

    def action_confirm(self):
        return self.write({"state": "ready"})

    def action_done(self):
        return self.write({"state": "done"})

    def action_cancel(self):
        return self.write({"state": "cancel"})

    def action_view_sales(self):
        # next section
        return

    # ORM API CRUD
    @api.model_create_multi
    def create(self, vals_list):
        # custom code
        res = super().create(vals_list)
        # custom code
        return res

    def read(self, fields=None, load='_classic_read'):
        return super().read(fields=fields, load=load)

    def write(self, vals):
        # custom code
        res = super().write(vals)
        # custom code
        return res

    def unlink(self):
        # custom code
        return super().unlink()


class OdooTutorialLine(models.Model):
    _name = 'odoo.tutorial.line'
    _description = 'Odoo Technical Tutorial Line'

    odoo_tutorial_id = fields.Many2one(comodel_name="odoo.tutorial", string="Odoo Tutorial", ondelete="cascade")
    name = fields.Char()
    price_unit = fields.Float()
    qty = fields.Float(string="Quantity")
