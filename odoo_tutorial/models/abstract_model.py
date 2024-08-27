from odoo import fields, models


class OdooModelAbstract(models.AbstractModel):
    _name = "odoo.tutorial.abstract"
    _description = "Odoo Tutorial Abstract"

    general_description = fields.Text()
    instructor_id = fields.Many2one(
        comodel_name="res.users",
        string="Instructor",
        ondelete="restrict",
        required=True,
    )
