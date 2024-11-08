// Copyright (c) 2024, abc and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Client Side Scripting", {

    // -------------------------------------------  EVENT  ------------------------------------------- 
    
	// refresh(frm) {
    //     frappe.msgprint("Hello from 'refresh' event")
	// },


    //  onload(frm){
    //             frappe.msgprint("Hello from 'onload' event")
    // },


    // validate(frm){
    //             frappe.throw("Hello from 'validate' event")
    // },



    // before_save(frm){
    //             frappe.throw("Hello from 'Before save' event")
    // },


    // after_save(frm){
    //         frappe.msgprint("Hello from 'after save' event")
    // },


    // is_present(frm){
    //         frappe.msgprint("Hello from  'Is Present' fieldname event")
    // },


    // roll_no: function(frm){
    //         frappe.msgprint("Hello from  'roll number' fieldname event")
    // },



    // before_submit: function(frm){
    //         frappe.throw("Hello from  'before_submit' event")
    // },



    // on_submit: function(frm){
    //         frappe.msgprint("Hello from  'on_submit'  event")
    // },



    // before_cancel: function(frm){
    //         frappe.throw("Hello from  'before_cancel' event")
    // },



    // after_cancel: function(frm){
    //         frappe.msgprint("Hello from  'after_cancel' event")
    // },





    // -------------------------------------------- Fatching Value -------------------------------
    // after_save: function(frm) {
    //                 // Display the full name of the student
    //                 // frappe.msgprint(__("The full name is '{0}'", 
    //                 //     [frm.doc.first_name + " " + frm.doc.last_name]
    //                 // ));
                    
    //                 // Check if the subject field exists and is an array
    //                 if (frm.doc.result && frm.doc.result.length > 0) {
    //                     frm.doc.result.forEach(row => {
    //                         frappe.msgprint(__("{0}. The Student Result for Semester '{1}'  is '{2}'", 
    //                             [row.idx, row.semester, row.spi]
    //                         ));
    //                     });
    //                 } else {
    //                     frappe.msgprint(__('No Result found.'));
    //                 }
    //             },

            

    
    // ----------------------------------------------- frm.set_intro & frm.is_new()  ----------------------------------------------- 
    // refresh:function(frm){
    //             frm.set_intro("Now you can create a new Client side Scripting doctype")  
                
    //                     // if(frm.is_new()){
    //                     //         frm.set_intro("Now you can create a new Client side Scripting doctype")       
    //                     // }
    //             }



    // -----------Query on this--------------------------------------- frm.set_value & frm.add_child  --------------------------------------------------  

    // validate:function(frm){
    //     // ------- autometic fill full name field (read only) --------
    //     // frm.set_value("full_name",frm.doc.first_name +"  "+ frm.doc.last_name) 
    
    //     let row = frm.add_child('student_result', {
    //         semester: '1st',
    //         spi:8.69,
    //         })
    //     },
    // ------------------------------------------------------------------------------------



    // ------------------------------------- frm.set_df_property   ------------------------------
    // is_present:function(frm){
    //     frm.set_df_property('roll_no','reqd', 1)
        
    //     frm.set_df_property('last_name','read_only', 1)
        
    //     frm.toggle_reqd('phone',true)
    // }

    // ----------------------------------------------------------------------------------------




    // --------------------------------- Button ------------------------------------------------
    // refresh:function(frm){
    //     // frm.add_custom_button('Click Me Button',() =>{
    //     //     frappe.msgprint(__("You Clicked Me!!"))
    //     // }) 
                       
    //     frm.add_custom_button("Click me1", () =>{
    //         frappe.msgprint(__('You Clicked 1 !!'))
    //     }, 'click me')
        
    //     frm.add_custom_button("Click me2", () =>{
    //         frappe.msgprint(__('You Clicked 2 !!'))
    //     }, 'click me')
        
    // }
    
                
	
// });










 // ---------------------------------------- Child Table Event ----------------------------------

// frappe.ui.form.on("Subject", {

//         // subject_name(frm){
//         //         frappe.msgprint("Hello from Child DocType 'Subject' event")
//         // },

//         /* cdt = Child DocType name i.e Family_members
//            cdn = row name   
//         */

//         marks(frm,cdt, cdn){
//                 frappe.msgprint("Hello from 'Subject' Child DocType fieldname event")
//         }

// });









    
