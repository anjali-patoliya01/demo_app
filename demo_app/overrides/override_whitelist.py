import frappe
import json

from erpnext.controllers.item_variant import (copy_attributes_to_variant)
from erpnext.selling.doctype.customer.customer import Customer
from frappe.utils import cstr



# @frappe.whitelist()
# def custom_create_variant(item, args, use_template_image=False):
#     frappe.msgprint('Hello...')
    
@frappe.whitelist()
def custom_create_variant(item, args, use_template_image=False):
	use_template_image = frappe.parse_json(use_template_image)
	if isinstance(args, str):
		args = json.loads(args)

	template = frappe.get_doc("Item", item)
	variant = frappe.new_doc("Item")
	variant.variant_based_on = "Item Attribute"
	variant_attributes = []

	for d in template.attributes:
		variant_attributes.append({"attribute": d.attribute, "attribute_value": args.get(d.attribute)})

	variant.set("attributes", variant_attributes)
	copy_attributes_to_variant(template, variant)

	if use_template_image and template.image:
		variant.image = template.image

	make_variant_item_code(template.item_code, template.item_name, variant)

	return variant


def make_variant_item_code(template_item_code, template_item_name, variant):
	"""Uses template's item code and abbreviations to make variant's item code"""
	if variant.item_code:
		return

	abbreviations = []
	for attr in variant.attributes:
		item_attribute = frappe.db.sql(
			"""select i.numeric_values, v.abbr
			from `tabItem Attribute` i left join `tabItem Attribute Value` v
				on (i.name=v.parent)
			where i.name=%(attribute)s and (v.attribute_value=%(attribute_value)s or i.numeric_values = 1)""",
			{"attribute": attr.attribute, "attribute_value": attr.attribute_value},
			as_dict=True,
		)

		if not item_attribute:
			continue
			# frappe.throw(_('Invalid attribute {0} {1}').format(frappe.bold(attr.attribute),
			# 	frappe.bold(attr.attribute_value)), title=_('Invalid Attribute'),
			# 	exc=InvalidItemAttributeValueError)

		abbr_or_value = (
			cstr(attr.attribute_value) if item_attribute[0].numeric_values else item_attribute[0].abbr
		)
		abbreviations.append(abbr_or_value)

	if abbreviations:
		variant.item_code = "{}/{}".format(template_item_code, "/".join(abbreviations))
		variant.item_name = "{}-{}".format(template_item_name, "-".join(abbreviations))



class CustomCustomerWhitelist(Customer):
    @frappe.whitelist()
    def get_customer_group_details(self):
        frappe.msgprint('Custom Class Whitelist Method Called.....')
        doc = frappe.get_doc("Customer Group", self.customer_group)
        self.accounts = []
        self.credit_limits = []
        self.payment_terms = self.default_price_list = ""

        fields = ["payment_terms", "default_price_list"]
        tables = {
            'accounts': ['account', 'advance_account'],
            'credit_limits': ['credit_limit', 'bypass_credit_limit_check']
        }

        for table, fields_to_update in tables.items():  
            if not doc.get(table):
                continue
            for entry in doc.get(table):
                child = self.append(table)
                for field in fields_to_update:
                    child.update({
                        "company": entry.company,
                        field: entry.get(field)
                    })

        for field in fields:
            if not doc.get(field):
                continue
            self.update({field: doc.get(field)})
        self.save()
