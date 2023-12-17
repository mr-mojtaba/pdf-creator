# Need to install ( pip install jinja2 )
from jinja2 import Environment, FileSystemLoader

# Need to install ( pip install jdatetime )
import jdatetime

# Need to install ( pip install pdfkit )
import pdfkit


order_number = input("Order Number: ")

context = {
    "order_number": order_number,
    "date": jdatetime.date.strftime(jdatetime.date.today(), "%Y/%m/%d")

}

# --------------- Variables ---------------

# Specifying the directory of the template file.
env = Environment(loader=FileSystemLoader("templates"))

# Specifying the template file.
template = env.get_template('template.html')

# Render the file.
output = template.render(name="mj")

# Creating and writing to the new file.
with open(r"templates/template.html", mode="w", encoding="utf-8") as tm:
    tm.write(output)

# Installation path of the wkhtmltopdf.
wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

# Specifying the template file path to convert to HTML.
file = r"templates/template.html"

# Doing wkhtmltopdf config.
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf)

# Convert html to pdf.
pdfkit.from_file(file, output_path="inv.pdf", configuration=config)
