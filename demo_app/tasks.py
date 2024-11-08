from demo_app.task.doctype.student.student import Student
import frappe
import string
import random
import time


def all():
    pass


# def cron():
#     letters = string.ascii_letters
#     note = " ".join(random.choice(letters) for i in range(20))

#     new_note = frappe.get_doc({'doctype': 'Note',
#                                'title' : note})
    
#     new_note.insert()
#     frappe.db.commit()
# cron()
 


def daily():
    # Your daily job logic here
    pass


def hourly():
    # Your hourly job logic here
    pass


def weekly():
    # Your weekly job logic here
    pass


def monthly():
    # Your monthly job logic here
    pass





# def long_running_job(param1, param2):
#     try:
#         frappe.log("Starting long running job...")
#         time.sleep(10)
#         frappe.log(f"Completed long running job with params: {param1}, {param2}")
#     except Exception as e:
#         frappe.log(f"Error in long running job: {str(e)}")
#         raise 


def time_taking_process(self):
    import math
    var1 = math.factorial(2000000)
    frappe.publish_realtime('msgprint','time taking process completed', user=frappe.session.user)


def before_save(self):
    frappe.enqueue(
        self.time_taking_process,
        queue = 'short',
        timeout = 200,
        is_async = True,
    )
    frappe.msgprint('Time taking process assinged to a queue',alert=True)
