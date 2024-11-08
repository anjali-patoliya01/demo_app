# Copyright (c) 2024, abc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


# class ServerSideScripting(Document):
    
	# ------------------------------------------ Event --------------------------------------
	# def validate(self):
	# 	frappe.msgprint("Hello Frappe from 'validate' event")


	# def before_save(self):
	# 	frappe.throw("Hello Frappe from 'before_save' event")

	
	# def before_insert(self):
	# 	frappe.throw("Hello Frappe from 'before_insert' event")
	

	# def after_insert(self):
	# 	frappe.throw("Hello Frappe from 'after_insert' event")


	# def on_update(self):
	# 	frappe.msgprint("Hello Frappe from 'on_update' event")

	
	# def before_submit(self):
	# 	frappe.msgprint("Hello Frappe from 'before_submit' event")

	
	# def on_submit(self):
	# 	frappe.msgprint("Hello Frappe from 'on_submit' event")


	# def on_cancel(self):
	# 	frappe.msgprint("Hello Frappe from 'on_cancel' event")
	

	# def on_trash(self):
	# 	frappe.msgprint("Hello Frappe from 'on_trash' event")


	# def after_delete(self):
	# 	frappe.msgprint("Hello Frappe from 'after_delete' event")








# -------------------------- frm_call() ------------------

class ServerSideScripting(Document):
	@frappe.whitelist()
	def frm_call(self,msg):
		import time
		time.sleep(5)
		frappe.msgprint(msg)

		return 'hii this message from frm_call'