// Copyright (c) 2024, abc and contributors
// For license information, please see license.txt



frappe.ui.form.on('Subject', {
   
        marks: function (frm, cdt, cdn) {
            let child = locals[cdt][cdn];
            for (let row of frm.doc.subject)
            {
                if (child.marks < 0) {
                    frappe.throw(__('Marks cannot be negative.'));
                    frappe.validated = false;
                    child.marks = null;
                    frm.refresh_field('marks');  
                    return; 
                }
            
                if (child.marks > 100) {
                    frappe.throw(__('Marks cannot be greater than 100.'));
                    frappe.validated = false;
                    child.marks = null; 
                    frm.refresh_field('marks');
                }
              
            }
        },

        on_update: function (frm) {
            percentage(frm.doc, 'on_update')
        },

        
});





frappe.ui.form.on('Student', {

    onload: function(frm) {
        if (!frm.doc.enrollment_date) {  
            frm.set_value('enrollment_date', frappe.datetime.get_today());
        }
    },


    validate: function(frm) 
    {
        if (frm.doc.date_of_birth && frm.doc.enrollment_date) 
            {
                if (frm.doc.date_of_birth === frm.doc.enrollment_date) 
                    {
                        frappe.throw(__('Enrollment date cannot be the same as birth date..!!'));
                    }
            }
    },

    date_of_birth : function(frm) {
        if (frm.doc.date_of_birth ) {
            const birthDate = new Date(frm.doc.date_of_birth );
            const today = new Date();
            let age = today.getFullYear() - birthDate.getFullYear();
            const monthDifference = today.getMonth() - birthDate.getMonth();

            if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
                age--;
            }

            frm.set_value('age', age); 
        } else {
            frm.set_value('age', null);
        }
    }

});


