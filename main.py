# Need to install ( pip install jinja2 )
from jinja2 import Environment, FileSystemLoader

# Need to install ( pip install jdatetime )
import jdatetime

# Need to install ( pip install pdfkit )
import pdfkit


order_number = input("شماره سفارش: ")
customer_name = input("نام مشتری: ")
economical_number = input("شماره اقتصادی: ")
national_code = input("کد ملی: ")
address = input("آدرس: ")
postal_code = input("کد پستی: ")
phone_number = input("شماره تلفن: ")
print(40 * "*")

number_of_products = int(input("تعداد محصولات: "))

products = []
for i in range(number_of_products):
    pr = {}
    pr["code"] = input("کد محصول: ")
    pr["name"] = input("نام محصول: ")
    pr["number"] = int(input("تعداد محصول: "))
    pr["unit"] = input("واحد: ")
    pr["unit_amount"] = int(input("مبلغ: "))
    pr["total_amount"] = pr["unit_amount"] * pr["number"]
    pr["discount"] = int(input("تخفیف: "))
    pr["discounted_amount"] = pr["total_amount"] - pr["discount"]
    pr["tax"] = int(input("مالیات بر ارزش افزوده: "))
    pr["total"] = pr["discounted_amount"] + pr["tax"]
    products.append(pr)
    print(40 * "-")

sum_total = {
    "sum_unit_amount": 0,
    "sum_total_amount": 0,
    "sum_discount": 0,
    "sum_discounted_amount": 0,
    "sum_tax": 0,
    "s_total": 0
}

for product in products:
    sum_total['sum_unit_amount'] += product['unit_amount']
    sum_total['sum_total_amount'] += product['total_amount']
    sum_total['sum_discount'] += product['discount']
    sum_total['sum_discounted_amount'] += product['discounted_amount']
    sum_total['sum_tax'] += product['tax']
    sum_total['s_total'] += product['total']

term = int(input("1-نقدی 2-اقساط: "))
terms_of_sale = "نقدی" if term == 1 else "اقساط"
description = input("توضیحات: ")

context = {
    "order_number": order_number,
    "date": jdatetime.date.strftime(jdatetime.date.today(), "%Y/%m/%d"),
    "customer_name": customer_name,
    "economical_number": economical_number,
    "national_code": national_code,
    "address": address,
    "postal_code": postal_code,
    "phone_number": phone_number,
    "products": products,
    "sum_total": sum_total,
    "terms_of_sale": terms_of_sale,
    "description": description
}

# --------------- Variables ---------------

# Specifying the directory of the template file.
env = Environment(loader=FileSystemLoader("templates"))

# Specifying the template file.
template = env.get_template('template.html')

# Render the file.
output = template.render(context=context)

# Creating and writing to the new file.
with open(r"templates\new-template.html", mode="w", encoding="utf-8") as tm:
    tm.write(output)

# Installation path of the wkhtmltopdf.
wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

# Specifying the template file path to convert to HTML.
file = r"templates\new-template.html"

# Doing wkhtmltopdf config.
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf)

# Convert html to pdf.
pdfkit.from_file(file, output_path="inv.pdf", configuration=config)
