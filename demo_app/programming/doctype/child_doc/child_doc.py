# Copyright (c) 2024, abc and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
from frappe import _


# ------------------------------------ Documnet API -----------------------------------


# ------------------------ frappe.get_doc(doctype, name) -------------------------
""" return a document object of the record identified by doctype and name """ 

# class ChildDoc(Document):

	## frappe.get_doc(doctype, name)

	# def validate(self):
	# 	self.get_document()


	# def get_document(self):
	# 	doc = frappe.get_doc('Parent Doc', self.parent_doc_link)
	# 	frappe.msgprint(_(f"The Parent name is {doc.full_name} and Phone number is {doc.phone}"))


	
	# def get_document(self):
    # 	# Create a dictionary with doctype and name
	# 	doc_dict = {
	# 		'doctype': 'Parent Doc',
	# 		'name': self.parent_doc_link
	# 	}
		
	# 	doc = frappe.get_doc(doc_dict)
		
	# 	# Display the message
	# 	frappe.msgprint(_(f"The Parent name is {doc.full_name} and Phone number is {doc.phone}"))
    




# -------------------------------------------------------------------------------------------------------




# class ChildDoc(Document):

# 	def validate(self):
# 		self.get_document()

# 	def get_document(self):
# 		doc = frappe.get_doc({
# 		'doctype': 'Parent Doc',
# 		'full_name': 'Parent3',
# 		'phone':'2344154677'
# 		})
		
# 		doc.insert()
# 		print("/n/n-----------------------------------------------------------------/n/n",doc)
# 		doc.save()



# ---------------------------------------------------------------------------------------------------------------------------------- 

# ------------------------- frappe.get_doc(doctype={document_type}, key1 = value1, key2 = value2, ...) ------------------------- 


# class ChildDoc(Document):

# 	def validate(self):
# 		self.new_document() 	


# 	def new_document(self):
# 		doc = frappe.new_doc('Parent Doc')
# 		doc.full_name = 'Parent6'
# 		doc.phone = '2233124567'
# 		doc.save()
# 		frappe.msgprint(f'{doc.full_name} is added succesfully in Parent Doc')





# -----------------------------------------------------  Frappe.delete_doc(doctype, name)  ---------------------------------------------- 

# class ChildDoc(Document):
# 	def validate(self):
# 		frappe.delete_doc('Parent Doc', 'B')
# 		frappe.msgprint(f'DOctype deleted succesfuly..')




#-----------------------------------------------------  Frappe.get_last_doc(doctype, filters, order_by)  ---------------------------------------------- 

# class ChildDoc(Document):

# 	def validate(self):
# 		frappe.get_last_doc('Parent Doc')



#----------------------------------------------------- frappe.rename_doc(doctype, old_name, new_name, merge=False) -----------------------------------------------------
# class ChildDoc(Document):

# 	def validate(self):
# 		frappe.rename_doc('Parent Doc','B','Parent-1')



# ------------------------------------------------- frappe.get_meta() ----------------------------------------------
# class ChildDoc(Document):
#     def validate(self):
#         meta = frappe.get_meta('Parent Doc')
#         meta.has_field('full_name')
# 		# meta.get_custom_fields()

            







####################################  Documnent Method ##########################################

# --------------------------------- doc.insert() --------------------------------

''' It will Check for user permissions and execute before_insert, validate, on_update, after_insert methods if they
	are written in the controller. '''

# class ChildDoc(Document):
    
# 	def validate(self):
# 		self.new_document()
	
# 	def new_document(self):
# 		doc = frappe.new_doc('Parent Doc')
# 		doc.full_name = 'Parent7'
# 		doc.phone = '9879665456'
# 		doc.insert()

# 		# Some escape hatches that can be used to skip certain checks
# 		# doc.insert(
# 		# 	ignore_permission = True,    # ignore write permissions during insert
# 		# 	ignore_links = True,		 # ignore Link validation in the document
# 		# 	ignore_if_duplicate = True,  # done insert if DuplicateEntryError is Thrown
# 		# 	ignore_mandatory = True      # insert evenn if mandatory fields are not set
# 		# )




# # --------------------------------- doc.save() --------------------------------

# ''' This will check for user permissions and execute validate before and on_update after updating values1 '''

# class ChildDoc(Document):
    
# 	def validate(self):
# 		self.save_document()
	
# 	def save_document(self):
# 		doc = frappe.new_doc('Parent Doc')
# 		doc.full_name = 'ABCD'
# 		doc.phone = '1524334566'
# 		doc.save()

# 		# Some escape hatches that can be used to skip certain checks
# 		# doc.insert(
# 		# 	ignore_permission = True,    # ignore write permissions during insert
# 		#   ignore_version = True        # Do not create a record
# 		# )






# # --------------------------------- doc.delete() --------------------------------

# class ChildDoc(Document):
    
# 	def validate(self):
# 		self.delete_document()
	
# 	def delete_document(self):
# 		doc = frappe.get_doc('Parent Doc','Parent6')
# 		doc.delete()





# # --------------------------------- doc.db_set() --------------------------------

# class ChildDoc(Document):
    
# 	def validate(self):
# 		self.db_set_document()
	
# 	def db_set_document(self):
# 		doc = frappe.get_doc('Parent Doc','New Doc')
# 		doc.db_set('phone','7366453321')




# --------------------------------- doc.get_doc_before_save  --------------------------------- 
# class ChildDoc(Document):
#     def validate(self):
#         self.check_phone_change()

#     def check_phone_change(self):
#         old_doc =self.get_doc_before_save()
#         if old_doc.parent_age != self.parent_age:
#             frappe.msgprint(f"Parent age has changed from {old_doc.parent_age} to {self.parent_age}")




# # --------------------------------- doc.has_value_changed  -------------------------------------
# class ChildDoc(Document):
#     def after_save(self):
#       value_change = self.has_value_changed('parent_full_name')
#       print('-------------------------------------',value_change)
#       if value_change:
#            frappe.msgprint(f"Parent Name has changed")
             




# # --------------------------------- doc.check_permission --------------------------------

# class ChildDoc(Document):
#     def validate(self):
#         if not self.check_permission(permtype='enable'):
#             frappe.msgprint("You do not have permission to enable this document.")





# # --------------------------------- doc.get_title() --------------------------------

# class ChildDoc(Document):
    
# 	def validate(self):
# 		self.get_title()
	
# 	def get_title(self):
# 		doc = frappe.get_doc('Parent Doc')
# 		title = doc.get_title()
# 		frappe.msgprint(f'Doc type Title is {title}')
# 		print('-----------------------------------------------------------',title)





# # --------------------------------- doc.notify_update() --------------------------------
# class ChildDoc(Document):
#     def validate(self):
#         self.notify_update()
#         frappe.msgprint("Document has been updated and notification sent")





# # --------------------------------- doc.db_set() --------------------------------
# class ChildDoc(Document):
#     def validate(self):
#         # doc = frappe.get_doc('Parent Doc','A')
#         # doc.db_set('phone', 1903115677)
#         # frappe.msgprint(f'Phone numbef is set in {doc}')
        

#         # notify_update
#         self.db_set('age', 16, notify=True)
#         frappe.msgprint('updates value in database, will trigger doc.notify_update()')
        
#         # commit
#         self.db_set('age', 20, commit=True)
#         frappe.msgprint('updates value in database, will also run frappe.db.commit()')
        
# 		# Update_modified
#         self.db_set('age', 20, update_modified=False)
#         frappe.msgprint('updates value in database, does not update the modified timestamp')






# # ----------------------------------------- doc.append ---------------------------------------

# class ChildDoc(Document):
#     def validate(self):
#         self.append("childtable", {
#     		"child_name": "AAA",
#     		"age": 10,
#             "std": 4,
# 		})
        
#         self.append("childtable", {
#     		"child_name": "BBB",
#     		"age": 13,
#             "std": 7,
# 		})
        
#         self.append("childtable", {
#     		"child_name": "CCC",
#     		"age": 17,
#             "std": 11,
# 		})
        

# # Using For Loop add multiple row

# class ChildDoc(Document):
#     def validate(self):
#         row_to_add = [ 
#             {
# 				"child_name": "A1",
# 				"age": 11,
# 				"std": 5,
# 			},
# 			{
# 				"child_name": "B1",
# 				"age": 15,
# 				"std": 9,
# 			}, 
# 			{
# 				"child_name": "C1",
# 				"age": 17,
# 				"std": 11,
# 			}]
        
#         for row in row_to_add:
#             self.append('childtable',row)
            
#         frappe.msgprint('Successfully Add Row in child table')
        






# #  ---------------------------------------------- doc.get_url ------------------------------------------------
# class ChildDoc(Document):
#     def validate(self):
#         url = self.get_url()
#         print('\n\n ----------------------------------\n\n',url)
#         frappe.msgprint(f'URL of this Doc is : {url}')







# #  ---------------------------------------------- doc.add_comment ------------------------------------------------
# class ChildDoc(Document):
#     def validate(self):
#         # # add a simple comment
#         self.add_comment('Comment', text='Test Comment...')
#         frappe.msgprint('Comment added successfully...')
        
# 		# add a comment of type Edit
#         self.add_comment('Edit','Now You can edit this comment........	')
#         frappe.msgprint('You can Edit Administrator Comment......')
        
#         user = frappe.session.user  # Assuming user information can be obtained this way
#         self.add_comment("Shared", "{0} shared this document with everyone".format(user))
#         frappe.msgprint('You can shared this dicument')






# #  ---------------------------------------------- doc.add_seen ------------------------------------------------
# class ChildDoc(Document):
#     def validate(self):
#         self.add_seen('anjupatel01@gmail.com')
#         frappe.msgprint('add anju to list of seen')
#         self.add_seen()






# #  ---------------------------------------------- doc.add_viewed ------------------------------------------------
# class ChildDoc(Document):
#     def validate(self):
#         self.add_viewed('anjupatel01@gmail.com')
#         # add a view log by session user
#         self.add_viewed()






# # ---------------------------------------------- doc.add_tag ------------------------------------------------
# class ChildDoc(Document):
#     def validate(self):
#         doc = frappe.get_doc("Child Doc", 'child-1')
#         doc.add_tag('Developer')
#         frappe.msgprint(f"tag added succesfuly in {doc}")





 # ---------------------------------------------- doc.get_tag ------------------------------------------------
# class ChildDoc(Document):
#     def validate(self):
#         # doc = frappe.get_doc("Child Doc", 'AA3')
#         tag = self.get_tags()
#         frappe.msgprint(f"{tag} get ")








# ------------------------------------------------ doc.run_method -----------------------------------------------
# class ChildDoc(Document):
#     def validate(self):
#         doc = frappe.get_doc('Chid Doc', 'VP')
#         doc.run_method('validate')




#  ------------------------------------- doc.db_insert() ---------------------------------


# class ChildDoc(Document):
#     def insert_document():
#             doc_data = {
# 			'doctype': 'Parent Doc',
# 			'full_name': 'A1',
# 			'phone': '2212334566',
# 			}
#             doc = frappe.get_doc(doctype="Parent Doc", data=doc_data)
#             doc.db_insert()
#             print(f"Document {doc.name} inserted successfully using db_insert.")





# ------------------------------------- frappe.db.sql(query, values, as_dict) --------------------------------- 

# class ChildDoc(Document): 
#     def validate(self):
#         self.sql()
        
#     def sql(self):
#         data = frappe.db.sql(""" 
# 								SELECT 
# 									full_name,
# 									phone
#                                 FROM
# 									`tabParent Doc`
# 								WHERE
# 									enable = 1
# 							""", as_dict = 1)
#         for d in data:
#             frappe.msgprint(_(f'The Parent Full Name is {d.full_name} and phone number is {d.phone}'))








# ------------------------------------- frappe.db.rename_table(old_name, new_name) --------------------------------- 
''' Executes a query to change table name. 
    Specify the DocType or internal table's name directly to rename the table. '''

# class ChildDoc(Document): 
#     def validate(self):
#         self.rename_table()
        
#     def rename_table(self):
#         rename_table =frappe.rename_table('Child Doc','Child doc')
#         frappe.msgprint(f'Table name is renamed = {rename_table}')



# class ChildDoc(Document): 
#     def validate(self):
#         self.rename_table()
        
#     def rename_table(self):
#         try:
#             # Use raw SQL to rename tables
#             frappe.db.sql("""
#                 RENAME TABLE `tabChildDoc` TO `tabChild Doc`
#             """)
#             frappe.db.commit()  # Commit the transaction

#             frappe.msgprint('Table name has been renamed to `Child Doc`')

#         except Exception as e:
#             frappe.log_error(f"Error renaming table: {e}", "Table Rename Error")
#             frappe.msgprint(f"Error renaming table: {e}")

        




# ------------------------------------- frappe.db.add_index(doctype, fields, index_name) --------------------------------- 
''' Creates indexes for doctypes for the specified fields. '''
