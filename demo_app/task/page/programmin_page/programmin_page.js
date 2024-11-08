frappe.pages['programmin-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Demo Page',
		single_column: true
	});

	page.set_title('My Page')
	page.set_indicator('Done', 'green')


	let $btn = page.set_primary_action('Click', ()=> frappe.msgprint('Clicked New'), 'acticon octicon-plus')
	let $btnOne = page.set_secondary_action('Refresh', ()=> frappe.msgprint('Clicked Refresh'), 'acticon octicon-plus')
	page.add_menu_item('Send Email', () => frappe.msgprint("Clicked send Email"))
	page.add_action_item("Delete", () => frappe.msgprint('Clicked Delete'))

	// ------------------ add option menu ------------------  //
	let field = page.add_field( {
		lable : 'Status',
		fieldtype : 'Select',
		fieldname : "staus",
		options : [
			'Open',
			'Closed',
			'Cancelled'
		],
		change(){
			frappe.msgprint(field.get_value());
		}
	});


// // ------------------ Render HTML Page ------------------  //
	$(frappe.render_template('programming_page',{})).appendTo(page.body);

// // ------------------- this msg show through HTML page  ------------------- 
	$(frappe.render_template('programming_page', {
		data : "Hii Frappe"
	})).appendTo(page.body)


	 // Include the CSS file
	 $('<link>', {
        rel: 'stylesheet',
        type: 'text/css',
        href: 'programming_pagesx/programming_page.css'
    }).appendTo('head');
}




