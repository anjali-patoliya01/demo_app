import frappe
from erpnext.buying.doctype.purchase_order.purchase_order import PurchaseOrder

class CustomPurchaseOrder(PurchaseOrder):
    def validate(self):
        super(CustomPurchaseOrder, self).validate() 
        self.status = 'On Hold'
        



