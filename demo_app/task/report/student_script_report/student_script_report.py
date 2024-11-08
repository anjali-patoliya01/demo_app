# # # Copyright (c) 2024, abc and contributors
# # # For license information, please see license.txt

import frappe
from frappe import _
from frappe import msgprint


# ----------------------------  Show chard accroding to age  ----------------------------------------------

# def execute(filters=None):
# 	"""Return columns and data for the report.

# 	This is the main entry point for the report. It accepts the filters as a
# 	dictionary and should return columns and data. It is called by the framework
# 	every time the report is refreshed or a filter is updated.
# 	"""
# 	if not filters: 
# 		filters={}

# 	columns, data = [], []	

# 	columns = get_columns()
# 	data = get_data(filters)

# 	if not data:
# 		msgprint(_("No record found"))

# 	all_data = []
# 	for d in data:
# 		row = {
# 			'student_name': d['student_name'],
# 			# 'date_of_birth': d['date_of_birth'],
# 			'age': d['age'],
# 			# 'percentage': d['percentage'],
# 			# 'subject_name': d['subject_name']
# 		}
# 		all_data.append(row)

# 	chart = get_chart_data(all_data)
# 	report_summary = get_report_summary(all_data)

# 	return columns, all_data, None , chart, report_summary


# def get_columns():
# 	"""Return columns for the report.

# 	One field definition per column, just like a DocType field definition.
# 	"""
# 	return [
# 		{
# 			"label": _("Student Name"),
# 			"fieldname": "student_name",
# 			"fieldtype": "Data",
# 			"width" : '120'
# 		},
# 		# {
# 		# 	"label": _("Date Of Birth"),
# 		# 	"fieldname": "date_of_birth",
# 		# 	"fieldtype": "Date",
# 		# 	"width" : '120'
# 		# },
# 		{
# 			"label": _("Age"),
# 			"fieldname": "age",
# 			"fieldtype": "Data",
# 			"width" : '100'
# 		},
# 		# {
# 		# 	"label": _("Percentage"),
# 		# 	"fieldname": "percentage",
# 		# 	"fieldtype": "percent",
# 		# 	"width" : '100'
# 		# },

# 		# {
# 		# 	"label": _("Subject Name"),
# 		# 	"fieldname": "subject_name",
# 		# 	"fieldtype": "Data",
# 		# },
# 	]


# def get_data(filters) -> list[dict]:
# 	"""Return data for the report.

# 	The report data is a list of dictionaries.
# 	"""
# 	conditions = get_conditions(filters)
# 	data = frappe.get_all(
# 		doctype = 'Student',
# 		fields = ['student_name', 'age'],
# 		filters = conditions,
# 		order_by = 'student_name desc'
# 	)

# 	return data


# def get_conditions(filters):
# 	"""Return conditions based on filters."""
# 	conditions = {}
# 	for key, value in filters.items():
# 		if filters.get(key):
# 			conditions[key] = value

# 	return conditions


# def get_chart_data(all_data):
# 	"""Use to get pie chart"""

# 	if not all_data:
# 		return None

# 	# Define the chart labels
# 	labels = ['age <= 15', 'age > 15']

# 	# Initialize counters for each age group
# 	age_data = {
# 		'age <= 15': 0,
# 		'age > 15': 0,
# 	}

# 	# List to hold dataset values
# 	datasets = []

# 	# Iterate through each entry in the data
# 	for entry in all_data:
# 		age = entry['age']  # Use dictionary access
		
# 		if age is not None:
# 			age = int(age)  # Ensure the age is an integer

# 			if age <= 15:
# 				age_data['age <= 15'] += 1 
# 			else:
# 				age_data['age > 15'] += 1 

# 	# Append the dataset with correct age values
# 	datasets.append({
# 		'name': 'Age Status',
# 		'values': [age_data.get('age <= 15'), age_data.get('age > 15')]
# 	})

# 	# Construct the pie chart dictionary
# 	chart = {
# 		'data' : {
# 			'labels': labels,
# 			'datasets': datasets,
# 		},
# 		'type': 'pie',
# 		'height': 300
# 	}

# 	return chart


# def get_report_summary(all_data):
# 	if not all_data:
# 		return None

# 	age_below_15, age_above_15 = 0, 0

# 	for entry in all_data:
# 		age = entry['age']  # Use dictionary access
# 		if age is not None:
# 			age = int(age)  # Ensure the age is an integer

# 			if age <= 15:
# 				age_below_15 += 1
# 			else:
# 				age_above_15 += 1

# 	return [
# 		{
# 			'value': age_below_15,
# 			'indicator' : "Green",
# 			'label': 'Age below 15',
# 			'datatype' : 'Int',
# 		},
# 		{
# 			'value': age_above_15,
# 			'indicator' : "Red",
# 			'label' : 'Age Above 15',
# 			'datatype' : 'Int',
# 		},
# 	]


# ------------------------------------------------------------------------------------------






# -------------------------- Get subject and marks from subject child table  ---------------------

def execute(filters=None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	if not filters: 
		filters = {}

	columns, data = [], []	

	columns = get_columns()
	data = get_data(filters)

	if not data:
		msgprint(_("No record found"))

	all_data = []
	for d in data:
		# Fetch related subjects and marks from the child table for each student
		subjects = get_student_subjects(d['name'])  # Get subjects from child table

		for subject in subjects:
			row = {
				'student_name': d['student_name'],
				'age': d['age'],
				'subject_name': subject['subject_name'],  # From child table
				'marks': subject['marks']  # From child table
			}
			all_data.append(row)

	chart = get_chart_data(all_data)
	report_summary = get_report_summary(all_data)

	return columns, all_data, None, chart, report_summary


def get_columns():
	"""Return columns for the report."""
	return [
		{
			"label": _("Student Name"),
			"fieldname": "student_name",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Age"),
			"fieldname": "age",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": _("Subject Name"),
			"fieldname": "subject_name",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Marks"),
			"fieldname": "marks",
			"fieldtype": "Int",
			"width": 100
		},
	]


def get_data(filters) -> list[dict]:
	"""Return data for the report, including student details."""
	conditions = get_conditions(filters)
	data = frappe.get_all(
	'Student',
		fields=['name', 'student_name', 'age'],  # Fetch the name to link with child table
		filters=conditions,
		order_by='student_name'
	)

	return data


def get_student_subjects(student_name) -> list[dict]:
	"""Fetch subjects and marks for the given student from the child table."""
	subjects = frappe.get_all(
		doctype='Subject',  
		fields=['subject_name', 'marks'],  # Fields from child table
		filters={'parent': student_name},  # Link with the student by parent field
		order_by='subject_name'
	)

	return subjects


def get_conditions(filters):
	"""Return conditions based on filters."""
	conditions = {}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value

	return conditions


def get_chart_data(all_data):
	"""Use to generate a pie chart based on student subject marks."""

	if not all_data:
		return None

	# Define the chart labels based on marks ranges
	labels = ['Marks < 50', 'Marks 50-75', 'Marks > 75']

	# Initialize counters for each marks range
	marks_data = {
		'Marks < 50': 0,
		'Marks 50-75': 0,
		'Marks > 75': 0,
	}

	# List to hold dataset values
	datasets = []

	# Iterate through each entry in the data
	for entry in all_data:
		marks = entry['marks']  
		if marks is not None:
			marks = int(marks)  

			if marks < 50:
				marks_data['Marks < 50'] += 1
			elif 50 <= marks <= 75:
				marks_data['Marks 50-75'] += 1
			else:
				marks_data['Marks > 75'] += 1

	# Append the dataset with correct marks values
	datasets.append({
		'name': 'Marks Distribution',
		'values': [marks_data.get('Marks < 50'), marks_data.get('Marks 50-75'), marks_data.get('Marks > 75')]
	})

	# Construct the pie chart dictionary
	chart = {
		'data' : {
			'labels': labels,
			'datasets': datasets,
		},
		'type': 'pie',
		'height': 300
	}

	return chart


def get_report_summary(all_data):
	"""Generate report summary based on student subject marks."""
	if not all_data:
		return None

	# Initialize counters for each marks range
	marks_below_50, marks_50_75, marks_above_75 = 0, 0, 0

	# Iterate through each entry in the data
	for entry in all_data:
		marks = entry['marks']  # Access marks field from data

		if marks is not None:
			marks = int(marks)  

			# Categorize marks into ranges
			if marks < 50:
				marks_below_50 += 1
			elif 50 <= marks <= 75:
				marks_50_75 += 1
			else:
				marks_above_75 += 1

	# Return the summary as a list of dictionaries
	return [
		{
			'value': marks_below_50,
			'indicator': "Red",
			'label': 'Marks below 50',
			'datatype': 'Int',
		},
		{
			'value': marks_50_75,
			'indicator': "Orange",
			'label': 'Marks 50-75',
			'datatype': 'Int',
		},
		{
			'value': marks_above_75,
			'indicator': "Green",
			'label': 'Marks above 75',
			'datatype': 'Int',
		}
	]





