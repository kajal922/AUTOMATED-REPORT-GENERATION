# Step 3a: Import libraries
import pandas as pd
from fpdf import FPDF

# Step 3b: Read CSV
df = pd.read_csv("data.csv")

# Step 3c: Analyze Data
avg_temp = df['Temperature'].mean()
max_temp = df['Temperature'].max()
min_temp = df['Temperature'].min()
weather_counts = df['Weather'].value_counts()

# Step 3d: Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

# Title
pdf.cell(0, 10, "Weather Report", ln=True, align='C')

# Step 3e: Add summary
pdf.set_font("Arial", '', 12)
pdf.ln(10)
pdf.cell(0, 10, f"Average Temperature: {avg_temp:.2f}°C", ln=True)
pdf.cell(0, 10, f"Max Temperature: {max_temp}°C", ln=True)
pdf.cell(0, 10, f"Min Temperature: {min_temp}°C", ln=True)

# Weather type frequency
pdf.ln(5)
pdf.cell(0, 10, "Weather Type Frequency:", ln=True)
for weather, count in weather_counts.items():
    pdf.cell(0, 10, f"{weather}: {count}", ln=True)

# Step 3f: Save PDF
pdf.output("Weather_Report.pdf")
