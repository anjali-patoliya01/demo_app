Custom = False 
frappe.listview_settings['Student'] = {
    onload(listvew) { 
        frappe.msgprint("List: Hello from Doctype list JS");

    }
};

