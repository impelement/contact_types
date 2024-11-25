from odoo import fields, models, api


class ResPartnerCategory(models.Model):
    _inherit = 'res.partner'

    partner_category = fields.Selection([
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('employee', 'Employee')
    ], string='Category', default='customer')

    @api.model
    def categorize_existing_contacts(self):
        for partner in self.search([]):
            if partner.customer_rank > 0:
                partner.partner_category = 'customer'
            elif partner.supplier_rank > 0:
                partner.partner_category = 'vendor'
            elif partner.is_company and not partner.parent_id:
                partner.partner_category = 'employee'

    # env['res.partner'].categorize_existing_contacts()