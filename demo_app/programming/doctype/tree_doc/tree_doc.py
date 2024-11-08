# Copyright (c) 2024, abc and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.nestedset import NestedSet





# -------------------------------------------- doc.get_children() -------------------------------------------- 

'''     Only available on tree DocTypes (inherited from NestedSet).
Returns a generator that yields an instance of NestedSet for each child record. '''

class TreeDoc(NestedSet):
	def validate(self):
		print('--------------------------------------',self)
		print('---------------------------------------------',self.get_children)
		# doc = frappe.get_doc('TreeDoc', 'Tree Doc') 
		for child_doc in self.get_children():
			print('---------------------------------------',child_doc)
			frappe.msgprint(f'Child is {child_doc.name}')











    