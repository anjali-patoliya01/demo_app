# Copyright (c) 2024, abc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student(Document): 
    def validate(self):
        total_marks = 0
        subject_count = 0
        
        for row in self.get('subject'):
            if row.marks == None:
                frappe.throw('Please Enter Mark..')
            total_marks += row.marks
            subject_count += 1
            

        #  Calculate Precentage
        self.total_marks = total_marks
        self.max_marks = subject_count * 100  

        if self.max_marks > 0:
            self.percentage = (self.total_marks / self.max_marks) * 100
        else:
            self.percentage = 0

        
        # # Update status based on percentage
        # if self.percentage < 33:
        #     self.status = "Failed"
        #     self.grade = 'C'

        # elif 33 <= self.percentage <= 40:
        #     self.status = "Pass"
        #     self.grade = 'B'

        # elif 40 <= self.percentage <= 50:
        #     self.status = "Pass"
        #     self.grade = 'B+'

        # elif 50 <= self.percentage <= 70:
        #     self.status = "Average"
        #     self.grade = 'A'

        # else:
        #     self.status = "Excellent"
        #     self.grade = "A+"



    def set_default_date(doc, method):
        if not doc.enrollment_date:  
            doc.enrollment_date = frappe.utils.nowdate()

    
    

		



