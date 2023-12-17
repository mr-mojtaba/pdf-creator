# Need to install ( pip install jinja2 )
from jinja2 import Environment, FileSystemLoader

# Need to install ( pip install jdatetime )
import jdatetime

# Need to install ( pip install pdfkit )
import pdfkit

# --------------- Variables ---------------

# Specifying the directory of the template file.
env = Environment(loader=FileSystemLoader("templates"))

# Specifying the template file.
template = env.get_template('template.html')

# Render the file.
output = template.render(name="mj")

# Creating and writing to the new file.
with open(r"templates\new-template.html", mode="w", encoding="utf-8") as tm:
    tm.write(output)
