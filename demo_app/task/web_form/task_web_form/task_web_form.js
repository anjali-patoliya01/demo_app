// frappe.ready(function() {
// 	// bind events here
// })



frappe.ready(function() {
	
	// frappe.web_form.after_load = () => {
	// 	frappe.msgprint("please fill all values carefully");
	// };

	frappe.web_form.after_load = () => {
		frappe.web_form.on('student_name', (field, value) => {
			frappe.msgprint("Hii User");
		});

		frappe.web_form.on('date_of_birth', (field, value) => {
			if(value) {
				dob = new Date(value);
				var today = new Date();
				var age = Math.floor((today-dob)/ (365.25 *24 *60 *60*1000));
				frappe.web_form.set_value('age', [age])
			}
		})
		
	}

	frappe.web_form.validate = () =>{
		email_id = frappe.web_form.get_value('email');
		var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		if(!pattern.test(email_id) && email_id){
			frappe.msgprint("Enter a valid email address");
			return false
		}

		// mobileNum = frappe.web_form.get_value('phone_no');
		// var validateMobNum = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
		// if(!validateMobNum.test(mobileNum) && mobileNum) {
		// 	frappe.msgprint('Enter a valid Mobile number');
		// 	return false;
		// }
		return true;
	}

})



