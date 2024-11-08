# Copyright (c) 2024, abc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _



class StudentDoc(Document):
	pass

# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------>>      Database API      <<-------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------



# #------------------------------------ frappe.db.get_list  ---------------------------------
''' frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length) '''
# class StudentDoc(Document):
#     def validate(self):
#         self.get_list()
        
#     def get_list(self):
#         doc = frappe.db.get_list('Parent Doc',
#                                  filters={
#                                      'enable': 1
# 								 },
#                                 fields = ['full_name','phone'],
#                                 order_by = 'full_name asc'
#                                 # order_by = 'full_name desc'
#                                 # start=18,
# 								# page_length=10,
#     							# as_list=True
#     						)
        
#         for d in doc:
#              frappe.msgprint(_(f'Parent Name is {d.full_name} and phone number is {d.phone}'))
    



# ------------------------------------- frappe.db.get_all ----------------------------------------
''' frappe.db.get_all(doctype, filters, or_filters, fields, order_by, group_by, start, page_length) 
	Same as frappe.db.get_list but will fetch all records without applying permissions.    '''
# class StudentDoc(Document):
#     def validate(self):
#         self.get_list()
        
#     def get_list(self):
#         doc = frappe.db.get_list('Parent Doc',
#                                  filters={
#                                      'enable': 1
# 								 },
#                                 fields = ['full_name','phone']
#     						)
        
#         for d in doc:
#              frappe.msgprint(_(f'Parent Name is {d.full_name} and phone number is {d.phone}'))
    






# ------------------------------------- frappe.db.get_value ----------------------------------------
'''  frappe.db.get_value(doctype, name, fieldname) or frappe.db.get_value(doctype, filters, fieldname)
	 Returns a document's field value or a list of values.   '''

# class StudentDoc(Document):
# 	def validate(self):
# 		self.get_value()

		
# 	def get_value(self):

# 		# # single value
# 		# std = frappe.db.get_value('Student Doc', 'A', 'std')
# 		# frappe.msgprint(f'student A is std in {std}')


# --------- Get Multiple value --------

# class StudentDoc(Document):
#     def validate(self):
#         self.get_value()

#     def get_value(self):
#         # Fetch values from the document
#         result = frappe.db.get_value('Student Doc', filters={'name': 'B'}, fieldname=['student_name', 'std'])
        
#         if result:
#             student_name, std = result
#             frappe.msgprint(f'Student name is {student_name} and std is {std}')
#         else:
#             frappe.msgprint('No data found for the specified criteria')



# -------- Get value as dict ---------
# class StudentDoc(Document):
# 	def validate(self):
# 		self.get_value_as_dict()
		
# 	def get_value_as_dict(self):
# 		task_dict = frappe.db.get_value('Student Doc', 'A', ['student_name', 'std'], as_dict=1)
# 		task_dict.student_name
# 		task_dict.std
# 		frappe.msgprint(f'student name is {task_dict.student_name} and std in {task_dict.std}')



# ---------  with filters, will return the first record that matches filters -------
# class StudentDoc(Document):
# 	def validate(self):
# 		self.get_value_as_dict()
		
# 	def get_value_as_dict(self):
# 		student_name, std = frappe.db.get_value('Student Doc', {'status': 'open'}, ['student_name', 'std'])
# 		frappe.msgprint(f'student name is {student_name} and std in {std}')









# ------------------------------------- frappe.db.get_single_value(doctype, fieldname) ----------------------------------------

''' Returns a field value from a Single DocType. '''

# class StudentDoc(Document):
#     def validate(self):
#         self.get_single_value()
    
#     def get_single_value(self):
#         try:
#             student_school_name= frappe.db.get_single_value('Single Doc', 'student_school_name')
#             if student_school_name:
#                 print('----------------------------------------------', student_school_name)
#                 frappe.msgprint(f'Student School Name is {student_school_name}')
#             else:
#                 print('-------------------- No student School name found or field is empty--------------------------')
#         except Exception as e:
#             print('Error occurred:', e)










# # ------------------------------------- frappe.db.set_value(doctype, name, fieldname, value)  ----------------------------------------
# ''' Sets a field's value in the database, does not call the ORM triggers but updates the modified timestamp 
#     (unless specified not to). '''

# class StudentDoc(Document):
#     def validate(self):
#         self.set_value()
    
#     def set_value(self):
#         	# Update Single Value
#            frappe.db.set_value('Student Doc', 'A', 'email', 'studenta02@gmail.com')
#            frappe.msgprint('Email is set in Student A')
           

		      
# 		#    Update Multiple Value
#            frappe.db.set_value('Student Doc', 'B', {
#     							'std': '5',
#     							'email': 'studentb01@gmail.com'
# 								})
#            frappe.msgprint('xstudent std and email is set for student B')
           
# 		# update without updating the `modified` timestamp
#            frappe.db.set_value('Student Doc', 'A', 'std', '9', update_modified=False)
           







# -------------------------------------------- frappe.db.exists(doctype, name) ----------------------------------------
''' Returns true if a document record exists '''

# class StudentDoc(Document):
#     def validate(self):
#         self.db_exists()
    
#     def db_exists(self):
#          is_db_exists= frappe.db.exists("Student Doc", "P", cache=True)
#          frappe.msgprint('Is DB Exists = {is_db_exists}')
         
# 		#  Pass a dict of filters including the "doctype" key
#          frappe.db.exists({"doctype": "Student Doc", "student_name": "A"})
         

#         #  Pass the doctype and a dict of filters
#          frappe.db.exists("Student Doc", {"student_name": "A"})
         








# -------------------------------------------- frappe.db.count(doctype, filters) ----------------------------------------
''' Returns number of records for a given doctype and filters. '''
# class StudentDoc(Document):
#     def validate(self):
#         self.db_count()
    
#     def db_count(self):
#         #    doc_count = frappe.db.count('Student Doc')
#         #    frappe.msgprint(f'Total Student Doc Type is { doc_count }')
           
#            doc_count_status = frappe.db.count('Student Doc', {'status': 'Open'})
#            frappe.msgprint(f'Total Student Doc Type which status is { doc_count_status }')








#  -------------------------------------------- frappe.db.delete(doctype, filters) ----------------------------------------
'''    Delete doctype records that match filters. This runs a DML command, which means it can be rolled back. 
   If no filters specified, all the records of the doctype are deleted.    '''

