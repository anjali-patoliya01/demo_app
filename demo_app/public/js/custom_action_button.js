// ----------------------- not working -------------------------------

// frappe.ui.form.on('Customer', {
//     refresh: function(frm) {
//         // Hide the action button in the Customer Doctype after saving
//         frm.page.clear_actions_menu();
//     }
// });



// frappe.ui.form.on('Customer', {
// 	refresh: function(frm) {
//         console.log('\n\n\n------------- Override Method ------------\n\n\n')
// 	    setTimeout(() => {
// 	        frm.page.actions.find('[data-label="Actions"]').remove();
// 	    }, 500);
// 	}
// });


// -----------------------------------------------------------------------



// frappe.ui.form.on('Customer', {
//     refresh: function(frm) {
        // Hide the action button in the Customer Doctype after saving
        // frm.page.remove_inner_button(__('Get Customer Group Details'),__('Actions'));


        // frm.page.remove_inner_button(__('Pricing Rule'),__('Create'));
        // frm.page.remove_inner_button(__('Accounts Receviable'),__('Accounting ledger'),__('View'));
        
        // console.log('\n\n\n------------- Override Method ------------\n\n\n')
//     }
// });






