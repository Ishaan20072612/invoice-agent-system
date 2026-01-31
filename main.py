print("MAIN FILE STARTED")

from dotenv import load_dotenv
load_dotenv()

print("ENV LOADED")

from workflows.workflow import app
print("GRAPH IMPORTED")

result = app.invoke({
    "invoice_path": "data/invoices/Invoice_1_Baseline.pdf"
})

print("GRAPH INVOKED")
print(result)