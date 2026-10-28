# Electrical Engineering Scope of AI-Era Data Center Development (as of Oct 2026)

> Research method note: Direct page fetches to nerc.com, arxiv.org and developer.nvidia.com were blocked by this session's network policy. Findings below come from search-engine extracts of those primary documents plus secondary coverage. Where only secondary sources were available, that is flagged. Items in "Inferences" that rest on general engineering practice rather than a retrieved source are labelled as such. The report writer should treat them as context, not citable fact.

## Grid connection: voltage levels, substations, redundancy, transformers, lead times, protection

### Takeaway
Hyperscale and AI campuses now connect at transmission voltage. In the US that is typically 230 kV (Dominion/PJM incidents occurred on 230 kV lines). In India, campuses use 220 kV and 400 kV GIS substations stepping down to 33 kV. Each campus has dedicated GIS substations sized for 0.6–1 GW. Power-transformer lead times of about 2.5 years (128–144 weeks) are now a critical-path item.

### Cited Findings
- **US voltage level, incident evidence:** Both major Northern Virginia load-loss events began with faults on 230 kV transmission lines. The July 10, 2024 event started with a failed lightning arrestor on a 230 kV line. The July 22, 2026 event started with a 230 kV line fault in Dominion's zone — [NERC Incident Review (PDF)](https://www.nerc.com/globalassets/our-work/reports/event-reports/incident_review_large_load_loss.pdf); [mgrid.org, Aug 2026](https://mgrid.org/2026/08/11/pjm-says-northern-virginia-data-centers-tripped-too-early-when-3800-mw-left-the-grid-after-a-cleared-fault/)
- **India, Navi Mumbai (Ghansoli):** Tata Consulting Engineers designed 220 kV/33 kV and 400 kV/33 kV GIS substations for a campus designed for up to 1 GW of total demand, including 620 MW of IT load. That is an implied facility-to-IT ratio of about 1.6 at design peak — [Tata Consulting Engineers](https://www.tataconsultingengineers.com/project/hyperscale-data-centre-power-infrastructure/)
- **India, Hyderabad:** Hyosung T&D India is reportedly supplying 400 kV GIS for the CtrlS Chandanvelly hyperscale park, which is expected to need about 600 MW. This rests on "industry sources" — [Switchgear Magazine](https://switchgear-magazine.com/news/business/hyosung-supplies-400-kv-gis/)
- **India, Colt DCS/RMZ Mumbai 3:** The 64 MW facility (148 MW campus potential) has access to a 220 kV GIS substation — [CRN Asia, 2026](https://www.crnasia.com/india/news/2026/colt-dcs-rmz-start-64mw-mumbai-data-centre-construction-after-signing-hyperscale-client)
- **India, Maharashtra:** MERC approved a 400/220 kV GIS substation at Ambernath/Palava (Thane) to serve data-center load under the dedicated distribution facility model, targeted for 2027 — [Mercom India](https://www.mercomindia.com/merc-approves-400-220-kv-transmission-project-to-support-data-center-load)
- **GCC:** Stargate UAE is a 1 GW cluster within a 5 GW UAE–US AI Campus in Abu Dhabi. The first 200 MW is targeted for 2026 and the first 1 GW is "on track for 2026" per Cushman & Wakefield. No grid-connection voltage was found — [Gulf News](https://gulfnews.com/business/markets/uae-openai-will-build-massive-stargate-ai-center-in-abu-dhabi-1.500136990); [PR Newswire / Cushman & Wakefield](https://tools.prnewswire.com/en-us/live/20823/release/20250714EN28611). The Emirates National Grid backbone is 400 kV, e.g. the Taweelah–Dubai 400 kV link (a historical 2005 article) — [Power Engineering](https://www.power-eng.com/operations-maintenance/abu-dhabi-and-dubai-to-link-grids-by-late-2006/)
- **Transformer lead times:**
  - Wood Mackenzie's Q2 2025 survey put power transformers at an average of 128 weeks and generator step-up units at 143–144 weeks.
  - Lead times for both have exceeded 100 weeks since 2023.
  - Distribution transformers averaged about 30 weeks, down from a peak of more than 100 weeks in 2023.
  - The estimated 2025 US supply deficit is about 30% for power transformers and about 10% for distribution transformers.
  - Substation power-transformer demand rose about 116% and GSU demand about 274% between 2019 and 2025.
  - Sources: [Power Magazine](https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis); [EE Power](https://eepower.com/market-insights/transformer-supply-chain-woes-persist-as-energy-demand-grows/)
  - A trade-press claim that substation transformer lead times exceed 160 weeks in 2026 is unverified — [EnkiAI](https://enkiai.com/sustainability-initiatives/data-center/grid-power-infrastructure-2026-mitsubishi-14-gw-surge/)
- **Protection and auto-reclose interaction (July 2024):** Auto-reclosing was set for 3 attempts, staggered at each end of the line. This produced 6 successive faults in 82 seconds, with voltage at 0.25–0.40 pu in the load-loss area. The data-center substation breakers did not trip. The facilities' own controls transferred to backup — [NERC Incident Review](https://www.nerc.com/globalassets/our-work/reports/event-reports/incident_review_large_load_loss.pdf); [APPA](https://www.publicpower.org/periodical/article/nerc-incident-review-examines-risks-challenges-tied-integration-large-loads)
- **Interconnection regulation, Texas:** ERCOT defines "Large Electronic Loads" as data-center and crypto loads of 75 MW or more. SB 6 directs the PUCT to set transmission-level interconnection standards at 75 MW or above, with a possible lower threshold, and to require backup-generation disclosure — [ERCOT market notice](https://www.ercot.com/services/comm/mkt_notices/M-B062325-01); [K&L Gates](https://www.klgates.com/Texas-Senate-Bill-6-and-Impacts-on-Large-Load-Development-in-ERCOT-2-17-2025)
- **NERC Level 2 alert (2025):** The alert covers large-load interconnection, study, commissioning and operations — [NERC Alert](https://www.nerc.com/globalassets/programs/bpsa/alerts/2025/nerc-alert-level-2--large-loads.pdf)

### Inferences
- **Typical sizing (engineering practice, not sourced here):**
  - Campuses connect via ring-bus or breaker-and-a-half HV yards with 2–4 incoming circuits for N-1 or N-2 security.
  - Main HV/MV transformers are typically about 80–200 MVA, sized so N-1 transformer loss carries full load.
  - Step-down goes to 33 kV (India/GCC/IEC markets) or 34.5/13.8 kV (US), then to 400/415 V (IEC) or 480 V (US) at the LV level.
  - NVIDIA references a 13.8 kV AC to 800 VDC conversion in the US context (see the next section).
- **Schedule:** A 128–144-week transformer lead time means HV equipment must be ordered before final interconnection agreements. Developers increasingly pre-purchase or standardize transformer frames.
- **Data-center scale:** The Indian examples (600 MW to 1 GW at 220/400 kV) show campus scale now matches a large generating station.

### Gaps
- No primary utility or TSO document was found on dedicated-substation N-1/N-2 criteria for data centers (e.g., Dominion, CEA/CTU India, DEWA/TRANSCO).
- No source gave transformer MVA ratings or protection schemes (distance/differential settings) specific to data centers.
- No verified 132 kV examples for India/GCC, and no 345 kV US examples, were retrieved.
- Saudi Arabia (Humain) grid connection: not found.

## MV/LV distribution architectures, 800 VDC / ±400 VDC rack power and solid-state transformers

### Takeaway
Classical AC architectures (2N, N+1 block-redundant, distributed redundant) at 415/480 V AC to 54 V DC in-rack are being displaced for AI racks above about 200 kW. Two competing high-voltage DC approaches lead this shift:
- **NVIDIA 800 VDC:** in production with the Kyber/Rubin Ultra platform in 2027. Racks of about 600 kW (576 GPUs) are fed from centralized AC/DC conversion, potentially via solid-state transformers from 13.8 kV.
- **OCP Mt. Diablo ±400 VDC:** a disaggregated "sidecar" power rack from Google, Meta and Microsoft. v1.0.0 was effective October 2026, targeting 100 kW to 1 MW racks.

### Cited Findings
- **NVIDIA architecture:** Grid AC is converted centrally in the power room to 800 V HVDC, then distributed through the hall to rows and IT racks. Traditional transformer-rectifier and SST approaches are both being studied — [NVIDIA Developer Blog](https://developer.nvidia.com/blog/?p=100571); [HPCwire](https://www.hpcwire.com/off-the-wire/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- **Timeline:** Full-scale production of 800 V HVDC data centers coincides with Kyber rack-scale systems in 2027. Kyber holds 576 Rubin Ultra GPUs per rack, and one source cites a design of about 600 kW per rack — [DCD](https://www.datacenterdynamics.com/en/news/nvidia-working-with-data-center-partners-to-build-800v-hvdc-power-systems/); [Engineering.com](https://www.engineering.com/navitas-nvidia-partner-on-800v-hvdc-for-kyber-gpu-systems/)
- **GTC 2025 demo:** NVIDIA showed an 800 V "sidecar" model powering 576 Rubin Ultra GPUs in a single Kyber rack — [NAND Research](https://nand-research.com/data-center-power-the-transition-to-800-vdc/)
- **Claimed benefits:**
  - Up to 5% end-to-end efficiency improvement.
  - About 45% copper reduction (repeated by secondaries; not confirmed from primary text).
  - About 85% more power through the same conductor size versus 415 VAC (secondary, unverified).
  - Sources: [Inside Deep Tech](https://www.insidedeeptech.com/800-vdc-power-distribution-ai-data-centers-full-guide/); [Converge Digest](https://convergedigest.com/the-megawatt-shift-nvidias-800-vdc-strategy/)
- **SST role:** One secondary source describes converting 13.8 kV AC directly to 800 VDC at the perimeter using SSTs. It also reports a joint NVIDIA/Google/Microsoft 800 VDC white paper via OCP (March 2026) and an LVDC SST specification (July 2026). These are single-source and unverified — [Macroplane](https://macroplane.com/blog/800-vdc-stocks); [Inside Deep Tech](https://www.insidedeeptech.com/800-vdc-power-distribution-ai-data-centers-full-guide/)
- **800 VDC ecosystem partners:** Delta, Schneider Electric, Vertiv, Infineon, STMicroelectronics, ABB, Eaton, GE Vernova, Hitachi Energy, Siemens, Navitas and Texas Instruments. Navitas showed a 96.5%-efficient DC-DC board at COMPUTEX in June 2026 — [Electronics Weekly](https://www.electronicsweekly.com/news/business/nvidia-and-partners-gear-up-for-800vdc-datacentres-and-vera-rubin-for-2025-10/); [Engineering.com](https://www.engineering.com/navitas-nvidia-partner-on-800v-hvdc-for-kyber-gpu-systems/)
- **Vertiv:** Vertiv is aligning products with the NVIDIA 800 V HVDC standard — [Tech Critter](https://www.tech-critter.com/vertiv-nvidia-next-gen-800v-hvdc-standard-for-ai-data-centers)
- **OCP Mt. Diablo:**
  - Google moved from 48 VDC to ±400 VDC to scale racks from 100 kW to 1 MW, choosing 400 VDC to reuse the EV supply chain.
  - Co-developers are Meta and Microsoft. Draft 0.5 was issued May 2025.
  - The "Mt. Diablo Disaggregated Power Rack Specification v1.0.0" base spec took effect October 8, 2026.
  - Earlier "Diablo 400" drafts (v0.5.2, v0.7.0) have sections on AC input, ride-through, ±400 VDC output and efficiency. Numeric values were not retrieved.
  - Sources: [The Register](https://www.theregister.com/2025/05/01/google_details_plans_for_1/); [W.Media](https://w.media/1mw-it-rack-coming-soon-thanks-to-google-ocp-partnership/); [OCP Mt. Diablo v1.0.0 PDF](https://www.opencompute.org/wp-content/uploads/2026/10/OCP-Specification-Mt.-Diablo-Disaggregated-Power-Rack-Specification-v1.0.0.pdf); [OCP Diablo 400 v0.7.0](https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf)
- **Mt. Diablo topology:** A sidecar rack of rectifiers feeds DC over a shared busbar to racks in the row, aimed at racks above 500 kW. It differs from NVIDIA's centralized 800 VDC approach — [Glenn Klockwood](https://www.glennklockwood.com/garden/diablo)

### Inferences
- **Classical topologies (engineering practice, not sourced here):**
  - **2N:** two fully independent A/B UPS and switchgear paths, each sized for 100% load. Typical of Tier IV and enterprise/finance sites.
  - **Distributed / "catcher" or N+1 block redundant:** 4N/3 or 3N/2 configurations with STS or a reserve block. These are favored by hyperscalers for higher utilization, about 67–75% per block versus 50% for 2N.
  - **Busway:** overhead busway at 415/480 V (400–1,250 A tap-offs) feeds rack PDUs in place of floor PDUs and RPPs.
  - **Rack conversion:** in-rack power shelves convert AC to a 48/54 V DC busbar (OCP ORV3).
- **Why DC wins at high density:** at more than 200 kW per rack, 54 V busbars need roughly 4,000 A or more per rack. That copper mass and those I²R losses are the core motivation for 800 VDC or ±400 VDC.
- **SST readiness:** SSTs are presented as a way to collapse the MV transformer, rectifier and UPS stages into one power-electronic stage. As of 2026 they remain pre-commercial at MW scale. Treat efficiency claims as vendor or projection figures.

### Gaps
- Numeric parameters in Mt. Diablo v1.0.0 (ride-through, voltage tolerance, efficiency) were not retrieved.
- No primary NVIDIA white paper text was retrieved to confirm the 45% copper or 5% efficiency figures.
- No commercial SST deployments at data-center MW scale were verified.
- DC protection standards (DC arc-flash, solid-state breakers, IEC 60364 / NEC treatment of 800 VDC) were not researched.

## UPS and backup power

### Takeaway
Double-conversion (IEC 62040-3 VFI) static UPS remains the norm. Modern transformerless and SiC units report 96–97% efficiency in double conversion. Lithium-ion (mostly LFP), qualified via UL 9540A, is displacing VRLA.

Diesel gensets of about 2.5–3 MW remain the backup standard, with emissions as the binding constraint:
- **US:** Tier 4 proposed as BACT in Virginia.
- **India:** CPCB IV+ applies to all gensets regardless of standby use.

Tier III targets about 99.982% availability (concurrently maintainable). Tier IV targets about 99.995% (fault tolerant, 2N).

### Cited Findings
- **IEC 62040-3 classification:** Double-conversion UPS falls under IEC/EN 62040-3 "VFI-S…". Vendor guide specs call for VFI-SS-111 performance, with the critical load continuously on the inverter in normal mode — [EU JRC Code of Conduct on UPS](https://e3p.jrc.ec.europa.eu/sites/default/files/2023-09/code_of_conduct_ups_16032011.pdf); [Vertiv Liebert EXM guide spec](https://inte.vertiv.com/49ca9f/globalassets/products/critical-power/uninterruptible-power-supplies-ups/liebert-exm-ups-480-volt-30-250kva-guide-specifications-sl-26104.pdf)
- **UPS efficiency:**
  - Double conversion is less efficient because two converters run continuously. SiC and modular designs have improved it.
  - Transformerless units report 96–97% (vendor-sourced).
  - ENERGY STAR stakeholders note the IEC 62040-3 efficiency test method can be biased by test-load setup.
  - Sources: [Legrand](https://www.legrand.com/datacenter/sites/g/files/ocwmcr1671/files/2025-03/Understanding%20UPS%20Efficiency%20in%20Data%20Centres_Localized_1.pdf); [ENERGY STAR](https://www.energystar.gov/sites/default/files/specs/private/UPS_V1_Draft2_Stakeholder_Comment_Summary.pdf)
- **Li-ion qualification:** LFP UPS batteries are verified through UL 9540A thermal-runaway testing. This comes from a study aid, not a code text — [BICSI DCDC study guide](https://open-exam-prep.com/study-guides/bicsi-dcdc/ch07-electrical-distribution/sec03-ups-systems-batteries-sizing)
- **UPS as a grid resource:** Academic work proposes grid-forming control modes for centralized data-center UPS ("from liability to asset") — [arXiv 2512.16497](https://arxiv.org/pdf/2512.16497)
- **Uptime Tiers:**
  - Tier III: about 99.982% availability, about 1.6 h of downtime per year. Concurrently maintainable, with redundant components and multiple paths. A capacity-component failure may need manual switching.
  - Tier IV: about 99.995%, under about 26 minutes per year. Fault tolerant, with 2N and automatic failover.
  - These are secondary sources. Uptime itself de-emphasizes availability percentages.
  - Sources: [TechTarget](https://www.techtarget.com/it-infrastructure/tip/Data-center-tiers-and-why-they-matter-for-uptime); [Bamboozle](https://blog.bamboozle.me/datacenter-tier-ratings-explained/)
- **Genset emissions, US:**
  - A single 2.5 MW diesel tested 100 h/yr emits about 1.2 t NOx and 0.05 t PM per year, using AP-42 factors — [arXiv 2509.21312 (Texas study)](https://arxiv.org/pdf/2509.21312)
  - Virginia proposed treating Tier 4 as BACT for data-center generators, determined case by case — [Fairfax County EQAC](https://www.fairfaxcounty.gov/environment-energy-coordination/sites/environment-energy-coordination/files/Assets/2026/2026%20EQAC/FINAL%202025%203%209c%20Diesel%20Generators_A-1a.pdf)
  - Northern Virginia generator air-quality impacts are under public scrutiny — [OPB, Jul 2026](https://www.opb.org/article/2026/07/22/data-center-air-quality-how-we-reported/); [Breathe Project](https://breatheproject.org/reports-studies/diesel-generators-at-data-centers-status-impacts-and-protective-practices/)
- **Genset emissions, India:** CPCB IV+ replaced CPCB II for new gensets from 2023, with much lower NOx and PM limits. There is no standby carve-out. Compliance typically needs electronically governed common-rail engines with after-treatment. Published CPCB IV+ limit bands reportedly go only up to 800 kW, so MW-class sets need regulator or OEM confirmation — [Secured Engineers](https://www.securedengineers.com/insights/dg-set-cpcb-iv-plus-emission-norms/); [Carraglobe](https://carraglobe.com/importing-diesel-generators-emissions-certification/)
- **Islanded or onsite-generation ramp rates:** Gas turbines ramp in about 1–10 s and Li-ion batteries in about 100 ms. This is relevant to sizing onsite generation for AI loads — [arXiv 2607.17391](https://arxiv.org/pdf/2607.17391)

### Inferences
- **Typical practice (not sourced here):**
  - UPS runtime has shrunk to about 5 minutes (Li-ion) because gensets start and synchronize in about 10–15 s.
  - Gensets are 2–3.25 MW, 400 V or 11/13.8 kV MV units, with N+1 or N+2 per block.
  - Uptime Tier III/IV requires generators be rated for unlimited-runtime (prime or continuous, or Data Center Continuous) duty rather than standby ratings.
  - Onsite fuel autonomy is typically 12–72 h.
- **Event linkage:** In both Virginia events, the "load loss" was the UPS and genset transfer logic deliberately disconnecting from a sagging grid. Backup-system settings are now a bulk-system reliability parameter (see the power-quality section).

### Gaps
- Uptime Tier Standard and TIA-942-C (Rated-1 to Rated-4) primary text was not retrieved.
- Requirements for genset continuous ratings were not sourced.
- The US EPA NSPS IIII / NESHAP ZZZZ emergency-engine 100 h/yr maintenance-and-testing allowance was not retrieved from a primary source (commonly cited, but unsourced here).
- EU (Medium Combustion Plant Directive) and GCC genset emission rules were not researched.
- NFPA 855 specifics (unit size and separation limits, UL 9540/9540A, large-scale fire testing) for UPS/BESS rooms: no source retrieved.

## Power quality and AI load dynamics

### Takeaway
Synchronous AI training produces fleet-coherent power swings of tens to hundreds of MW. These concentrate around 0.2–3 Hz, which risks sub-synchronous and torsional resonance with generators (Microsoft/NVIDIA/OpenAI, arXiv 2508.14318).

Separately, voltage-sensitive data-center protection has produced grid-scale load-loss events in Northern Virginia:

| Date | Load lost |
|---|---|
| July 2024 | 1,500 MW |
| February 2025 | 1,800 MW |
| July 2026 | about 3,800–4,000 MW |

These events are driving mandatory large-load ride-through rules: ERCOT NOGRR282, a PJM FERC filing planned for November 2026, and NERC standards in 2027. Mitigation combines GPU-level power smoothing, rack energy storage (GB300 power-shelf capacitors) and facility BESS.

### Cited Findings
- **July 10, 2024 Eastern Interconnection (Virginia):**
  - About 1,500 MW of data-center load was lost across 60 points and 25 substations.
  - Six faults occurred in 82 s from 230 kV auto-reclosing, with 0.25–0.40 pu voltage.
  - Data centers transferred to backup. Frequency peaked at about 60.047–60.053 Hz.
  - Operators switched out shunt capacitors to control the overvoltage.
  - Operators had not anticipated this voltage-sensitive load behavior. NERC warned about uncontrolled reconnection.
  - Sources: [NERC Incident Review](https://www.nerc.com/globalassets/our-work/reports/event-reports/incident_review_large_load_loss.pdf); [White & Case](https://www.whitecase.com/insight-alert/nerc-tees-plan-assess-grid-risks-associated-data-centers); [DCD](https://datacenterdynamics.com/en/news/virginia-narrowly-avoided-power-cuts-when-60-data-centers-dropped-off-the-grid-at-once); [ReliabilityFirst](https://www.rfirst.org/resource-center/incident-review-and-guidance-on-voltage-sensitive-large-loads/)
- **February 2025:** NERC's October 2026 presentation lists a 1,800 MW load loss in Loudoun and Fairfax counties — [UCS blog citing NERC](https://blog.ucs.org/lee-shaver/data-centers-are-already-stressing-the-grid-regulators-are-playing-catch-up/)
- **July 22, 2026 Dominion zone:**
  - A normally cleared 230 kV fault caused about 2,970 MW to transfer to backup at 07:56:33. The resulting voltage rise tripped a further 1,099 MW at 07:57:40.
  - Frequency peaked at 60.092 Hz. ACE recovered in 9 minutes (versus the 30 minutes allowed by BAL-001-2). Load returned within 30 minutes.
  - The reported cause was a sub-conductor pulling free from its compression sleeve.
  - PJM said data centers are "disconnecting too early."
  - Figures differ by source: NERC cites 3,800 MW and PJM about 4,000 MW.
  - Sources (mgrid.org is secondary): [mgrid.org](https://mgrid.org/2026/08/11/pjm-says-northern-virginia-data-centers-tripped-too-early-when-3800-mw-left-the-grid-after-a-cleared-fault/); [APPA](https://www.publicpower.org/periodical/article/pjm-dominion-review-large-load-transfer-event); [Datacenter Dispatch](https://datacenterdispatch.org/northern-virginia-dropped-3-8-gw-again-two-years-after-nerc-said-why/)
- **Regulatory response:**
  - PJM will file a large-load ride-through rule at FERC in November 2026, ahead of NERC thresholds expected in 2027 — [mgrid.org](https://mgrid.org/2026/09/10/pjm-will-file-its-own-data-center-ride-through-rule-in-november-before-nerc-sets-thresholds/)
  - FERC directed NERC in April 2025 to investigate large-load loss events — [White & Case](https://www.whitecase.com/insight-alert/nerc-tees-plan-assess-grid-risks-associated-data-centers)
  - NERC has a draft SAR on "computational load disturbance performance" — [NERC draft SAR](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/draft_sar_computational_load_disturbance_performance-1.pdf)
- **ERCOT NOGRR282:** This board-priority rule sets voltage and frequency ride-through for "Large Electronic Loads" of 75 MW or more (Section 2.14). It exempts loads approved to energize by November 14, 2025. It was retitled "Large Computational Load Ride-Through Requirements" and TAC recommended approval on April 29, 2026 — [ERCOT comments, May 2026](https://www.ercot.com/files/docs/2026/05/11/282NOGRR-30-ERCOT-Comments-051126.docx); [ERCOT policy update](https://www.ercot.com/files/docs/2026/04/16/4-High-Impact-Policy-Discussions-in-the-Stakeholder-Process.pdf)
- **NERC Large Loads Task Force white papers:**
  - "Characteristics and Risks of Emerging Large Loads" (July 2025) covers loads from a few MW to several GW. It analyzes seven risk areas: load shedding and restoration, security, power quality, stability, operations and balancing, long-term planning, and observability. It cites ERCOT load-reduction events.
  - A second white paper (March 2026) found existing NERC standards inadequate.
  - Sources: [NERC LLTF White Paper](https://www.nerc.com/globalassets/who-we-are/standing-committees/rstc/whitepaper-characteristics-and-risks-of-emerging-large-loads.pdf); [NERC Large Loads FAQ](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/large-loads-faqs.pdf)
- **AI training dynamics (Microsoft/NVIDIA/OpenAI, arXiv 2508.14318):**
  - Power alternates between compute-heavy and communication-heavy phases. Swing amplitude grows with job size.
  - The swings appear coherently at rack, data-center and grid levels, reaching tens to hundreds of MW.
  - Energy concentrates at roughly 0.2–3 Hz, which can excite turbine-generator torsional modes, sub-synchronous resonance and voltage flicker.
  - The paper calls for utility-style specifications (ramp-rate limits, dynamic power range).
  - Sources: [arXiv 2508.14318](https://arxiv.org/html/2508.14318v2); [Microsoft Tech Community](https://techcommunity.microsoft.com/blog/azurecompute/power-stabilization-for-ai-training-datacenters/4460937); [The Register](https://www.theregister.com/2025/08/22/microsoft_nvidia_openai_power_grid)
- **GB200 power smoothing:**
  - The GB200 offers programmable ramp-up and ramp-down rates, a minimum power floor (MPF) and a stop delay.
  - A high floor costs about 10.5% energy overhead in simulation.
  - The MPF is capped at 90% of TDP. That leaves a 20% dynamic range, which may exceed utility limits of about 10%.
  - Storage is the most energy-efficient fix but costly in capacitance, space and embodied carbon.
  - Recommended split: storage for steady-state fluctuations, GPU smoothing (software and hardware) for ramps and corner cases.
  - Sources: [Microsoft Tech Community](https://techcommunity.microsoft.com/blog/azurecompute/power-stabilization-for-ai-training-datacenters/4460937); [arXiv 2508.14318v2](https://arxiv.org/html/2508.14318v2)
- **GB300 NVL72:** Power shelves add energy storage, including electrolytic capacitors. The shelf reportedly cuts grid-facing peak power by 30% versus GB200 (trade press) — [Data Centre Magazine](https://datacentremagazine.com/news/how-nvidia-gb300-nvl72-provides-data-centres-steady-ai-power)
- **Multi-timescale storage:** Supercapacitors for sub-second spikes and facility batteries for longer swings are reportedly in NVIDIA's 800 VDC notes (secondary, unverified) — [TheValueist on X](https://x.com/TheValueist/status/1984753651148050467)
- **Further academic work:**
  - EasyRider, on mitigating power transients — [arXiv 2604.15522](https://arxiv.org/pdf/2604.15522)
  - Operational risks and stability sensitivity studies of large data-center loads — [arXiv 2510.05437](https://arxiv.org/pdf/2510.05437)
  - Modal analysis of spatial load correlation — [arXiv 2606.13847](https://arxiv.org/pdf/2606.13847)
  - A pre-dispatch resonance safety criterion for AI clusters — [arXiv 2606.22096](https://arxiv.org/pdf/2606.22096)
  - HV-breaker-switched braking resistors for GW-scale data-center resilience — [arXiv 2512.21295](https://arxiv.org/pdf/2512.21295)
- **Harmonics:** Utilities have documented harmonic impacts from synchronized computing loads — [The Register](https://www.theregister.com/2025/08/22/microsoft_nvidia_openai_power_grid)
- **Commercial BESS smoothing:** Vendors such as Torus market battery-based load smoothing (marketing material) — [Torus](https://torus-prod.zaneray.com/ai-load-management)

### Inferences
- **Two distinct dynamic risks need different mitigations:**
  1. Fault-induced load loss (voltage sensitivity of UPS transfer logic). Fixed by ride-through settings: widening UPS input tolerance and delaying transfer, coordinated with grid auto-reclose. Also by controlled, staggered reconnection.
  2. Workload-induced oscillation in the 0.2–3 Hz band. Fixed by GPU power capping and smoothing, rack capacitors and BESS with fast (about 100 ms) response.
- **Escalation:** Event magnitude in Northern Virginia has grown about 2.5x in two years (1.5 GW to 3.8 GW). The largest single contingencies designed into the Eastern Interconnection are of a similar order, which is why PJM and NERC are moving to mandatory standards.
- **Regional relevance:** For India and GCC grids with smaller system inertia per GW of data-center load, these risks may be proportionally larger. No source was found on CEA/CTU or GCCIA grid-code treatment.

### Gaps
- Exact NERC recommendation text and numeric ride-through curves (ERCOT NOGRR282 final, PJM proposal) were not retrieved.
- Harmonic spectra and IEEE 519 compliance data for AI campuses: no source found.
- India (CEA Technical Standards for Connectivity, IEGC 2023), GCC grid codes and EU (Network Code Demand Connection, RfG) treatment of large data-center loads: not researched.

## Cooling power, PUE and WUE

### Takeaway
Global average PUE has been flat at about 1.54–1.56 for six years (Uptime 2025). Hyperscalers run about 1.10–1.15. Liquid cooling lowers total energy more than PUE shows, because it removes server-fan power, which counts as IT load. US data centers used 176 TWh (4.4% of US electricity) in 2023, rising to 325–580 TWh by 2028 (LBNL). Globally, the IEA puts consumption at 415 TWh in 2024 rising to about 945 TWh in 2030.

### Cited Findings
- **Uptime Institute 2025 survey:** Average PUE showed little change for the sixth consecutive year, held back by legacy infrastructure and regional cooling barriers. The weighted average "hovers above 1.5" — [Uptime Global Survey 2025](https://intelligence.uptimeinstitute.com/resource/uptime-institute-global-data-center-survey-2025); [Uptime PUE trends, Oct 2025](https://intelligence.uptimeinstitute.com/resource/mapping-pue-trends-data-center-region-age-and-size)
- **Figures from secondary sources:** 2025 average about 1.54 and 2024 about 1.56. Hyperscale about 1.10–1.15, colo and enterprise about 1.58–1.80 — [mgrid.org](https://mgrid.org/2025/10/01/uptime-institute-data-center-pue-stagnation-2025-liquid-cooling/); [Upsite](https://www.upsite.com/blog/data-center-trends-rack-density-rises-while-pue-and-outage-frequency-remain-flat/)
- **LBNL (December 2024):** US data-center use was 58 TWh (2014) and 176 TWh (2023, 4.4% of US electricity). Projected use is 325–580 TWh by 2028, or 6.7–12%. Demand more than doubled between 2017 and 2023, driven by AI servers — [LBNL](https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/); [DOE](https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers)
- **IEA Energy & AI (2025):**
  - 415 TWh in 2024 (about 1.5% of global electricity), about 945 TWh by 2030 and about 1,200 TWh by 2035 (base case).
  - Growth has run about 12% per year since 2017.
  - Regional shares in 2024: US 45%, China 25%, Europe 15%.
  - Data centers account for nearly half of US demand growth to 2030.
  - Sources: [IEA](https://www.iea.org/reports/energy-and-ai/executive-summary); [S&P Global](https://www.spglobal.com/commodity-insights/en/news-research/latest-news/electric-power/041025-global-data-center-power-demand-to-double-by-2030-on-ai-surge-iea)
- **Vertiv/NVIDIA liquid-cooling study:** In a 1–2 MW, 50-rack Baltimore site, a staged transition to direct-to-chip cooling cut total power about 9%, but PUE moved only from 1.38 to 1.34 because fan power is counted as IT load. About 75% of rack heat can be captured by D2C. TUE is suggested as a better metric — [Vertiv](https://www.vertiv.com/en-emea/about/news-and-events/articles/blog-posts/quantifying-data-center-pue-when-introducing-liquid-cooling/)

### Inferences
- **Cooling electrical load (practice, not sourced here):**
  - Chiller compressors, CDUs and pumps, and dry-cooler or cooling-tower fans make up most of the non-IT load. At PUE 1.5, non-IT load is about 33% of the total; at PUE 1.15, about 13%.
  - D2C allows warm-water (30–45 °C) supply with extended economizer hours, which is especially valuable in hot GCC and Indian climates where chiller-free operation is otherwise limited.
- **Electrical design consequence:** Cooling loads (pumps, CDUs) that must ride through to prevent GPU thermal trips are increasingly placed on UPS. This raises UPS sizing beyond IT load alone.

### Gaps
- WUE benchmarks were not retrieved from LBNL, Uptime or hyperscaler sustainability reports. The industry-cited value of about 1.8 L/kWh is unverified.
- No primary data was found on the cooling share of total energy, or on immersion versus D2C electrical loads.
- No regional PUE data was found for India or GCC.

## Relevant standards

### Takeaway
The standards stack spans:
- **UPS performance:** IEC/EN 62040-3.
- **Facility topology and availability:** Uptime Tier I–IV, TIA-942 Rated-1 to 4, EN 50600 Availability Classes 1–4.
- **Power quality and design:** IEEE 3006 series, IEEE 1100, IEEE 519.
- **BESS fire safety:** NFPA 855, UL 9540/9540A.
- **Grid compliance:** emerging NERC, ERCOT and PJM large-load ride-through rules.

Primary text for most of these was not retrievable in this session.

### Cited Findings
- **IEC/EN 62040-3:** Defines UPS performance classification (VFI/VI/VFD plus output waveform and dynamic performance codes, e.g., VFI-SS-111) and the efficiency test method — [EU JRC Code of Conduct](https://e3p.jrc.ec.europa.eu/sites/default/files/2023-09/code_of_conduct_ups_16032011.pdf); [Vertiv guide spec](https://www.vertiv.com/globalassets/shared/liebert-exl-s1-400-500kva-guide-specification.rtf)
- **Uptime Tier III / IV:** concurrently maintainable versus fault tolerant (see the UPS section) — [TechTarget](https://www.techtarget.com/it-infrastructure/tip/Data-center-tiers-and-why-they-matter-for-uptime)
- **UL 9540A:** thermal-runaway test basis for LFP UPS and BESS — [BICSI study guide](https://open-exam-prep.com/study-guides/bicsi-dcdc/ch07-electrical-distribution/sec03-ups-systems-batteries-sizing)
- **OCP specs:** ORV3 / Mt. Diablo v1.0.0 (±400 VDC) — [OCP](https://www.opencompute.org/wp-content/uploads/2026/10/OCP-Specification-Mt.-Diablo-Disaggregated-Power-Rack-Specification-v1.0.0.pdf)
- **NERC, ERCOT and PJM large-load rules:** see the power-quality section — [NERC draft SAR](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/draft_sar_computational_load_disturbance_performance-1.pdf); [ERCOT NOGRR282](https://www.ercot.com/files/docs/2026/05/11/282NOGRR-30-ERCOT-Comments-051126.docx)

### Inferences
- **Standards by region (general knowledge, not sourced here):**
  - **US:** NEC/NFPA 70 (Article 645, Article 708 for COPS), NFPA 110 (emergency and standby power), NFPA 855 and IEEE 3006.x / 1100 / 519. Uptime Tiers and TIA-942 dominate certification.
  - **EU:** EN 50600 (incl. 50600-2-2 power distribution and 50600-4-2 PUE, aligned with ISO/IEC 30134) plus the EU Energy Efficiency Directive data-center reporting obligation (≥500 kW IT).
  - **India:** Uptime and TIA-942 certification are common. Facilities must comply with CEA regulations and CPCB DG norms.
  - **GCC:** Uptime certification is widely used. Local utility codes (DEWA, ADDC/TAQA, SEC) govern connection.

### Gaps
- Primary texts of IEEE 3006.x, IEEE 1100, TIA-942-C, EN 50600, NFPA 855 (2026 edition) and Uptime Tier Standard: Topology were not retrieved. Clause-level requirements must be verified from the standards themselves.
- Hosts that need to be allowed for a fuller follow-up: nerc.com, arxiv.org, developer.nvidia.com.
