

import frappe

def custom_get_requested_item_qty(sales_order):
    result = {}
    for d in frappe.db.get_all(
        "Material Request Item",
        filters={"docstatus": 1, "sales_order": sales_order},
        fields=["sales_order_item", "sum(qty) as qty", "sum(received_qty) as received_qty"],
        group_by="sales_order_item",
    ):
        result[d.sales_order_item] = frappe._dict({"qty": d.qty, "received_qty": d.received_qty})



    return result
