import requests
from openpyxl import Workbook
import smtplib
from email.mime.text import MIMEText

# ==============================
# STEP 1: FETCH JOB DATA
# ==============================

url = "https://remoteok.com/api"
response = requests.get(url)
jobs = response.json()

# ==============================
# STEP 2: FILTER KEYWORDS
# ==============================

keywords = ["python", "ai", "machine learning", "data", "automation"]

# ==============================
# STEP 3: CREATE EXCEL FILE
# ==============================

wb = Workbook()
sheet = wb.active
sheet.title = "AI Jobs"

# Headers
sheet.append(["Position", "Company"])

print("🔥 AI / PYTHON JOBS:\n")

# ==============================
# STEP 4: PROCESS JOBS
# ==============================

for job in jobs[1:]:
    title = str(job.get("position")).lower()
    company = job.get("company")

    if any(word in title for word in keywords):
        print("✅", job.get("position"), "-", company)
        sheet.append([job.get("position"), company])

# Save Excel
wb.save("ai_jobs.xlsx")
print("\n📊 Saved to ai_jobs.xlsx")

# ==============================
# STEP 5: SEND EMAIL ALERT
# ==============================

# 👉 CHANGE THESE DETAILS
sender = "cdawoodshareef@gmail.com"
password = "uukcxyeyxxfmfrma"
receiver = "cdawoodshareef@gmail.com"

# Email content
msg = MIMEText("🔥 New AI Jobs Found!\nCheck attached Excel file (ai_jobs.xlsx).")
msg["Subject"] = "AI Job Alert"
msg["From"] = sender
msg["To"] = receiver

print("📧 Sending email...")

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()
    print("✅ Email sent successfully!")

except Exception as e:
    print("❌ Email error:", e)