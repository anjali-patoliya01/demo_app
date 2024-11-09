import frappe

def calculate_outstanding_amount(doc, method):
     customer_name = doc.customer
     invoices = frappe.db.get_all('Sales Invoice', filters={
      'customer': customer_name,
        'docstatus': 1
    }, fields=['outstanding_amount'])
     
    #  print('-------------------------------------------',  invoices )
     
    #  total_outstanding = sum(invoice.outstanding_amount for invoice in invoices)
     total_outstanding = 0
     for invoice in invoices:
          total_outstanding += invoice.outstanding_amount

     frappe.msgprint(f"Total Outstanding Amount for {customer_name}: {total_outstanding}")
     print(f"\n\nTotal Outstanding Amount for {customer_name}: {total_outstanding}\n")


