# Convert PDFs to Markdown with Local LLMs

Fast, private, and free PDF-to-Markdown conversion using a local LLM (e.g., Gemma 3 via Ollama). No cloud APIs, no tokens, no privacy concerns — just elegant Python.

**Article**: [Convert PDFs to Markdown using Local LLMs — Fast, Private, and Free](https://medium.com/data-science-collective/convert-pdfs-to-markdown-using-local-llms-c5232f3b50fc?sk=9b0036a7ff93a1c48bae7dd8216dc671)

---

## Installation (Option 1: Using [uv](https://github.com/astral-sh/uv))

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
uv pip install -r requirements.txt
```
Then run:
```bash
uv run src/pdf2md.py
```

## Installation (Option 2: Using pip)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Then run:
```bash
python src/pdf2md.py
```

## Installation (Option 3: Using conda)

```bash
conda env create -f pdf2md.yaml -p  ~/envs/pdf2md
```

Then run:
```bash
conda activate ~/envs/pdf2md
python src/pdf2md.py -p mypdf.pdf -m gemma3:12b -o output.md
```

---

## Dependencies

- PyMuPDF (for PDF rendering) — not free for commercial use
- Pillow
- Ollama, for Ollama use `curl -fsSL https://ollama.com/install.sh | sh` and the `ollama run gemma3:12b`
- A local model like gemma3:12b or gemma3:4b must be installed and pulled

---

## Alternative: Fully Open Source Version

Use `pdf2image` + `Poppler` instead of `pymupdf`.

```bash
brew install poppler  # or sudo apt install poppler-utils
pip install pdf2image pillow ollama
```
Then run:
```bash
python src/pdf2md_poppler.py
```

---

## Features

- Handles scanned PDFs via image input
- Converts to clean, structured Markdown
- Works offline with local models

---

## Convert pdf to image

```bash
pip install pdf2image
brew install poppler    # or in Linux: sudo apt install poppler-utils
```
