from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
import os

def make_receipt(data, payment_method, out_file_name, customer_name=None, customer_id=None, total_orders=None):
    # Creating a Base Document Template of page size A4
    pdf = SimpleDocTemplate(out_file_name, pagesize=A4)

    # Standard stylesheet defined within reportlab itself
    styles = getSampleStyleSheet()

    # Fetching the style of Top level heading (Heading1)
    title_style = styles["Heading1"]

    # Setting alignment
    title_style.alignment = 1

    # Creating the paragraph with the heading text and passing the styles of it
    title_text = f"Dessert Shop Receipt\nPayment Method: {payment_method}\nCustomer Name: {customer_name}\nCustomer ID: {customer_id}\nTotal Orders: {total_orders}"
    title = Paragraph(title_text, title_style)

    # Creating Table Style object
    style = TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (2, len(data)), 1, colors.black),
            ("BACKGROUND", (0, 0), (2, 0), colors.gray),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ]
    )

    # Creating a table object and passing the style to it
    table = Table(data, style=style)

    # Building the actual pdf putting together all the elements
    pdf.build([title, table])

def main():
    # Data for the receipt
    data = [
        ["Name", "Item Cost", "Tax"],
        ["Candy Corn", "$0.38", "$0.03"],
        ["Gummy Bears", "$0.09", "$0.01"],
        ["Chocolate Chip", "$2.00", "$0.14"],
        ["Pistachio", "$1.58", "$0.11"],
        ["Vanilla", "$3.36", "$0.24"],
        ["Oatmeal Raisin", "$0.57", "$0.04"],
        ["--------------------------------------------------------", "", ""],
        ["Order Subtotals", "$7.97", "$0.58"],
        ["Order Total", "", "$8.55"],
        ["Total items in the order", "", "6"]
    ]

    # Payment method for the receipt
    payment_method = "CASH"

    # Customer information
    customer_name = "Apollo"
    customer_id = "1000"
    total_orders = "1"

    # Output file name for the receipt
    out_file_name = "dessert_receipt.pdf"

    # Calling make_receipt with the provided data, payment method, customer information, and output file name
    make_receipt(data, payment_method, out_file_name, customer_name, customer_id, total_orders)

if __name__ == "__main__":
    main()