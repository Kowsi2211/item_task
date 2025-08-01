import frappe

def before_install():
    if not frappe.db.exists("Item Group", "Consumable"):
        frappe.get_doc({
            "doctype": "Item Group",
            "item_group_name": "Consumable",
            "is_group": 0,
            "parent_item_group": "All Item Groups"
        }).insert(ignore_permissions=True)

    if not frappe.db.exists("UOM", "Nos"):
        frappe.get_doc({
            "doctype": "UOM",
            "uom_name": "Nos"
        }).insert(ignore_permissions=True)

    if not frappe.db.exists("Item", "Chocolate"):
        doc = frappe.new_doc("Item")
        doc.item_code = "Chocolate"
        doc.item_name = "Chocolate"
        doc.item_group = "Consumable"
        doc.stock_uom = "Nos"
        doc.is_stock_item = 1
        doc.insert(ignore_permissions=True)

        frappe.msgprint(f"Item '{doc.item_code}' is created.")

