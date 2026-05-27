# Multi-Agent Invoice Reconciliation System

A production-grade multi-agent system that autonomously processes supplier invoices, matches them against purchase orders, detects discrepancies, and recommends resolution actions — all orchestrated via an agentic workflow.

---

## Architecture

```
Invoice PDF
     |
     v
Document Intelligence Agent   ← PDF extraction + OCR fallback (Tesseract)
     |
     v
Matching Agent                ← Matches invoice to PO database
     |
     v
Discrepancy Detection Agent   ← Detects price/quantity/item mismatches
     |
     v
Resolution Agent              ← Recommends: auto-approve / review / escalate
```

---

## Agents

| Agent | Responsibility |
|-------|---------------|
| **Document Intelligence** | Extracts text from PDFs via pdfplumber; falls back to Tesseract OCR for scanned/rotated invoices |
| **Matching** | Matches invoices to PO database with fallback logic for missing PO references |
| **Discrepancy Detection** | Flags item, quantity, and price mismatches including hidden price increases |
| **Resolution** | Recommends auto-approve, manual review, or escalation based on confidence scores |

---

## Features

- Non-linear agent orchestration via LangGraph
- Confidence-aware decision making at every stage
- Handles both clean and scanned invoices
- Explainable outputs — every agent appends its decision and confidence to shared state
- 5 sample invoice PDFs included for testing (baseline, scanned, different format, price trap, missing PO)

---

## Project Structure

```
├── agents/
│   ├── document_agent.py       # PDF extraction + OCR
│   ├── matching_agent.py       # PO matching
│   ├── discrepancy_agent.py    # Mismatch detection
│   └── resolution_agent.py     # Final recommendation
├── data/
│   ├── invoices/               # Sample invoice PDFs
│   └── purchase_orders.json    # PO database
├── utils/
│   ├── ocr.py                  # Tesseract OCR wrapper
│   ├── pdf_utils.py            # PDF helpers
│   ├── basic_field_parser.py   # Field extraction
│   ├── line_item_parser.py     # Line item parsing
│   └── text_parser.py          # Text processing
├── workflows/
│   └── workflow.py             # LangGraph orchestration
├── main.py                     # Entry point
└── requirements.txt
```

---

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Install Tesseract OCR (for scanned invoices)
```bash
# macOS
brew install tesseract

# Ubuntu
sudo apt-get install tesseract-ocr
```

### 3. Run
```bash
python main.py
```

The system will process `data/invoices/Invoice_1_Baseline.pdf` by default. Change the `invoice_path` in `main.py` to test other invoices.

---

## Sample Invoices

| File | Test Case |
|------|-----------|
| `Invoice_1_Baseline.pdf` | Clean, standard format |
| `Invoice_2_Scanned.pdf` | Scanned — tests OCR fallback |
| `Invoice_3_Different_Format.pdf` | Non-standard layout |
| `Invoice_4_Price_Trap.pdf` | Hidden price increase |
| `Invoice_5_Missing_PO.pdf` | Missing PO reference |

---

## Tech Stack

| Library | Purpose |
|---------|---------|
| `langgraph` | Agent orchestration |
| `pdfplumber` | PDF text extraction |
| `pytesseract` | OCR for scanned invoices |
| `python-dotenv` | Environment config |

---

## Author

Ishaan Chowdhury · [@Ishaan20072612](https://github.com/Ishaan20072612)
