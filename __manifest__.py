{
    'name': 'Contact Categorization',
    'version': '1.0',
    'summary': 'Categorize contacts into Customers, Vendors, and Employees',
    'description': 'Adds a category field to contacts'
                   ' Customers, Vendors, or Employees.',
    'author': 'Impelement Digital',
    'depends': ['base', 'contacts'],
    'data': [
        'views/action.xml',
        'views/menu.xml',
        'views/contact_custom.xml',
    ],
    'installable': True,
    'application': True,
}

