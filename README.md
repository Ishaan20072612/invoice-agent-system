# Multi-Agent Invoice Reconciliation System

## Overview
This project implements a multi-agent invoice reconciliation system using an agentic architecture.
The system processes supplier invoices, extracts structured data, matches against purchase orders,
detects discrepancies, and recommends resolution actions.

## Agent Architecture

### 1. Document Intelligence Agent
- Extracts text from PDFs using pdfplumber
- Falls back to OCR (Tesseract) for scanned/rotated invoices
- Outputs extraction confidence and OCR usage flag

### 2. Matching Agent
- Matches invoices to PO database
- Handles missing PO references using fallback logic
- Outputs match confidence

### 3. Discrepancy Detection Agent
- Detects item, quantity, and price mismatches
- Flags anomalies (e.g., hidden price increases)
- Produces structured discrepancy reports

### 4. Resolution Agent
- Recommends auto-approve, manual review, or escalation
- Decision based on discrepancies and confidence scores

## Key Features
- Agent-based (non-linear) orchestration
- Confidence-aware decision making
- Works with clean and scanned invoices
- Explainable agent outputs

## How to Run
```bash
python3.11 -m pip install -r requirements.txt
python3.11 main.py

## Explainability
Each agent appends its decision and confidence to a shared state.
The final resolution decision is derived from:
- Extraction confidence
- PO matching confidence
- Number and severity of discrepancies

All agent outputs are printed for transparency and debugging.
