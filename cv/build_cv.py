"""Build Justin Thomas CV tailored to MasTec Clean Energy & Infrastructure -
Construction Project Manager (Solar and BESS / Renewables). Outputs DOCX."""
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY = RGBColor(0x12, 0x2B, 0x4A)

CV = {
    "name": "JUSTIN THOMAS",
    "title": "Construction Project Manager — Utility-Scale Solar & Battery Energy Storage (BESS)",
    "contact": "+91 94466 74610  |  justinthomas1992@gmail.com  |  linkedin.com/in/justinthomass  |  "
               "Available for remote role with 50–60% job-site travel",
    "summary": (
        "Construction Project Manager with 11+ years in utility-scale solar and battery energy storage (BESS) "
        "construction — ~1 GWh of BESS and ~3.9 GW of solar — delivered from the EPC contractor, owner, "
        "developer and agency sides. Directs day-to-day project resources (staff, equipment, subcontractors "
        "and materials) against the Project Execution Plan; controls scope, schedule, cost, quality, risk, "
        "change and contract documents from mobilization through commissioning, handover and contract closeout. "
        "Champions safety, environmental and regulatory compliance with a Zero Injury mindset, builds a strong "
        "quality management culture, and coaches and mentors project teams. Ready to own Prevailing Wage & "
        "Apprenticeship (PWA) compliance execution in partnership with the PWA team on renewables projects "
        "supporting grid resilience and decarbonization."
    ),
    "competencies": [
        "Utility-Scale Solar & BESS Construction Management",
        "Project Execution Plan (PEP) & Resource Integration",
        "Schedule, Cost & Forecast Control",
        "Scope, Integration & Stakeholder Management",
        "Contract Documents, Change & Risk Management",
        "Subcontractor & Procurement Management (through Contract Closeout)",
        "Safety, Environmental & Regulatory Compliance (Zero Injury)",
        "Quality Management (ISO 9001:2015, QA/QC, NCR / RCA / CAPA)",
        "Coaching, Mentoring & Workforce Development",
        "Blueprint, Specification & Contract Interpretation",
        "Progress Reporting & Executive Presentations",
        "Testing, Commissioning & Handover",
    ],
    "tools": "Microsoft Office (Excel, Word, PowerPoint, Outlook), MS Project, AutoCAD, construction scheduling "
             "and document-control software, DPR / MIS reporting",
    "experience": [
        {
            "role": "Manager – Electrical Projects (EPC Contractor)",
            "org": "Amara Raja Infra Pvt. Ltd.",
            "dates": "Aug 2025 – Present",
            "project": "125 MW / 500 MWh standalone LFP BESS, Kerala, India — Owner's Engineer: Tata Consulting Engineers",
            "bullets": [
                "Direct and oversee day-to-day construction resources — site staff, equipment, subcontractors and "
                "materials — integrating activities and deliverables with the Project Execution Plan on one of "
                "India's largest BESS projects under construction.",
                "Control construction schedule and progress across containerized LFP battery systems, PCS, MV/HV "
                "balance of plant and the 145 kV grid interconnection; document and communicate progress, "
                "performance and issues to the client, Owner's Engineer and senior management.",
                "Manage subcontractor and OEM procurement interface (battery containers, PCS, transformers, MV "
                "switchgear, power cables, EMS/SCADA, UPS) — submittals, drawing approvals, pre-dispatch inspection, "
                "site acceptance and defect closure.",
                "Manage contract documents and technical risk through a 278-entry RFI register tracked to closure, "
                "resolving design and field issues before they impact schedule or cost.",
                "Drive quality management and compliance — NCR management, root cause analysis, CAPA and inspection "
                "checklists — while enforcing HSE and permit-to-work systems to keep the site audit-ready.",
                "Coach and mentor site engineers and technicians through QA/QC procedures, checklists and on-site "
                "training to build team capability.",
            ],
        },
        {
            "role": "Owner's Engineer — Quality & Construction Oversight",
            "org": "TQ Cert Services Pvt. Ltd. (Tata Projects Ltd.)",
            "dates": "Aug 2023 – Aug 2025",
            "project": "500 MW BESS + solar hybrid, Khavda, Gujarat  |  1,034 MW utility-scale solar, Jaisalmer, Rajasthan",
            "bullets": [
                "Represented the owner on two utility-scale renewables programmes, monitoring EPC contractor and "
                "subcontractor performance against scope, schedule, quality and safety commitments.",
                "Reviewed and approved contractor Quality Assurance Plans, Inspection & Test Plans, method statements "
                "and field quality procedures; enforced hold and witness points for evidence-based stage clearance.",
                "Evaluated deviation, concession and change requests on technical and contractual merit; reviewed "
                "design drawings and blueprints against specifications and standards.",
                "Performed factory acceptance testing and pre-dispatch inspection of modules, inverters, transformers, "
                "switchgear and battery systems — protecting procurement quality before materials reached site.",
                "Issued, tracked and closed NCRs and led quality audits, reporting findings and risks to owner "
                "stakeholders and top management.",
            ],
        },
        {
            "role": "Project Lead — Construction Execution (Developer / Owner)",
            "org": "Tata Power Renewable Energy Ltd.",
            "dates": "Aug 2022 – Aug 2023",
            "project": "450 MWp / 335 MWac solar, Bikaner, Rajasthan  |  300 MW solar, Dholera, Gujarat",
            "bullets": [
                "Led construction execution across ~750 MW of utility-scale solar in two states, managing EPC "
                "contractors and subcontractors against schedule, quality and safety commitments.",
                "Integrated engineering, procurement, contracts, HSE and O&M functions to resolve interface issues and "
                "keep multi-package construction sites in sequence.",
                "Governed progress through site reviews, milestone verification and punch-list closure, driving "
                "projects to commissioning and commercial operation readiness.",
                "Prepared DPR / MIS progress reports and presented schedule status, risks and issues to stakeholders "
                "and management.",
            ],
        },
        {
            "role": "Project Engineer — Implementation",
            "org": "Solar Energy Corporation of India (SECI)",
            "dates": "Oct 2020 – Aug 2022",
            "project": "2,050 MW Pavagada Solar Park, Karnataka  |  1.4 MWh island BESS, Lakshadweep",
            "bullets": [
                "Monitored developer and contractor delivery against milestones on the 2,050 MW Pavagada Solar Park, "
                "one of the world's largest solar parks.",
                "Delivered a 1.4 MWh island BESS installation, planning materials, equipment and logistics under "
                "remote, constrained site conditions.",
                "Applied tendering, contract and government-regulation knowledge to stakeholder management across "
                "developers, contractors and utilities.",
            ],
        },
        {
            "role": "Electrical Engineer — Construction Execution & O&M",
            "org": "KC Kopar Energy Solutions",
            "dates": "Jun 2015 – Oct 2020",
            "project": "25.4 MW solar, Cochin International Airport — world's first fully solar-powered airport",
            "bullets": [
                "Executed installation, testing and commissioning of 25.4 MW ground-mount, rooftop and canopy solar "
                "(modules, inverters, LT/HT switchgear, transformers, evacuation) within a live, security-controlled site.",
                "Coordinated crews, equipment and materials with airport operations to maintain jobsite safety and "
                "uninterrupted service.",
            ],
        },
    ],
    "education": [
        "B.Tech — Electrical & Electronics Engineering, SCMS School of Engineering & Technology, Cochin (2011 – 2015)",
        "Certified Lean Six Sigma Green Belt (CLSSGB)",
    ],
}


def rule(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    for k, v in (("w:val", "single"), ("w:sz", "8"), ("w:space", "1"), ("w:color", "122B4A")):
        bottom.set(qn(k), v)
    bdr.append(bottom)
    pPr.append(bdr)


def heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(text.upper())
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = NAVY
    rule(p)


def bullet(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(1)
    p.add_run(text).font.size = Pt(10)


def build(path):
    doc = Document()
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Inches(0.6)
        s.left_margin = s.right_margin = Inches(0.7)
    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(10)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(CV["name"]); r.bold = True; r.font.size = Pt(20); r.font.color.rgb = NAVY
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(CV["title"]); r.bold = True; r.font.size = Pt(11)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run(CV["contact"]).font.size = Pt(9)

    heading(doc, "Professional Summary")
    doc.add_paragraph(CV["summary"]).paragraph_format.space_after = Pt(2)

    heading(doc, "Core Competencies")
    t = doc.add_table(rows=0, cols=2)
    items = CV["competencies"]
    half = (len(items) + 1) // 2
    for i in range(half):
        row = t.add_row().cells
        for j, idx in enumerate((i, i + half)):
            if idx < len(items):
                row[j].paragraphs[0].add_run("▪ " + items[idx]).font.size = Pt(10)
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(4)
    r = p.add_run("Software: "); r.bold = True
    p.add_run(CV["tools"])

    heading(doc, "Professional Experience")
    for e in CV["experience"]:
        p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(5); p.paragraph_format.space_after = Pt(0)
        r = p.add_run(f"{e['role']}  |  {e['org']}"); r.bold = True; r.font.color.rgb = NAVY
        p.add_run(f"\t{e['dates']}").bold = True
        p.paragraph_format.tab_stops.add_tab_stop(Inches(7.1), alignment=2)
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
        r = p.add_run(e["project"]); r.italic = True; r.font.size = Pt(9.5)
        for b in e["bullets"]:
            bullet(doc, b)

    heading(doc, "Education & Certification")
    for ed in CV["education"]:
        bullet(doc, ed)

    doc.save(path)


if __name__ == "__main__":
    import sys
    build(sys.argv[1] if len(sys.argv) > 1 else "Justin_Thomas_CV_MasTec_Construction_PM_Solar_BESS.docx")
