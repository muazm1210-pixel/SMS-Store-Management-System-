from fpdf import FPDF
from products import products

bill_items = []

def add_to_bill():
    pid = int(input("Product ID: "))
    qty = int(input("Quantity: "))

    if pid in products and products[pid]["qty"] >= qty:
        item = products[pid]
        item["qty"] -= qty

        total = item["price"] * qty
        bill_items.append((item["name"], qty, total))

        print("Item added to bill!\n")
    else:
        print("Product not available!\n")


def generate_bill(shop):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, shop["shop_name"], ln=True, align="C")
    pdf.cell(200, 10, f"Owner: {shop['owner']}", ln=True)
    pdf.cell(200, 10, f"Phone: {shop['phone']}", ln=True)
    pdf.ln(10)

    total_amount = 0
    for name, qty, total in bill_items:
        pdf.cell(200, 10, f"{name} x {qty} = Rs {total}", ln=True)
        total_amount += total

    pdf.ln(5)
    pdf.cell(200, 10, f"TOTAL: Rs {total_amount}", ln=True)

    pdf.output("bill.pdf")
    print("Bill generated: bill.pdf\n")