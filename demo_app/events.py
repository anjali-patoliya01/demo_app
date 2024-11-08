from demo_app.task.doctype.student.student import Student
import frappe


def update_status_based_on_percentage(self,method):            
    print('\n\n\n    Overried Student Method   \n\n\n')
    if self.percentage is None:
        self.percentage = 0 

    if self.percentage < 33:
        self.status = "Failed"
        self.grade = 'C'

    elif 33 <  self.percentage <= 40:
        self.status = "Pass"
        self.grade = 'B'

    elif 40 < self.percentage <= 50:
        self.status = "Pass"
        self.grade = 'B+'

    elif 50 < self.percentage <= 70:
        self.status = "Average"
        self.grade = 'A'
            
    else:
        self.status = "Excellent"
        self.grade = "A+"

    # frappe.msgprint(f"Calculated Percentage: {self.percentage:.2f}% - Status Updated to: {self.status}")







