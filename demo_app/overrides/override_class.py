import frappe
from frappe import _
from frappe.utils import getdate, today


from  erpnext.setup.doctype.employee.employee import Employee
# from  erpnext.selling.doctype.sales_order.sales_order import SalesOrder 



class CustomEmployee(Employee):
    def on_update(self):
        super(CustomEmployee, self).on_update()
        if self.final_confirmation_date and getdate(self.final_confirmation_date) < getdate(today()):
            frappe.throw(_('Conformation date cannot be lesser than today'))
            


# class CustomEmployee(Employee):

#     # 1. ------- Custom validation logic ------- 
#     def validate(self):
#         super(CustomEmployee, self).validate()  
#         if not self.department:
#             frappe.throw("Department is mandatory")
        
#         if self.employee_number and len(self.employee_number) < 6:
#             frappe.throw("Employee number must be at least 6 characters long")
        
#         frappe.msgprint(f"Validated employee: {self.employee_name}")



#     # 2. -------  Logic before saving the document ------- 
#     def before_save(self):
#         if self.status == "Left":
#             frappe.throw("Cannot save employee with 'Left' status")



#     # 3. -------  Logic after inserting the document  ------- 
#     def after_insert(self): 
#         frappe.msgprint(f"New Employee record created: {self.employee_name}")



#     # 4. ------- Custom logic before submitting the document  ------- 
#     def before_submit(self):
#         if self.date_of_joining and not self.final_confirmation_date:
#             frappe.throw("Confirmation date is required before submitting")        
#         frappe.msgprint(f"Ready to submit employee: {self.employee_name}")



#     # 5.------- Logic after submitting the document  -------
#     def on_submit(self):
#         frappe.msgprint(f"Employee record submitted: {self.employee_name}")



#     # 6. ------- Custom logic before canceling the document -------
#     def before_cancel(self):
#         if self.status != "Active":
#             frappe.throw("Can only cancel records of employees who have 'Active' status") 
#         frappe.msgprint(f"Canceling employee record: {self.employee_name}")



#     # 7. ------- Logic after canceling the document  -------
#     def on_cancel(self):
#         frappe.msgprint(f"Employee record canceled: {self.employee_name}")



#     # 8. ------- Custom logic before deleting (trashing) the document  -------
#     def before_delete(self):
#         super(CustomEmployee, self).before_delete()  
#         frappe.msgprint(f"Preparing to delete employee record: {self.employee_name}")



#     # 9. ------- Logic after deleting the document  -------
#     def after_delete(self):
#         super(CustomEmployee, self).after_delete() 
#         frappe.msgprint(f"Employee record deleted: {self.employee_name}")




# class CustomSalesOrder(SalesOrder):
#     # def validate(self):
#     #     # Call the original validate method (if needed)
#     #     super(CustomSalesOrder, self).validate()

#     #     # Call the custom validation logic for purchase order
#     #     self.validate_po()

#     def validate_po(self):
#          if self.po_date and not self.skip_delivery_note:
#               for d in self.get("items"):
#                    if d.delivery_date and getdate(self.po_date) > getdate(d.delivery_date):
#                        frappe.throw(
#                             _("Row #{0}: The Expected Delivery Date must be on or after the Purchase Order Date.-> Override Message").format(d.idx)
#                         )   
