frappe.ui.form.on("Issue", {
	refresh: function(frm) {
		frm.add_custom_button(frappe._("View in Web Chat"), function() {
			window.open("/etms-support/ticket?name="+frm.doc.name, "_blank").focus();
		})
	}
})