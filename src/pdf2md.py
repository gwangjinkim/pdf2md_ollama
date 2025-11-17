import fitz  # PyMuPDF for PDFs
import ollama
import io
import argparse
from PIL import Image

def convert_pdf_to_images(pdf_path):
    images = []
    doc = fitz.open(pdf_path)  # Open the PDF
    total_pages = len(doc)
    for page_num, page in enumerate(doc, start=1):
        print(f"\rProcessing page {page_num}/{total_pages}...", end="", flush=True)
        pix = page.get_pixmap()  # Render page to pixel map
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)  # Convert to PIL image
        img_buffer = io.BytesIO()
        img.save(img_buffer, format="PNG")  # Save as in-memory PNG
        images.append(img_buffer.getvalue())  # Raw PNG bytes
    print()  # Retour à la ligne à la fin
    return images

prompt = "Extract all readable text and text chunks from this image" + \
         " and format it as structured Markdown." + \
         " Look in the entire image always and try to retrieve all text!"

def query_gemma3_with_images(image_bytes_list, model="gemma3:12b", prompt=prompt):
    response = ollama.chat(
        model=model,
        messages=[{
            "role": "user",
            "content": prompt,
            "images": image_bytes_list
        }]
    )
    return response["message"]["content"]

def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF to Markdown using pdf2md. This script extracts text from each page of a PDF and saves it as a structured Markdown file."
    )
    parser.add_argument("-p", "--pdf", required=True, help="Path to the PDF file to process")
    parser.add_argument("-o", "--output", default="output.md", help="Path to the output Markdown file (default: output.md)")
    parser.add_argument("-m", "--model", default="gemma3:12b", help="Model to use for OCR (default: gemma3:12b)")
    parser.add_argument("-pr", "--prompt", default=prompt, help="Prompt to use for text extraction (default: built-in prompt)")
    args = parser.parse_args()

    images = convert_pdf_to_images(args.pdf)
    if images:
        print(f"Converted {len(images)} pages to images.")

        extracted_text = query_gemma3_with_images(images, model=args.model)

        with open(args.output, "w", encoding="utf-8") as md_file:
            md_file.write(extracted_text)
        print(f"\nMarkdown Conversion Complete! Check `{args.output}`.")
    else:
        print("No images found in the PDF.")

if __name__ == '__main__':
    main()