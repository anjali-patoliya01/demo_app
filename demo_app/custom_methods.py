import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field
from erpnext.selling.doctype.customer.customer import Customer


def add_customer_group_count_field():
    # Check if the custom field already exists to avoid duplication
    if not frappe.db.exists('Custom Field', 'Customer-customer_group_count'):
        custom_field = frappe.get_doc({
            'doctype': 'Custom Field',
            'dt': 'Customer',
            'fieldname': 'customer_group_count',
            'label': 'Customer Group Count',
            'fieldtype': 'Int',
            'insert_after': 'customer_group',
            'default': 0,
            'read_only': 1,
            'description': 'Tracks the count of customers in the same group'
        })
        
        # Insert the custom field into the database
        custom_field.insert()
        frappe.db.commit()

add_customer_group_count_field()




# def update_customer_group_count_on_insert(doc, method):
#     if doc.customer_group:
#         # Count the number of customers in the selected customer group
#         customer_count = frappe.db.count('Customer', filters={'customer_group': doc.customer_group})

#         customer_count += 1
        
#         # Update the 'customer_group_count' field in the newly created customer
#         frappe.db.set_value('Customer', doc.name, 'customer_group_count', customer_count)
#         print(f'\n\n\n { customer_count }  \n\n\n')
#         frappe.db.commit()





# def add_delivery_note():
#     # Check if the custom field already exists to avoid duplication
#     if not frappe.db.exists('Custom Field', 'Sales Invoice-note'):
#         custom_field = frappe.get_doc({
#             'doctype': 'Custom Field',
#             'dt': 'Sales Invoice',
#             'fieldname': ' delivery_note',
#             'label': 'Add your Note',
#             'fieldtype': 'Text',
#             'insert_after': 'customer',
#             'default': 0,
           
#         })
        
#         # Insert the custom field into the database
#         custom_field.insert()
#         frappe.db.commit()

# add_delivery_note()




def add_special_note_field():
    # Check if the field already exists
    if not frappe.db.exists("Custom Field", {"dt": "Delivery Note", "fieldname": "special_note"}):
       
        custom_field = frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Delivery Note",  # Doctype to which the field is added
            "fieldname": "special_note",  
            "label": "Special Note",  
            "fieldtype": "Small Text",  
            "insert_after": "customer_name",  
            "description": "A special note for the customer",
            # "default": "Thank you for your business!", 
            "print_hide": 0, 
        })
        custom_field.insert()
        frappe.db.commit()
        print("\n\n Custom field 'special_note' added to Delivery Note.\n\n")
    else:
        print("\n\n Field 'special_note' already exists in Delivery Note.\n\n")

add_special_note_field()


