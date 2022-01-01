import frappe
from frappe import data_migration

def get_context(ctx):
    ctx.no_cache = 1
    frappe.only_for(['Customer'], "ETMS Support for Customers and Support Team only")

    user = frappe.get_doc("User", frappe.session.user)
    fdict = {}
    # if not user.name == "Administrator":
        # fdict['user'] = user.name

    tickets = frappe.get_all(
        "Issue",
        fields=[
            "name",
            "creation",
            "status",
            "issue_type",
            "priority",
            "customer",
            "subject",
            "company",
            "raised_by",
            "description",
        ], filters=fdict)

    ctx['company'] = frappe.defaults.get_user_default("Company")
    ctx['tickets'] = tickets