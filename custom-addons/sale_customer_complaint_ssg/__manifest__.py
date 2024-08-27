{
	'name':'Customer Complaints',
	'version':'13.0.01',
	'author':'Solar Service Guys',
	'website':'https://www.solarserviceguys.com.au/',
	'depends':['sale'],
	'data':[
	'security/sale_customer_complaint_ssg_security.xml',
	'security/ir.model.access.csv',
	'views/customer_complaint.xml'
	],
	'installable': True
}