import pandas as pd
import random
from difflib import SequenceMatcher
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet



# ---------- Worker Agents ----------

class DataValidationAgent:
    """Validates contact info using simulated external sources"""

    def validate(self, provider):
        # Simulated lookup results
        updated_phone = provider["phone"]
        updated_address = provider["address"]

        # 20% chance phone differs
        if random.random() < 0.2:
            updated_phone = "+91" + str(random.randint(6000000000, 9999999999))

        # 10% chance address differs
        if random.random() < 0.1:
            updated_address = updated_address.replace("MG Road", "Main Street")

        return {
            "phone": updated_phone,
            "address": updated_address
        }


class InfoEnrichmentAgent:
    """Enriches provider info with specialties and license validation"""

    def enrich(self, provider):
        specialties = ["Cardiology", "General Medicine", "Orthopedics",
                       "Pediatrics", "Dermatology", "ENT", "Neurology",
                       "Gynecology", "Radiology", "Oncology"]
        enriched = {
            "specialty": random.choice(specialties),
            "license_status": random.choice(["ACTIVE", "EXPIRED", "UNKNOWN"])
        }
        return enriched


class QAAgent:
    """Cross-validates info and generates confidence scores"""

    def score(self, original, validated, enriched):
        scores = {}

        # Compare phone similarity
        phone_sim = SequenceMatcher(None, original["phone"], validated["phone"]).ratio()
        scores["phone_confidence"] = round(0.5 + 0.5 * phone_sim, 2)

        # Compare address similarity
        addr_sim = SequenceMatcher(None, original["address"], validated["address"]).ratio()
        scores["address_confidence"] = round(0.5 + 0.5 * addr_sim, 2)

        # License status confidence (higher if ACTIVE)
        scores["license_confidence"] = 0.9 if enriched["license_status"] == "ACTIVE" else 0.6

        return scores


class DirectoryManagerAgent:
    """Decides if auto-update or manual review is required"""

    def decide(self, provider, validated, enriched, scores):
        action = "AUTO-UPDATE"
        if (scores["phone_confidence"] < 0.7 or
                scores["address_confidence"] < 0.7 or
                scores["license_confidence"] < 0.7):
            action = "MANUAL-REVIEW"

        result = {
            "provider_id": provider["provider_id"],
            "name": provider["name"],
            "phone": validated["phone"],
            "address": validated["address"],
            "specialty": enriched["specialty"],
            "license_status": enriched["license_status"],
            "phone_confidence": scores["phone_confidence"],
            "address_confidence": scores["address_confidence"],
            "license_confidence": scores["license_confidence"],
            "action": action
        }
        return result


# ---------- Master Agent ----------

class MasterAgent:
    def _init_(self):
        self.validator = DataValidationAgent()
        self.enricher = InfoEnrichmentAgent()
        self.qa = QAAgent()
        self.manager = DirectoryManagerAgent()

    def process(self, provider):
        validated = self.validator.validate(provider)
        enriched = self.enricher.enrich(provider)
        scores = self.qa.score(provider, validated, enriched)
        final = self.manager.decide(provider, validated, enriched, scores)
        return final


# ---------- Run Pipeline ----------

def run_pipeline(input_csv, output_csv, report_pdf):
    df = pd.read_csv(input_csv)
    master = MasterAgent()

    results = []
    for _, row in df.iterrows():
        result = master.process(row)
        results.append(result)

    results_df = pd.DataFrame(results)
    results_df.to_csv(output_csv, index=False)
    print(f"✅ Output saved to {output_csv}")

    # Generate PDF report
    doc = SimpleDocTemplate(report_pdf, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []
    elements.append(Paragraph("Provider Data Validation Report", styles['Title']))

    table_data = [list(results_df.columns)] + results_df.head(15).values.tolist()
    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    elements.append(table)
    doc.build(elements)
    print(f"✅ Report saved to {report_pdf}")


# ---------- Main ----------

if _name_ == "_main_":
    run_pipeline(
        input_csv="synthetic_providers.csv",
        output_csv="validated_providers.csv",
        report_pdf="provider_report.pdf"
    )