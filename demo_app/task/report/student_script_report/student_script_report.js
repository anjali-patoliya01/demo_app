// Copyright (c) 2024, abc and contributors
// For license information, please see license.txt

frappe.query_reports["Student Script Report"] = {
	"filters": [
	
		   {
			"fieldname": "name",
			"label": __("Student"),
			"fieldtype": "Link",
			"options": "Student",
		},

		// {
		// 	"fieldname": "date_of_birth",
		// 	"label": __("Date Of Birth"),
		// 	"fieldtype": "Date",
		// 	// "options": "server_side_scripting",
		// },

		{
			"fieldname": "age",
			"label": __("Age"),
			"fieldtype": "Data",
		},
		// {
		// 	"fieldname": "percentage",
		// 	"label": __("Percentage"),
		// 	"fieldtype": "percent",
		// },

		{
			"fieldname": "subject_name",
			"label": __("Subject Name"),
			"fieldtype": "Data",
		},

	]
};
