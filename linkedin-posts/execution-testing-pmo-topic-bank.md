# LinkedIn Topic Bank: Grid Integration, Testing & Commissioning, PMO/PMC

These topics show **execution depth**, which is what directors hire for. Each topic has a hook, the core points, and a question to close.
Status: ✅ = published, ⏳ = drafted, blank = idea.

---

## A. BESS: Grid Integration

| # | Hook | Core points | Closing question |
|---|---|---|---|
| A1 | "Your BESS is ready. The grid isn't." | Connectivity approval, GC/GTA, grid code compliance, PPC tuning, SLDC/RLDC data telemetry | What's your longest wait: connectivity or compliance? |
| A2 | "The PPC is the most underrated box in a BESS plant" | Power plant controller closes the loop at the POI; ramp rates, Q-V droop, frequency response; tuning on site | Who owns PPC tuning on your projects: OEM or EPC? |
| A3 | "Grid studies are not paperwork" | Load flow, short circuit, RMS & EMT studies, harmonic study, SCR at POI; validated OEM models | Have you ever had to redo a study after OEM change? |
| A4 | "Ride-through tests fail for boring reasons" | LVRT/HVRT settings, protection mis-coordination, aux supply drop, UPS sizing for control | What tripped your plant in its first grid event? |
| A5 | "Metering & telemetry delays COD more than batteries do" | ABT/SEM meters, RTU/SCADA integration, IEC 104 mapping, time sync | |

## B. BESS: FAT (Factory Acceptance Tests) by equipment

| # | Hook | Core points |
|---|---|---|
| B1 ✅ | "A BESS that passes FAT can still fail on site" | FAT vs SAT gap, firmware freeze, integrated FAT (**published**) |
| B2 | "Battery container FAT checklist directors should ask about" | Cell/module traceability, insulation resistance, BMS alarm/trip matrix, HVAC, fire detection & suppression interface, door/E-stop interlocks |
| B3 | "PCS FAT: what to witness, not just read" | Efficiency curve, harmonics (IEEE 519 / IEC 61000), FRT on test bench, P-Q capability, firmware version lock |
| B4 | "Transformer & switchgear FAT is still where many surprises hide" | Routine tests per IEC 60076 / IEC 62271, losses vs guaranteed, tan-delta, SFRA baseline |
| B5 | "EMS FAT = software testing. Treat it that way" | Point-to-point I/O list, protocol conformance (Modbus/IEC 61850/IEC 104), use-case scenarios, cybersecurity basics (IEC 62443) |
| B6 | "Witness vs review: which FATs need your engineer on a plane?" | Risk-based witness plan, sample sizes, hold points in the ITP |

## C. BESS: SAT & Commissioning (whole system)

| # | Hook | Core points |
|---|---|---|
| C1 | "Pre-commissioning ≠ commissioning ≠ SAT" | Clear stage gates: mechanical completion → cold tests → hot tests → SAT → trial run → COD |
| C2 | "The capacity test that decides your warranty for 15 years" | Rated power/energy test, RTE measurement method, auxiliary consumption, ambient correction; agree method in contract |
| C3 | "End-to-end testing: BMS → PCS → EMS → PPC → SLDC" | Signal-by-signal checks, failure-mode tests, comms loss behaviour |
| C4 | "Fire system SAT is not optional theatre" | Detection, off-gas, suppression discharge logic, ESD, interface with fire brigade plan |
| C5 | "Trial run & COD: where commercial teams and engineers clash" | Trial run criteria, availability calculation, punch list A/B/C classification |

## D. Solar & Hybrid: Grid Integration, FAT, SAT

| # | Hook | Core points |
|---|---|---|
| D1 | "Module FAT/pre-dispatch inspection: what a sample really tells you" | EL imaging, flash test, visual, BOM vs certification, sampling plan (AQL) |
| D2 | "Inverter FAT for utility solar: the 5 checks that matter" | Efficiency, harmonics, reactive capability, FRT, firmware |
| D3 | "Solar SAT: string level to POI" | IV curve tracing, IR thermography, insulation tests, SCADA, PR test |
| D4 | "The PR test is a contract, not a calculation" | Measurement method, irradiance sensors calibration, test window, IEC 61724 |
| D5 | "Hybrid plants: two assets, one POI, one grid code" | Shared connectivity, PPC coordination, solar-charging rules, CUF/availability compliance |
| D6 | "Hybrid commissioning: test the controller, not just the assets" | Solar-to-BESS charging, peak dispatch, curtailment handling, FDRE schedule compliance |
| D7 | "AC vs DC coupled hybrid: an execution view" | Clipping recovery, PCS count, protection complexity, testing scope |

## E. BESS & Solar: Project Planning, PMO, PMC

| # | Hook | Core points |
|---|---|---|
| E1 | "Most renewable projects slip in the first 90 days, not the last 90" | Land, connectivity, design freeze, long-lead ordering |
| E2 | "Long-lead items now decide your COD" | Power transformers, MV switchgear, PCS: order before final design freeze; lead time tracking |
| E3 | "PMO vs PMC: what developers actually need" | PMO = governance & portfolio reporting; PMC = owner's engineer on site; avoiding overlap |
| E4 | "The 5 dashboards a renewable PMO should show the board" | Critical path, cash flow/S-curve, risk register, quality NCRs, HSE |
| E5 | "Your schedule is lying if it has no interfaces" | Interface matrix: civil ↔ electrical ↔ OEM ↔ utility; RACI |
| E6 | "Inspection & Test Plans are your best schedule-protection tool" | ITP hold points, witness planning, NCR closure speed |
| E7 | "Why EPC claims start in the commissioning phase" | Delay attribution, documentation, change orders, LD exposure |
| E8 | "Handover is a project, not a meeting" | As-builts, O&M manuals, spares, training, warranty registration, SCADA data handover |
| E9 | "Lessons learned registers nobody reads, and how to fix that" | Turn lessons into checklists and tender clauses |

---

## Suggested 6-week calendar (2 posts/week)

| Week | Tue | Thu |
|---|---|---|
| 1 | B1 ✅ FAT vs SAT | E2 Long-lead items |
| 2 | A2 PPC | D5 Hybrid single POI |
| 3 | C2 Capacity test | E3 PMO vs PMC |
| 4 | B3 PCS FAT | D4 PR test |
| 5 | A4 Ride-through | E4 Board dashboards |
| 6 | C5 Trial run & COD | E8 Handover |

---

## ✅ Published post (B1)

A BESS that passes FAT can still fail on site.

It happens more often than most project plans assume.

FAT proves the equipment works in the factory.
SAT proves the system works on YOUR grid.

The gap between the two is where projects lose months.

What FAT should cover (equipment level):
• Battery containers: insulation, BMS alarm/trip logic, HVAC and fire detection interfaces
• PCS: efficiency, harmonics, ride-through on the test bench, firmware version frozen
• MV transformer & switchgear: routine tests per IEC 60076 / IEC 62271
• EMS/SCADA: point-to-point I/O list, protocol tests (IEC 61850 / Modbus / IEC 104)

What SAT must prove (system level):
• End-to-end communication: BMS → PCS → EMS → PPC → grid operator SCADA
• Protection coordination and relay tests at the POI
• Capacity and round-trip efficiency at rated power
• Active/reactive power, voltage and frequency response vs grid code
• Fire suppression and emergency shutdown functional test
• Black start / islanding, if contracted

Three things that save the most time:
1. Freeze firmware at FAT. Any change after FAT means re-testing.
2. Run an integrated FAT (BMS + PCS + EMS together), not just component FATs.
3. Agree SAT and grid compliance test procedures with the utility before equipment ships.

Commissioning is not the last step of a project. It has to be planned from day one.

What has caused the biggest SAT delay on your projects?

#BESS #EnergyStorage #Commissioning #FAT #SAT #GridIntegration #ProjectManagement
