import os
import csv
import qrcode
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader  # ✅ Required for in-memory image
from io import BytesIO

# ==== Configuration ====
CERT_FOLDER = "C:\\Users\\DELL\\Desktop\\web\\cipher_qr_generator\\certificates"         # Input folder
OUTPUT_FOLDER = "C:\\Users\\DELL\\Desktop\\web\\cipher_qr_generator\\certificates_qr"    # Output folder
CSV_FILE = "C:\\Users\\DELL\\Desktop\\web\\cipher_qr_generator\\data.csv"                # Data file
BASE_URL = "https://cipher25-eight.vercel.app/verify.html?cert="

# Make output folder if not exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load CSV and process each certificate
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        file_name = row["File Name"]
        cert_id = row["Certificate ID"]

        cert_path = os.path.join(CERT_FOLDER, file_name)
        if not os.path.exists(cert_path):
            print(f"❌ File not found: {file_name}")
            continue

        # ==== Create QR Code ====
        qr_link = BASE_URL + cert_id
        qr = qrcode.make(qr_link)
        qr_io = BytesIO()
        qr.save(qr_io, format='PNG')
        qr_io.seek(0)

        # ==== Create overlay with QR ====
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=A4)
        x = 10 * mm   # X position (right side)
        y = 230 * mm    # Y position (bottom side)
        qr_image = ImageReader(qr_io)  # ✅ Convert BytesIO to ImageReader
        can.drawImage(qr_image, x, y, width=30*mm, height=30*mm)
        can.save()
        packet.seek(0)

        # ==== Merge overlay with original PDF ====
        overlay = PdfReader(packet)
        original = PdfReader(cert_path)
        writer = PdfWriter()

        for i in range(len(original.pages)):
            page = original.pages[i]
            if i < len(overlay.pages):
                page.merge_page(overlay.pages[i])
            writer.add_page(page)

        output_path = os.path.join(OUTPUT_FOLDER, file_name)
        with open(output_path, "wb") as f_out:
            writer.write(f_out)

        print(f"✅ QR added: {file_name}")
