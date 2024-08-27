# Odoo models
from odoo import api, fields, models
from datetime import datetime

class CustomerComplaint(models.Model):
	_name = "sale_customer_complaint_ssg.customercomplaint"
	_description = "Customer Complaints"

	@api.onchange('customer')
	def onchange_customer(self):
		if self.customer:
			if self.customer.email:
				self.emailAddress = self.customer.email
		else:
			self.emailAddress = ''	

	customer = fields.Many2one('res.partner', string='Customer', required=True)
	emailAddress = fields.Char(string='Customer Email', required=True, store = True)
	jobNumber = fields.Many2one('sale.order', string='Job Number')
	complaintDate = fields.Date(string='Complaint Date', default=datetime.today())
	complaintReason = fields.Selection(string='Complaint Reason',selection=[
		("installationIssue","Installation Issue"),
		("technicianBehaviour","Technician Behaviour"),
		("other","Other")
	], required=True)
	notes = fields.Text(string="Notes")