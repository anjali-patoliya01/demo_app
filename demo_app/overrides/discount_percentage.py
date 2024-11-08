import frappe

def before_save(doc, method):
    discount_percentage = doc.additional_discount_percentage = 5
    frappe.msgprint(f'discount set : {discount_percentage}%')
