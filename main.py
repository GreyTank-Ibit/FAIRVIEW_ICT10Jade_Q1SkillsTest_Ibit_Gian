from pyscript import display, document

def confirm_info(e):
    customer_name = document.getElementById("input1").value
    requested_items = document.getElementById("input2").value
    display(f"Customer Name: {customer_name}")
    display(f"Requested Items: {requested_items}")

def create_order (e):
    customer_name = document.getElementById("input1").value
    requested_items = document.getElementById("input2").value
    display(f"Order Created for {customer_name} with items: {requested_items}")
    document.getElementById("output1").innerHTML = " "

def show_order (e):
    customer_name = document.getElementById("input1").value
    requested_items = document.getElementById("input2").value
    display(f"Order Details: Customer Name: {customer_name}, Requested Items: {requested_items}")