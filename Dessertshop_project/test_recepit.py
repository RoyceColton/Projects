from receipt import make_receipt

data = [
    ["Name", "Item Cost", "Tax"],
    ["Candy Corn", "$0.38", "$0.03"],
    ["Gummy Bears", "$0.09", "$0.01"],
    # Add more rows as needed
]

payment_method = "CASH"
customer_name = "Apollo"
customer_id = "1000"
total_orders = "1"

out_file_name = "receipt.pdf"

make_receipt(data, payment_method, out_file_name, customer_name, customer_id, total_orders)
