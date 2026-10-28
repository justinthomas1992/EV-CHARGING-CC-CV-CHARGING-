import sys
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = sys.argv[1]
NAVY = RGBColor(0x12, 0x3A, 0x5E)
GREY = RGBColor(0x55, 0x55, 0x55)

def base(doc):
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Cm(1.5)
        s.left_margin = s.right_margin = Cm(1.8)
    st = doc.styles["Normal"]
    st.font.name = "Calibri"; st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    st.paragraph_format.space_after = Pt(2)

def rule(p):
    pPr = p._p.get_or_add_pPr()
    b = OxmlElement("w:pBdr"); bot = OxmlElement("w:bottom")
    for k, v in (("val", "single"), ("sz", "8"), ("space", "1"), ("color", "123A5E")):
        bot.set(qn("w:" + k), v)
    b.append(bot); pPr.append(b)

def heading(doc, text):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(3)
    r = p.add_run(text.upper()); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAVY
    rule(p)

def bullet(doc, text, bold_lead=None):
    p = doc.add_paragraph(style="List Bullet"); p.paragraph_format.space_after = Pt(1)
    if bold_lead:
        p.add_run(bold_lead).bold = True
    p.add_run(text)

def header_block(doc, subtitle):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
    r = p.add_run("JUSTIN THOMAS"); r.bold = True; r.font.size = Pt(20); r.font.color.rgb = NAVY
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
    r = p.add_run(subtitle); r.bold = True; r.font.size = Pt(11)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Hyderabad, India (open to relocation – Rajasthan / pan-India)  |  +91 94466 74610  |  "
                  "justinthomas1992@gmail.com  |  linkedin.com/in/justinthomass")
    r.font.size = Pt(9.5); r.font.color.rgb = GREY
    rule(p)

def role(doc, title, org, dates, project, bullets):
    t = doc.add_table(rows=1, cols=2); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    t.columns[0].width = Cm(13.4); t.columns[1].width = Cm(4)
    c0, c1 = t.rows[0].cells
    c0.width = Cm(13.4); c1.width = Cm(4)
    p = c0.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
    r = p.add_run(title); r.bold = True; r.font.color.rgb = NAVY
    p.add_run("  |  " + org).bold = True
    p = c1.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.RIGHT; p.paragraph_format.space_after = Pt(0)
    r = p.add_run(dates); r.italic = True; r.font.color.rgb = GREY
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(1)
    r = p.add_run(project); r.italic = True; r.font.size = Pt(9.5); r.font.color.rgb = GREY
    for b in bullets:
        bullet(doc, b)

# ---------------- CV ----------------
cv = Document(); base(cv)
header_block(cv, "Site Construction Head – Utility-Scale Renewable Power Projects  |  Solar · BESS · HV Balance of Plant")

heading(cv, "Professional Summary")
cv.add_paragraph(
    "Renewable-energy construction leader with 11+ years delivering utility-scale power assets – ~3.9 GW of solar and "
    "~1 GWh of battery storage – through site execution, contractor management, QA/QC, EHS, testing, commissioning and "
    "handover. Has run civil, mechanical and electrical site packages, multi-contractor balance-of-plant (BOP) works and "
    "the 145 kV grid-evacuation interface that every wind farm shares. Brings recent Rajasthan site experience on the "
    "1,034 MW Siyambar / Bandha programme in Jaisalmer district and 450 MWp in Bikaner, and has seen projects from all four "
    "sides of the contract – EPC contractor, Owner's Engineer, IPP / developer and government agency – so understands "
    "what the client, the Owner's Engineer and the contractor each need to close a milestone. Certified Lean Six Sigma "
    "Green Belt; known for building site systems that are safe, auditable and right first time."
).paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

heading(cv, "Core Competencies – Mapped to the Role")
comp = [
    ("Site Construction Leadership: ", "civil foundations, mechanical erection and electrical works on multi-package utility-scale sites"),
    ("EHS & Compliance: ", "zero-incident focus, permit-to-work, HSE governance, monsoon / weather-readiness planning, IEC / IEEE standards"),
    ("Contractor & Vendor Management: ", "EPC contractors, subcontractors and OEMs; drawing approvals, FAT / PDI, site acceptance, defect closure"),
    ("Schedule & Progress Control: ", "MS Project scheduling, milestone verification, DPR / MIS reporting, punch-list closure to COD"),
    ("Quality Assurance / Control: ", "ISO 9001:2015, QAP / ITP, field quality plans, hold & witness points, NCR / RCA / CAPA"),
    ("Grid Connection & BOP: ", "pooling substations, 33 kV HT panels, power transformers, 145 kV switchyard and evacuation systems"),
    ("Stakeholders & Risk: ", "client, Owner's Engineer, local authorities and community interface; technical, safety and schedule risk mitigation"),
    ("People: ", "site team leadership, training and capability building; English, Hindi, Malayalam, Tamil"),
]
for lead, txt in comp:
    bullet(cv, txt, lead)

heading(cv, "Project Portfolio – ~3.9 GW Solar | ~1 GWh BESS")
rows = [
    ("Project", "Capacity", "Location", "Role"),
    ("JSW Renew Energy 38L – standalone LFP BESS", "125 MW / 500 MWh", "Kasaragod, Kerala", "EPC Contractor"),
    ("Khavda BESS + solar hybrid", "500 MW", "Khavda, Gujarat", "Owner's Engineer / TPI"),
    ("Siyambar / Bandha solar", "1,034 MW", "Jaisalmer, Rajasthan", "Owner's Engineer / TPI"),
    ("TP Solapur solar", "450 MWp / 335 MW AC", "Bikaner, Rajasthan", "IPP / Developer"),
    ("Dholera solar", "300 MW", "Dholera, Gujarat", "IPP / Developer"),
    ("Pavagada Solar Park", "2,050 MW", "Tumakuru, Karnataka", "Implementing Agency"),
    ("Lakshadweep island BESS", "1.4 MWh", "Lakshadweep, UT", "Implementing Agency"),
    ("Cochin International Airport solar", "25.4 MW", "Kochi, Kerala", "Execution & O&M"),
]
t = cv.add_table(rows=len(rows), cols=4); t.style = "Light Grid Accent 1"
for i, row in enumerate(rows):
    for j, v in enumerate(row):
        cell = t.cell(i, j); cell.text = ""
        r = cell.paragraphs[0].add_run(v); r.font.size = Pt(9); r.bold = (i == 0)

heading(cv, "Professional Experience")
role(cv, "Senior Manager – Electrical Projects", "Amara Raja Infra Pvt. Ltd.", "Aug 2025 – Present",
     "JSW Renew Energy 38L – 125 MW / 500 MWh standalone LFP BESS, Kasaragod, Kerala · EPC scope · TCE as Owner's Engineer",
     ["Leads electrical project delivery and site QA/QC for one of India's largest storage assets under construction – "
      "containerised battery systems, PCS, MV / HV balance of plant and the 145 kV evacuation interface.",
      "Coordinates the OEM and vendor interface across Gotion, Hopewind, Shilchar, Trisquare, CG Power, KEC, Smart Grid "
      "and Fuji Electric – drawing approvals, pre-dispatch inspection, site acceptance and defect closure.",
      "Set up the site quality-control regime: RFI register with 278 entries tracked to closure, NCR / observation "
      "management, RCA and CAPA reporting, and post-pour foundation inspection checklists for civil works.",
      "Keeps the site audit-ready for the Owner's Engineer and the client, with work sequenced across civil, "
      "mechanical and electrical packages."])
role(cv, "Manager – Owner's Engineer, Quality & Inspection", "TQ Cert Services (Tata Projects Ltd.)", "Aug 2023 – Aug 2025",
     "500 MW BESS + solar hybrid, Khavda, Gujarat  |  1,034 MW Siyambar / Bandha solar, Jaisalmer, Rajasthan",
     ["Served as the client's technical and quality authority, overseeing EPC contractor performance on two of the "
      "country's largest renewable programmes, including the Jaisalmer site in western Rajasthan.",
      "Reviewed and approved contractor QAPs, ITPs and field quality procedures; enforced hold and witness points so "
      "stage clearances were evidence-based rather than schedule-driven.",
      "Carried out FAT / pre-dispatch inspection at OEM works for modules, inverters, transformers, switchgear and "
      "battery systems, stopping non-conforming equipment before it reached site.",
      "Issued, tracked and closed NCRs, led quality audits, reviewed designs and drawings, and decided deviation and "
      "concession requests on technical merit."])
role(cv, "Project Lead", "Tata Power Renewable Energy Ltd.", "Aug 2022 – Aug 2023",
     "450 MWp / 335 MW AC solar, Bikaner, Rajasthan  |  300 MW solar, Dholera, Gujarat",
     ["Led developer-side site execution across ~750 MW in two states, holding EPC contractors to schedule, quality and "
      "safety commitments on behalf of the asset owner.",
      "Tracked construction progress through site reviews, milestone verification and punch-list closure, taking "
      "contractors through to commissioning and COD readiness.",
      "Coordinated engineering, procurement, contracts, HSE and O&M to resolve interface issues and keep "
      "multi-package sites in sequence."])
role(cv, "Project Engineer – Implementation", "Solar Energy Corporation of India (SECI)", "Oct 2020 – Aug 2022",
     "2,050 MW Pavagada Solar Park, Karnataka  |  1.4 MWh island BESS, Lakshadweep",
     ["Monitored developer and contractor delivery against scheme milestones at one of the world's largest solar parks, "
      "on behalf of the central nodal agency.",
      "Delivered a 1.4 MWh island BESS under logistically constrained conditions, which involved planning material, "
      "manpower and equipment around limited access.",
      "Built the policy, tendering and authority-liaison experience behind contract-aware site decisions."])
role(cv, "Electrical Engineer – Execution & O&M", "KC Kopar Energy Solutions", "Jun 2015 – Oct 2020",
     "25.4 MW solar at Cochin International Airport (CIAL) – the world's first fully solar-powered airport",
     ["Executed installation, testing and commissioning of modules, inverters, LT / HT switchgear, transformers and "
      "evacuation infrastructure in a live, security-controlled airport environment.",
      "Ran plant O&M – preventive and breakdown maintenance, fault diagnosis and generation reporting – learning the "
      "failure modes that now guide construction QA/QC decisions."])

heading(cv, "Education & Certification")
bullet(cv, " SCMS School of Engineering & Technology, Cochin (2011 – 2015)", "B.Tech (Full-Time), Electrical & Electronics Engineering –")
bullet(cv, "", "Certified Lean Six Sigma Green Belt (CLSSGB)")
bullet(cv, " MS Project, AutoCAD, DPR / MIS reporting", "Tools:")

cv.save(OUT + "/Justin_Thomas_CV_Wind_Site_Construction_Head.docx")

# ---------------- Cover letter ----------------
cl = Document(); base(cl)
cl.styles["Normal"].font.size = Pt(10.5)
cl.styles["Normal"].paragraph_format.space_after = Pt(5)
header_block(cl, "Application – DGM / GM, Site Construction Head – Wind Power Project, Fatehgarh")
cl.add_paragraph("28 October 2026")
cl.add_paragraph("The Hiring Manager\nSunshine Workforce Solutions – on behalf of the Renewable Energy Client\nJodhpur, Rajasthan")
p = cl.add_paragraph(); p.add_run("Subject: Application for Site Construction Head (DGM / GM) – 50–150 MW Wind Power Project, Fatehgarh").bold = True
cl.add_paragraph("Dear Hiring Manager,")
paras = [
    "I am applying for the Site Construction Head (DGM / GM) role for your client's wind power project at Fatehgarh. "
    "I have spent more than 11 years building utility-scale renewable power plants, about 3.9 GW of solar and 1 GWh of "
    "battery storage in total. I have managed EPC contractors, run civil, mechanical and electrical site packages, and "
    "delivered the HV balance of plant and grid connection that a wind farm depends on.",

    "Rajasthan is familiar ground for me. As Owner's Engineer on the 1,034 MW Siyambar / Bandha solar programme in "
    "Jaisalmer district, close to Fatehgarh, and as Project Lead on 450 MWp at Bikaner for Tata Power Renewables, I have "
    "worked with the remote logistics, harsh site conditions and the local authorities and communities that "
    "shape every site in the region.",

    "Your key responsibilities line up closely with what I do today:",
]
for x in paras:
    cl.add_paragraph(x).paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
for lead, txt in [
    ("Project oversight and BOP: ", "I am currently leading electrical delivery for a 125 MW / 500 MWh BESS for JSW Renew "
     "Energy, covering MV / HV balance of plant, foundations and the 145 kV evacuation interface, with eight OEMs and "
     "vendors to coordinate."),
    ("Contractor management: ", "I have held EPC contractors to schedule, quality and safety commitments as the "
     "developer, as the Owner's Engineer, and as the contractor myself, so I know where each party's incentives lie."),
    ("Quality control: ", "I build and run QAP / ITP regimes, hold and witness points and NCR / RCA / CAPA cycles. On my "
     "current site, 278 RFIs have been tracked to closure."),
    ("Safety and schedule: ", "I enforce permit-to-work and HSE discipline, plan for weather risk, and track progress "
     "through MS Project, DPR / MIS and milestone verification through to commissioning and COD."),
]:
    p = cl.add_paragraph(style="List Bullet"); p.paragraph_format.space_after = Pt(3)
    p.add_run(lead).bold = True; p.add_run(txt)

for x in [
    "I have not yet led a WTG erection campaign, and I would rather say so plainly. The rest of a wind farm's construction "
    "scope is work I have delivered many times: civil foundations, 33 kV HT cabling and panels, pooling "
    "substations, 145 kV evacuation, multi-contractor coordination and statutory approvals. Crane planning, blade and "
    "nacelle logistics and OEM erection sequences are areas I would get up to speed on quickly, in the same way I moved "
    "from solar into GWh-scale storage. My Lean Six Sigma Green Belt training and my experience on the developer, Owner's "
    "Engineer, contractor and government sides would help me build a site organisation that the client, the Owner's "
    "Engineer and local stakeholders can all rely on.",

    "I am willing to relocate to Fatehgarh / Jodhpur and can join at short notice. I would welcome the chance to discuss "
    "how I could deliver your project safely, on schedule and to the required quality. Thank you for considering my "
    "application.",
]:
    cl.add_paragraph(x).paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
cl.add_paragraph("Yours sincerely,\n\nJustin Thomas\n+91 94466 74610  |  justinthomas1992@gmail.com")
cl.save(OUT + "/Justin_Thomas_Cover_Letter_Wind_Site_Construction_Head.docx")
