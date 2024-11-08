// Copyright (c) 2024, abc and contributors
// For license information, please see license.txt





// // // Frppe frm_call method from server side
// frappe.ui.form.on("Server Side Scripting", {
//     is_prasent: function(frm) {
//         frm.call({
//         doc: frm.doc,
//         method : 'frm_call',
//         args : {
//             msg: 'Hello'
//         },
//         freeze : true,
//         freeze_message : __('Calling frm_call Method'),
//         callback: function(r) {
//             frappe.msgprint(r.message)

//             // frappe.msgprint('Server side calling compleated')
//             // frm.refresh_field('madication_order')

//         }
//         });
//     }




frappe.ui.form.on("server_side_scripting", {
    is_prasent: function(frm) {
        frappe.call({
        // doc: frm.doc,/
        method : 'demo_app.task.doctype.client_side_scripting.client_side_scripting.frappe_call',
        args : {
            msg: 'Hello'
        },
        freeze : true,
        freeze_message : __('Calling frm_call Method'),
        callback: function(r) {
            frappe.msgprint(r.message)

        }
        });
    }

});

