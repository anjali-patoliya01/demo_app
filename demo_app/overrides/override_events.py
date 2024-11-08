import frappe
from erpnext.selling.doctype.customer.customer import Customer


def update_customer_group_count_on_insert(doc, method):
    if doc.customer_group:
        # Count the number of customers in the selected customer group
        customer_count = frappe.db.count('Customer', filters={'customer_group': doc.customer_group})

        customer_count += 1
        
        # Update the 'customer_group_count' field in the newly created customer
        frappe.db.set_value('Customer', doc.name, 'customer_group_count', customer_count)
        print(f'\n\n\n { customer_count }  \n\n\n')
        frappe.db.commit()


    