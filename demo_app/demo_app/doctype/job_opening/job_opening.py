# Copyright (c) 2024, abc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator
from frappe import _


# class jobopening(Document):
# 	pass



# subclass from WebsiteGenerator, not Document
class  jobopening(WebsiteGenerator):
    website = frappe._dict(
        template = "templates/generators/job_opening.html",
        condition_field = "published",
        page_title_field = "job_title",
    )

    def get_context(self, context):
        # show breadcrumbs
        context.parents = [{'name': 'jobs', 'title': _('All Jobs') }]
        
    def get_list_context(context):
        context.title = _("Jobs")
        context.introduction = _('Current Job Openings')


