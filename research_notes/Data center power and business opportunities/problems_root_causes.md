# Key Problems in Data Center Development and Operation (2023-2026): Symptoms, Root Causes, Solutions

Scope note: global, with India/GCC emphasis. Research done Oct 2026 through web search (about 19 queries). Most citations are trade press or secondary summaries of primary reports (Uptime, NERC, Wood Mackenzie, LBNL). Where a primary document was not retrieved, that is flagged. "Confirmed" = stated by an official investigation, regulator order or the primary report author. "Hypothesis/speculation" = everything else.

---

## 1. Grid interconnection queues and power availability delays

### Takeaway
Power availability, not land or capital, is the binding constraint in every major hub: de facto connection moratoria in Dublin (since 2022, nothing new before ~2028), Amsterdam (congestion to 2030+), central Frankfurt (upgrades not before the 2030s), London/UK (5-7 year queues), and Singapore (2019-2022 moratorium, then rationed allocation). The root cause is that large-load demand arrives in 1-3 years while transmission takes 5-10 years, combined with clustering of demand in a few metro nodes.

### Cited Findings
**Symptoms / evidence**
- Ireland: since January 2022 EirGrid has imposed a de facto moratorium on new data center connections in greater Dublin; no new applications expected to get a grid connection before 2028 — [DCD](https://www.datacenterdynamics.com/en/news/eirgrid-says-no-new-applications-for-data-centers-in-dublin-till-2028); dozens of projects cancelled or in limbo (Interxion/Digital Realty paused a $300m expansion; Equinix paused Clondalkin; Microsoft, AWS also paused) — [DCD](https://datacenterdynamics.com/en/news/interxion-pauses-plans-for-300-million-expansion-in-dublin), [DCD](https://www.datacenterdynamics.com/en/news/microsoft-aws-equinix-join-list-of-companies-pausing-data-center-projects-in-dublin/); Google said the moratorium made further Irish investment "impossible" — [DCD](https://www.datacenterdynamics.com/en/news/google-data-center-moratorium-makes-further-investments-in-irish-infrastructure-impossible).
- Ireland policy (2021): CRU rejected a national ban ("not a suitable response") but allowed location limits and required on-site generation/storage matching demand — [DCD analysis](https://www.datacenterdynamics.com/en/analysis/dublin-and-data-centers-the-end-of-the-road/). (2025 CRU final large-energy-user connection decision: not retrieved; see Gaps.)
- Amsterdam/Netherlands: grid operators said in 2024 congestion would persist until at least 2030 with possible local outages from 2026 — [W.Media / CBRE](https://w.media/special-feature-flap-d-markets-plagued-by-grid-constraints-and-moratoriums-cbre/); Netherlands reported waits of up to 10 years for new data-center connections, longest among surveyed jurisdictions — [PPC Land summary of Ember](https://ppc.land/dutch-grid-crisis-exposes-europes-ai-energy-infrastructure-gap/); a Sept 2026 piece claims TenneT congestion has frozen new hyperscale capacity since 2023 with relief ~2029 (single source, uncorroborated) — [Datacentres.com](https://www.datacentres.com/news/amsterdam-data-centre-market-1-340-mw-live-as-tennet-s-grid-congestion-locks-out-slot2-2026-09-08).
- Frankfurt: CBRE (Global DC Trends 2026) says central Frankfurt grid upgrades unlikely before the 2030s; projects moving ~40 km out — [W.Media / CBRE](https://w.media/special-feature-flap-d-markets-plagued-by-grid-constraints-and-moratoriums-cbre/).
- London/UK: CBRE says development limited by power availability, high energy costs, liquid-cooling requirements and supply chain; Ember puts UK grid queues at 5-7 years — [W.Media / CBRE](https://w.media/special-feature-flap-d-markets-plagued-by-grid-constraints-and-moratoriums-cbre/), [Ember, Grids for data centres in Europe (2025)](https://ember-energy.org/latest-insights/grids-for-data-centres-ambitious-grid-planning-can-win-europes-ai-race/).
- Singapore: moratorium 2019-2022; 2022 pilot DC-CFA targeted ~60 MW, ~80 MW awarded to four operators in 2023; May 2024 Green Data Centre Roadmap aims for at least 300 MW more, prioritising green/efficient operators — [Reed Smith](https://www.reedsmith.com/en/perspectives/2025/11/singapores-data-centre-expansion-jurong-island-sustainable-growth), [Capacity Media](https://capacitymedia.com/article/2davfx8ylwhh1au8329kw/news/singapore-to-free-up-300mw-for-data-centres). Some coverage says the 300 MW is to be unlocked through efficiency in existing sites (conflicting framing) — [DCD](https://datacenterdynamics.com/en/news/singapore-to-unlock-300mw-of-data-center-capacity-through-industry-energy-efficiency-initiatives). As of late 2025 "DC-CFA2" had not launched — [Reed Smith](https://www.reedsmith.com/en/perspectives/2025/11/singapores-data-centre-expansion-jurong-island-sustainable-growth). BMI argued 300+80 MW is too little to bring large-scale investment back — [DCD](https://www.datacenterdynamics.com/en/news/singapore-data-center-roadmap-unlikely-to-drive-investment-report/).
- US demand scale: LBNL/DOE (Dec 2024, LBNL-2001637) says data center load tripled over the last decade and is projected to double or triple by 2028 — [DOE](https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers), [LBNL](https://eta-publications.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report). (Widely reported figures from the report — ~176 TWh / ~4.4% of US electricity in 2023 and 6.7-12% by 2028 — were not verified in the snippets retrieved; check the PDF.)
- India: constraint is local, not national; data centers are clustered in five metros (incl. Mumbai, Chennai); many last-mile transmission lines cannot serve a 1 GW campus; Equinix executive questioned whether substations would be upgraded in time — [Bloomberg Tax](https://news.bloombergtax.com/daily-tax-report-international/india-moves-to-lure-data-centers-despite-land-energy-challenges).

**Root causes (5-whys chain supported by sources)**
1. Why can't projects connect? Local substations/transmission at the hub node are full — [Ember](https://ember-energy.org/latest-insights/grids-for-data-centres-ambitious-grid-planning-can-win-europes-ai-race/).
2. Why are they full? Demand is clustered in a few metros (FLAP-D, NoVA, Mumbai/Chennai) — [W.Media/CBRE](https://w.media/special-feature-flap-d-markets-plagued-by-grid-constraints-and-moratoriums-cbre/), [Bloomberg Tax](https://news.bloombergtax.com/daily-tax-report-international/india-moves-to-lure-data-centers-despite-land-energy-challenges).
3. Why not expanded? Grid planning was reactive/not anticipatory, and transmission build is multi-year while DC demand arrives quickly — [Ember](https://ember-energy.org/latest-insights/grids-for-data-centres/).
4. Why reactive? Utilities/TSOs plan on firm demand, and speculative or duplicate requests inflate queues (inference; see Inferences). In India, DISCOMs are financially weak due to subsidised farm/household tariffs, limiting capex — [Bloomberg Tax](https://news.bloombergtax.com/daily-tax-report-international/india-moves-to-lure-data-centers-despite-land-energy-challenges).
5. Underlying: equipment supply constraints (Section 2) slow even funded upgrades.

**Who is affected:** developers/hyperscalers (stranded sites, relocation), host economies (lost investment — Ireland/Singapore), other grid users competing for capacity.

**Solutions being applied**
- Regulatory: Ireland requires on-site dispatchable generation/storage and location limits — [DCD](https://www.datacenterdynamics.com/en/analysis/dublin-and-data-centers-the-end-of-the-road/); Singapore allocates capacity competitively on sustainability/economic value criteria — [Reed Smith](https://www.reedsmith.com/en/perspectives/2025/11/singapores-data-centre-expansion-jurong-island-sustainable-growth); Texas SB6 (2025) imposes interconnection-study fees, disclosure of backup generation, and curtailment obligations — [Sidley](https://www.sidley.com/en/insights/publications/2025/11/how-new-law-transforms-large-load-power-projects-in-texas).
- Technical/commercial: relocation to secondary sites (Frankfurt periphery; Nordics and Southern Europe forecast faster growth) — [DCD](https://www.datacenterdynamics.com/en/news/nordics-and-southern-europe-to-see-110-data-center-demand-growth-by-2030-report/); Ember recommends anticipatory grid planning and steering DCs to grid-rich locations — [Ember](https://ember-energy.org/latest-insights/grids-for-data-centres-ambitious-grid-planning-can-win-europes-ai-race/); on-site/behind-the-meter supply (e.g., Equinix Mumbai met 60% of power from solar for two months) — [Bloomberg Tax](https://news.bloombergtax.com/daily-tax-report-international/india-moves-to-lure-data-centers-despite-land-energy-challenges); India states (Tamil Nadu, Telangana) offer dual feeds; Maharashtra subsidised power — [The India Forum (PDF)](https://www.theindiaforum.in/sites/default/files/article_pdf/2026/09/08/2100-1788847261.pdf).

### Inferences
- Queue inflation from speculative requests is a likely contributor (it motivated the financial-commitment tariffs in Section 5), but I did not retrieve a source quantifying speculative share of queues.
- Moratoria do not stop demand; they redistribute it to secondary markets (Johor for Singapore, periphery of Frankfurt, Nordics), which then face their own grid limits.

### Gaps
- Dominion/PJM large-load queue size (often cited ~40 GW contracted) and wait times (often quoted as up to ~7 years in NoVA) were not retrieved from a primary source in this session.
- The 2025 CRU final decision on large-energy-user connections (Ireland) was not retrieved.
- Singapore grid-specific constraint data and Johor spillover numbers not retrieved.

---

## 2. Supply-chain bottlenecks: transformers, switchgear, gas turbines, generators

### Takeaway
Large power transformers average ~2.5 years lead time (128 weeks; GSUs 144 weeks), prices up ~77% since 2019, and the US runs a ~30% supply deficit met 80% by imports. Gas-turbine OEM order books (GE Vernova 116 GW, Siemens Energy 69 GW) push new deliveries toward 2029-2031. Root causes: decades of under-investment in manufacturing capacity, a single domestic GOES supplier, specialised labour, tariffs, and a simultaneous demand surge from data centers, renewables, electrification and grid replacement.

### Cited Findings
- Wood Mackenzie (Q2 2025): power transformer lead times average 128 weeks; generator step-up (GSU) 144 weeks; distribution transformers 30 weeks (down from 100+ week peak in 2023) — [pv magazine](https://www.pv-magazine.com/2025/08/15/us-transformer-supply-may-fall-sharply-in-2025-says-wood-mackenzie/), [Solar Builder](https://solarbuildermag.com/news/less-than-meets-the-eye-transformer-shortages-could-derail-u-s-solar-and-grid-projects-woodmac-warns/).
- Wood Mackenzie: 2025 US supply deficit ~30% for power transformers and ~10% for distribution transformers; imports ~80% of power and ~50% of distribution transformer supply — [pv magazine](https://www.pv-magazine.com/2025/08/15/us-transformer-supply-may-fall-sharply-in-2025-says-wood-mackenzie/).
- Power-transformer prices up ~77% since 2019; tariffs (incl. 50% copper tariff from Aug 2025) raise both imported and domestic unit costs — [Solar Builder / WoodMac](https://solarbuildermag.com/news/less-than-meets-the-eye-transformer-shortages-could-derail-u-s-solar-and-grid-projects-woodmac-warns/), [EEPower](https://eepower.com/market-insights/transformer-supply-chain-woes-persist-as-energy-demand-grows/).
- Lead times for some units reported up to four years — [pv magazine USA](https://pv-magazine-usa.com/?p=20370).
- GOES: Cleveland-Cliffs is the only US producer of grain-oriented electrical steel — [Solar Builder / WoodMac](https://solarbuildermag.com/news/less-than-meets-the-eye-transformer-shortages-could-derail-u-s-solar-and-grid-projects-woodmac-warns/), [National Law Review](https://natlawreview.com/article/grids-bottleneck-isnt-just-money-its-materials).
- ~$1.8bn of North American transformer manufacturing expansions announced; pad-mount three-phase shortages expected to worsen due to data centers, manufacturing and EV charging — [Solar Builder / WoodMac](https://solarbuildermag.com/news/less-than-meets-the-eye-transformer-shortages-could-derail-u-s-solar-and-grid-projects-woodmac-warns/).
- POWER Magazine (2026) frames the question as "shortage, scramble or self-inflicted crisis" (i.e., partly due to non-standard specs and fragmented ordering) — [POWER](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/) (content not fetched; title only).
- Gas turbines: GE Vernova backlog 116 GW at end Q2 2026 (≈53 GW firm + 63 GW slot reservations), up from 83 GW at end 2025, deliveries slated into 2031; Siemens Energy 69 GW backlog; Mitsubishi large-frame back orders 35 GW; ~20% of GEV backlog tied to data centers; global capacity ~60-70 GW/yr vs ~110 GW orders — [OilPrice](https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html), [Gainer Substack](https://mitchgainer.substack.com/p/green-fundamentals-gas-gridlock) (secondary sources). Earlier reporting: lead times past 2029, and OEMs telling customers to plan 7-8 years ahead; long lead times are killing some proposed gas plants — [Power Engineering](https://www.power-eng.com/gas/turbines/long-lead-times-are-dooming-some-proposed-gas-plant-projects/).
- GE Vernova plans to raise annual turbine capacity from 20 GW to 30 GW by 2030 (contingent on orders) — [OilPrice](https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html).

**Root causes (5-whys)**
1. Why long lead times? Orders exceed factory capacity (transformers −30% deficit; turbines ~110 GW orders vs 60-70 GW/yr).
2. Why insufficient capacity? OEMs did not expand after the flat-demand 2010s; turbine OEMs cut capacity when gas orders slumped (inference from capacity expansion plans now being conditional on firm orders).
3. Why slow to expand now? Specialised inputs (GOES from one US producer; copper subject to tariffs) and skilled winding/assembly labour; OEMs fear a demand bust and want firm orders/reservation fees before adding capacity.
4. Why demand surge? Data centers coincide with renewables interconnection, electrification, ageing grid replacement.

**Who is affected:** utilities (substation upgrades delayed), developers (energisation delayed even with grid capacity), behind-the-meter gas strategies.

**Solutions:** OEM capacity expansion (~$1.8bn transformers; GEV to 30 GW/yr); slot-reservation agreements and early procurement/framework agreements by hyperscalers; standardisation of transformer specs (argued in POWER piece, inferred); alternative on-site generation (reciprocating engines, aeroderivatives, fuel cells — not quantified here).

### Inferences
- Slot-reservation agreements (63 GW of GEV backlog) suggest part of the backlog is optionality and may not convert; actual scarcity could be overstated in headline backlog numbers.

### Gaps
- HV switchgear and diesel/gas generator lead times: no quantitative source retrieved.
- India/GCC-specific transformer lead times not found.

---

## 3. Outages and failures (Uptime analysis, fires)

### Takeaway
Outage frequency is declining (53% of operators had an outage in past 3 years vs 78% in 2020), but power remains the leading cause of impactful outages (54%), and procedure failures behind human-error outages rose ten points. Lithium-ion UPS batteries are the common element in the two highest-profile recent fires (Alibaba/Digital Realty Singapore 2024; Korea NIRS 2025); the OVHcloud 2021 cause was never conclusively determined, but building design (no automatic suppression, delayed power cutoff) explains the scale.

### Cited Findings
**Uptime Institute Annual Outage Analysis 2025 (7th edition, May 2025)**
- Power is the largest cause of impactful outages at 54% — [Uptime press release](https://uptimeinstitute.com/about-ui/press-releases/uptime-announces-annual-outage-analysis-report-2025), [Business Wire](https://www.businesswire.com/news/home/20250506733553/en/Uptime-Announces-Annual-Outage-Analysis-Report-2025).
- 53% of operators reported an outage in the past three years, down from 78% in 2020; fourth straight year of decline — [Data Center Knowledge](https://www.datacenterknowledge.com/outages/data-center-outages-decline-for-fourth-straight-year-but-issues-persist).
- Failure to follow procedures rose by ten percentage points from 2024; the overwhelming majority of human-error outages involve ignored or inadequate procedures; The Register puts human error as a factor in two-thirds to four-fifths of major outages — [The Register](https://www.theregister.com/2025/05/07/human_error_a_factor_in).
- Report links new risks to AI-driven power/cooling strain — [FMLink](https://www.fmlink.com/?p=49764).

**OVHcloud SBG2, Strasbourg, 10 Mar 2021 (official BEA-RI report, May 2022)**
- Cause not conclusively determined (official). Leading hypothesis: water leak on a power inverter; sensors showed anomalous moisture on one inverter in the hour before the fire; other possibilities included maintenance that morning and an inverter outside normal range — [DCD](https://datacenterdynamics.com/en/news/ovhcloud-sbg2-fire-report-reveals-water-was-detected-near-power-inverters), [W.Media](https://w.media/what-was-the-possible-cause-of-ovhcloud-data-centre-fire-in-2021/).
- Confirmed spread factors: no automatic fire extinguishing system, delayed electrical cutoff, toxic fumes from lead batteries; (widely reported free-cooling "chimney" design also cited) — [W.Media](https://w.media/what-was-the-possible-cause-of-ovhcloud-data-centre-fire-in-2021/), [Gigazine](https://gigazine.net/news/20220610-ovhcloud-fire-report-bea-ri).

**Digital Realty SIN11 / Alibaba Cloud, Singapore, 10 Sep 2024**
- Alibaba status updates: "caused by the explosion of lithium batteries"; fire in third-floor battery rooms; SCDF suggested a lithium-ion UPS system. Digital Realty did not publicly disclose an official cause (no official root cause published as found) — [DCD](https://datacenterdynamics.com/en/news/lithium-ion-fire-causes-emergency-power-shutdown-at-digital-realty-data-center-in-singapore), [The Register](https://www.theregister.com/2024/09/10/digtal_realty_singapore_datacenter_fire/).
- Secondary damage: firefighting water accumulation created short-circuit risk forcing emergency power shutdown; servers had to be dried; firefighters still on site after 24 hours — [DCD](https://www.datacenterdynamics.com/en/news/alibaba-carefully-dries-servers-after-data-center-fire/), [W.Media](https://w.media/24-hours-on-firefighters-still-at-digital-realtys-singapore-data-center/).

**Korea NIRS Daejeon, 26 Sep 2025**
- Fire began ~8:20 pm in a server room; origin confirmed by joint police/fire/ministry probe as a lithium-ion UPS battery; sparks occurred while outsourced workers were relocating UPS systems to the basement (Interior Ministry statement) — [DCD](https://www.datacenterdynamics.com/en/news/south-korea-data-center-fire-government-services-could-be-offline-for-a-month/), [Korea Herald](https://www.koreaherald.com/article/10588621).
- Battery: LG Energy Solution cells, LG CNS BMS; installed Aug 2014, ~1 year past expected service life — [Korea Times](https://www.koreatimes.co.kr/amp/business/companies/20250928/govt-lg-face-scrutiny-after-state-data-center-fire).
- Speculation (not confirmed): workers may have removed wiring before cutting power, causing a short — [Korea Times](https://www.koreatimes.co.kr/amp/business/companies/20250928/govt-lg-face-scrutiny-after-state-data-center-fire).
- Police booked four people (one NIRS employee, three contractors) for professional negligence; six suspected batteries sent to National Forensic Service; police raided NIRS — [Asia News Network](https://asianews.network/?p=230800).
- Impact: 647 government services halted; services possibly offline for a month — [BEST Magazine](https://www.bestmag.co.uk/south-korea-data-centre-fire-halts-647-government-services/), [DCD](https://www.datacenterdynamics.com/en/news/south-korea-data-center-fire-government-services-could-be-offline-for-a-month/).

**Root causes (5-whys, NIRS as worked example; confirmed parts only to step 2)**
1. Why outage? Fire destroyed/forced shutdown of server room (confirmed).
2. Why fire? Li-ion UPS battery ignited during relocation work (confirmed origin; mechanism under forensic analysis).
3. Why did work ignite it? Possibly live disconnection / inadequate procedure (speculative).
4. Why so much impact? UPS batteries co-located with servers; ageing batteries past rated life; lack of geographically separate DR for key government systems (reported widely; DR point not verified here).
5. Systemic: maintenance done by outsourced staff under procedures that may not have been followed — aligns with Uptime finding that procedure failures drive human-error outages.

**Solutions:** Li-ion battery rooms with fire separation and off-gas detection, NFPA 855/UL 9540A testing (industry practice; not sourced here); automatic suppression and fast electrical isolation (lesson from OVH); procedure discipline/MOP-SOP compliance (Uptime); geographic redundancy/DR.

### Inferences
- Lithium-ion UPS adoption (higher energy density, longer life) introduces thermal-runaway risk that legacy fire strategies (water) handle poorly; both Singapore and Korea showed long burn times and water damage.

### Gaps
- Uptime 2025 cooling-specific share and 2026 report figures not retrieved.
- Final forensic report on NIRS cause not found (latest coverage April 2026).
- No official SCDF/Digital Realty root cause for SIN11 found.

---

## 4. Grid-stability risks from large loads

### Takeaway
Data centers are now a bulk-system reliability risk: on 10 July 2024 about 1,500 MW of NoVA data-center load tripped to backup in response to a 230 kV fault sequence, and a Feb 2025 event dropped ~1,800 MW. Root cause is customer-side protection/UPS logic designed to protect IT, not the grid, plus AI training loads' rapid power swings. NERC has escalated to a Level 3 alert (May 2026) and a Reliability Guideline.

### Cited Findings
- 10 Jul 2024: lightning arrestor failure on a 230 kV line; auto-reclosing caused six faults in 82 seconds; ~1,500 MW (exclusively data center load) disconnected across 60 points/25 substations via customer-side protection; frequency peaked 60.047 Hz; voltage rose to 1.07 pu; load did not return for hours because many UPS systems require manual transfer back to grid. NERC incident review released 8 Jan 2025 — [DCD](https://datacenterdynamics.com/en/news/virginia-narrowly-avoided-power-cuts-when-60-data-centers-dropped-off-the-grid-at-once), [NS Energy](https://www.nsenergybusiness.com/analysis/nerc-on-data-centres-and-grid-voltage-disturbances/), [FERC-hosted NERC presentation](https://www.ferc.gov/sites/default/files/2025-04/Presentation%20NERC%20Seeks%20to%20Address%20Reliability%20Impacts%20from%C2%A0Large%20Load%20Integration_1.pdf).
- Feb 2025: ~1,800 MW data-center load loss in Loudoun/Fairfax — [FERC/NERC presentation](https://www.ferc.gov/sites/default/files/2025-04/Presentation%20NERC%20Seeks%20to%20Address%20Reliability%20Impacts%20from%C2%A0Large%20Load%20Integration_1.pdf).
- Claimed 22 Jul 2026 NoVA event with ~3,000 MW shifting to backup (single source, unverified) — [Texas RE newsletter](https://texasre.org/pages/newsletters/august2026/largeloadrisk).
- NERC recommendations: large-load modelling, consider registering large loads, possible new standards — [FERC/NERC presentation](https://www.ferc.gov/sites/default/files/2025-04/Presentation%20NERC%20Seeks%20to%20Address%20Reliability%20Impacts%20from%C2%A0Large%20Load%20Integration_1.pdf).
- NERC Large Loads Task Force white paper (July 2025): forced oscillations 0.1-30 Hz from AI workloads; one 200 MW training facility saw a 50 MW block ramp at 1.9 pu/s for ~250 ms; many AI training designs skip UPS and use checkpoint-restore, preferring to drop load rather than ride through — [HSI summary](https://hsi.com/blog/large-loads-reshaping-grid-reliability-and-nerc), [PNNL/NASPI slides](https://www.naspi.org/sites/default/files/2026-04/10-1_Chatterjee-PNNL_0.pdf).
- Oscillation mechanisms: low-frequency (0.1-1 Hz) resonates with inter-area modes; sub-synchronous (5-59 Hz) with generator torsional modes; WECC/PNNL studying AI fluctuation effects on hydro units — [PNNL/NASPI](https://www.naspi.org/sites/default/files/2026-04/10-1_Chatterjee-PNNL_0.pdf), [WECC](https://www.wecc.org/sites/default/files/documents/meeting/2026/16%20-%20ChatterjeeK%2C%20BiswasS%20-%20Effects%20of%20Power%20Fluctuations%20from%20AI%20Training%20Processes%20on%20Hydro%20Generator%20Systems_May%202026.pdf).
- NERC Level 3 alert (highest) on computational loads, 4 May 2026; May 2026 Reliability Guideline "Risk Mitigation for Emerging Large Loads"; AESO, ATC, ERCOT, PSEG-LI proposing oscillation amplitude limits — [Let's Data Science](https://letsdatascience.com/news/nerc-issues-level-3-alert-on-data-center-loads-5b6e48df), [Keentel](https://www.keentelengineering.com/nerc-large-loads-guide) (secondary).
- Texas SB6: remote-disconnect capability and emergency curtailment for large loads (≥75 MW) connected after 31 Dec 2025 — [Data Center Frontier](https://www.datacenterfrontier.com/energy/article/55298872/texas-senate-bill-6-a-bellwether-on-how-states-may-approach-data-center-energy-use).

**Root causes (5-whys, July 2024 event — supported by NERC review)**
1. Why did 1,500 MW vanish? Data centers' protection transferred to UPS/generators on repeated voltage dips.
2. Why? Protection settings tuned to protect IT from any disturbance; no grid ride-through requirement.
3. Why no requirement? Loads are not NERC-registered entities; no standards for load ride-through.
4. Why slow return? UPS-to-grid retransfer is manual at many sites.
5. Why risky now? Clustering — dozens of sites on the same transmission area respond identically, making a single fault a GW-scale event.

**Solutions:** NERC registration/standards for large loads; ride-through and oscillation-limit interconnection requirements; utility modelling requirements; on-site batteries/supercapacitors and software power smoothing for AI training (industry-proposed; draft Nvidia/Microsoft/OpenAI paper reported) — [EEPower](https://eepower.com/news/nerc-warns-ai-data-centers-threaten-grid-reliability/).

### Gaps
- Primary NERC Level 3 alert text and Reliability Guideline not retrieved.

---

## 5. Cost allocation and electricity tariffs

### Takeaway
PJM capacity prices rose ~10x and then hit court-imposed caps ($329.17/MW-day for 2026/27), attributed largely to data-center load forecasts plus plant retirements; ratepayers face bill increases. Regulators responded with large-load tariffs requiring minimum demand charges (AEP Ohio 85%, Dominion GS-5 85% T&D / 60% generation), long contracts, collateral and exit fees.

### Cited Findings
- PJM 2026/27 BRA cleared at the cap $329.17/MW-day (vs $269.92 in 2025/26); ~$16bn total, +9.5% — [E&E News](https://www.eenews.net/articles/pjm-power-prices-rise-to-meet-energy-demand/), [Penn Capital-Star](https://penncapital-star.com/2025/12/11/repub/energy-market-watchers-see-electric-bills-in-pa-other-states-rising-as-data-center-demand-continues/).
- Cap resulted from Pennsylvania Gov. Shapiro's challenge — [Ohio Capital Journal](https://ohiocapitaljournal.com/?p=35742).
- IEEFA: projected data center growth drove PJM capacity prices up by a factor of ~10 — [IEEFA](https://ieefa.org/resources/projected-data-center-growth-spurs-pjm-capacity-prices-factor-10).
- Dec 2025 (2027/28) auction also cleared at cap and failed to procure enough capacity to meet the 1-in-10 reliability standard (14.8% reserve margin) — [Sierra Club](https://www.sierraclub.org/pennsylvania/blog/2025/12/pjm-capacity-auction-ends-record-high-costs-again).
- Consumer advocates estimated 1.5-5% bill increases from the spike; NRDC projected ~$70/month increase for average PJM household by 2028 without reform (projection) — [Penn Capital-Star](https://penncapital-star.com/2025/12/11/repub/energy-market-watchers-see-electric-bills-in-pa-other-states-rising-as-data-center-demand-continues/), [Avanza Substack](https://avanzaenergy.substack.com/p/the-164-billion-reliability-tax-how).
- AEP Ohio: PUCO order 9 Jul 2025 for new/expanded loads >25 MW: pay at least 85% of subscribed demand for up to 12 years (incl. 4-year ramp), financial viability proof, exit fee of 36 months of minimum charges; rehearing by data-center firms denied — [POWER](https://www.powermag.com/regulator-approves-aep-ohios-landmark-data-center-tariff/), [Renewable Energy World](https://www.renewableenergyworld.com/energy-business/policy-and-regulation/policy-and-regulation/ohio-utility-regulators-approve-aeps-contested-data-center-tariff-proposal/), [DCD](https://www.datacenterdynamics.com/en/news/ohio-regulator-rejects-bid-from-data-center-firms-to-nix-newly-approved-rate-structure-for-large-load-users/).
- Dominion (Virginia SCC, Nov 2025 biennial review): new GS-5 class for ≥25 MW from 1 Jan 2027; minimum payments 85% of contracted T&D demand and 60% of generation demand; 14-year contracts; higher collateral; PEC argued 61% of upgrade costs would still fall on other ratepayers after 14 years — [Loudoun Now](https://www.loudounnow.com/news/scc-approves-new-data-center-rate-class-for-dominion/article_02d5fa0c-1ed8-4771-b57d-c24765739854.html), [Inside Climate News](https://insideclimatenews.org/news/07012026/virginia-regulators-approve-new-dominion-rates/).
- Texas SB6 (signed June 2025): interconnection standards, cost contribution for interconnection, disclosure of backup generation ≥50% of demand, curtailment — [SDxCentral](https://www.sdxcentral.com/news/texas-governor-approves-bill-mandating-data-centers-to-contribute-to-costs-of-interconnection-sdx/), [Pillsbury](https://www.pillsburylaw.com/en/news-and-insights/texas-sb6-transmission-fees-interconnected-standards-large-load-customers-colocated-loads.html).

**Root causes:** (1) bills rise because capacity/transmission costs are socialised; (2) capacity is short because load forecasts surged while dispatchable plants retired and new supply is slow to interconnect (IEEFA, E&E); (3) legacy tariffs had no mechanism to assign stranded-asset risk to speculative large loads; (4) forecasting relies on unfirm, duplicated data-center requests (inference).

**Who is affected:** residential/small business ratepayers in PJM states; developers (higher fixed costs, collateral); utilities (stranded-asset risk).

### Gaps
- PJM IMM quantification of data-center share of capacity cost not retrieved (IMM has publicly attributed a large share; not verified this session).

---

## 6. Water, heat, community opposition, moratoria, permitting and emissions

### Takeaway
Local opposition blocked or delayed $64bn of US projects (Mar 2023-Mar 2025) and ~$98bn more in Q2 2025 alone, driven by bills, water, noise, property values and green space, and it is bipartisan. Diesel backup generator fleets (177 air permits in Virginia by Nov 2024) are a permitting flashpoint.

### Cited Findings
- Data Center Watch: $18bn blocked + $46bn delayed in two years to March 2025 (16 projects); 142 activist groups in 24 states; 55% of opposing officials Republicans, 45% Democrats; follow-up: 20 projects / ~$98bn blocked or delayed late Mar-Jun 2025 — [DCD](https://www.datacenterdynamics.com/en/news/group-claims-64bn-in-us-data-center-projects-impacted-by-local-opposition-in-last-two-years/), [Virginia Mercury](https://virginiamercury.com/2025/05/21/report-highlights-community-pushback-stalling-64-billion-in-data-center-development-nationwide/), [Data Center Knowledge](https://www.datacenterknowledge.com/regulations/local-opposition-hinders-more-data-center-construction-projects).
- Caveat: two of the "blocked" projects ($14.5bn of $18bn) were relocated nearby rather than cancelled; Data Center Watch is funded by 10a Labs — [DCD](https://www.datacenterdynamics.com/en/news/group-claims-64bn-in-us-data-center-projects-impacted-by-local-opposition-in-last-two-years/).
- Virginia DEQ: 177 data center air permits listed (Nov 2024), mostly emergency diesel generator sets; a proposed variance to relax generator run limits (to let DCs go off-grid during grid stress) drew opposition and was scaled back/withdrawn after an industry-PJM solution — [Virginia Mercury](https://virginiamercury.com/2024/11/13/virginia-environmental-regulators-make-info-on-data-center-operations-more-publicly-accessible/), [Baxtel](https://baxtel.com/news/concerns-over-northern-virginia-diesel-generators-leads-to-deq-revising-its-relaxation-of-generator-restrictions).

**Root causes:** concentrated local externalities (noise, diesel emissions, water, land use, transmission lines) with diffuse benefits (few jobs post-construction); bill increases (Section 5) turn opposition into a regional political issue; low transparency on water/energy use.

**Solutions:** transparency (DEQ permit page), large-load tariffs, community benefit agreements, closed-loop/air cooling, zoning setbacks and noise standards, cleaner backup (gas, HVO, batteries) — mostly not quantified in retrieved sources.

### Gaps
- US national water figures (LBNL) not verified in snippets; local moratoria list (e.g., county-level pauses) not retrieved.

---

## 7. Skilled labour shortages, construction delays and cost overruns

### Takeaway
Staffing shortages are persistent: nearly two-thirds of operators struggle to hire or retain; reported 52% of shortages caused direct disruption (up from 43%). Construction backlog averages ~10.9 months. Hard data on cost overruns is thin.

### Cited Findings
- Uptime Global Survey 2025: nearly two-thirds of operators report difficulty retaining staff, finding qualified candidates, or both — [DCPost MEA](https://www.dcpostmea.com/?p=47346).
- Uptime Staffing Survey 2025 (Field Report 186; 864 respondents, Jul-Sep 2025): "staffing crisis persists"; recruiting qualified staff a top concern for colo and enterprise — [Uptime PDF](https://intelligence.uptimeinstitute.com/sites/default/files/2025-10/UI%20Field%20report%20186_UI%20Staffing%20Survey%202025%20-%20Staffing%20crisis%20persists.pdf).
- 52% of shortages caused direct disruptions, up from 43% (secondary, not confirmed in Uptime primary) — [Per Scholas](https://enterprise.perscholas.org/the-data-center-staffing-crisis-the-hidden-bottleneck-to-ai-growth/).
- ABC: data center contractors average 10.9 months backlog vs 8 months other sectors — [Per Scholas](https://enterprise.perscholas.org/the-data-center-staffing-crisis-the-hidden-bottleneck-to-ai-growth/).
- Claimed 439,000-worker construction shortfall (blog; no primary source) — [Introl](https://introl.com/fr/blog/us-data-center-construction-drop-first-since-2020).
- India: Yotta filing (2024) — projects normally 15-18 months taking 24-30 months due to approval complexity — [The India Forum (PDF)](https://www.theindiaforum.in/sites/default/files/article_pdf/2026/09/08/2100-1788847261.pdf).

**Root causes:** simultaneous megaproject demand (fabs, LNG, DCs) for the same electricians/commissioning engineers; ageing workforce; specialised skills for HV and liquid cooling; long training pipelines.

### Gaps
- No primary quantification of DC cost overruns (% over budget) found.

---

## 8. India- and GCC-specific problems

### Takeaway
India: power is a local distribution/transmission problem (DISCOM finances, last-mile lines), plus water stress in Mumbai/Chennai and slow state-level approvals. GCC: ambient >45-50°C and 60-90% reliance on gas-powered desalination make water and cooling energy the core trade-off; capacity is to triple to ~3.3 GW by 2030.

### Cited Findings
**India**
- DISCOMs financially weak from subsidised farm/household power; last-mile lines can't serve 1 GW campuses; demand concentrated in five cities — [Bloomberg Tax](https://news.bloombergtax.com/daily-tax-report-international/india-moves-to-lure-data-centers-despite-land-energy-challenges).
- Data center water use estimated ~150 billion litres/yr, could more than double by 2030; India uses >80% of available freshwater; Mumbai/Chennai among most water-stressed cities (estimates, secondary) — [Policy Circle](https://www.policycircle.org/industry/indias-data-centre-ambitions-budget/), [Let's Data Science](https://letsdatascience.com/news/india-builds-data-centres-straining-water-resources-1a99b412).
- Cooling overhead example: 100 units IT may need ~80 units cooling for GPU servers (analyst estimate, implies PUE ~1.8) — [Outlook Business](https://www.outlookbusiness.com/amp/story/magazine/will-ai-and-cloud-growth-push-indias-data-centres-to-the-edge-of-a-power-crisis).
- Jurisdiction: water is a State List subject, electricity Concurrent List; central standards bind states only if adopted; land conversion and right-of-way approvals with state/urban bodies; Yotta delays 15-18 → 24-30 months — [The India Forum (PDF)](https://www.theindiaforum.in/sites/default/files/article_pdf/2026/09/08/2100-1788847261.pdf).
- Solutions: treated wastewater reuse, rainwater harvesting, closed-loop cooling (uneven, low disclosure); state incentives (Maharashtra subsidised power; TN/Telangana dual feeds); on-site/open-access solar — [The India Forum (PDF)](https://www.theindiaforum.in/sites/default/files/article_pdf/2026/09/08/2100-1788847261.pdf), [Bloomberg Tax](https://news.bloombergtax.com/daily-tax-report-international/india-moves-to-lure-data-centers-despite-land-energy-challenges).

**GCC**
- Desalination (mostly gas-powered) supplies 60-90% of Gulf water; rainfall <100 mm/yr — [AGBI](https://www.agbi.com/analysis/ai/2025/05/thirsty-for-data-water-scarcity-challenges-gulfs-ai-ambitions/).
- Saudi data centers used ~15 billion litres in 2024 (FTI Consulting); GCC capacity to triple from ~1 GW to 3.3 GW by 2030; summer temps regularly >45°C — [Arab News](https://www.arabnews.pk/node/2612606/saudi-arabia).
- A 1 GW Saudi facility estimated at 1.5-5 million m³ water/yr; evaporative cooling could be 5-10x higher (rough estimate) — [Mobile Europe](https://www.mobileeurope.co.uk/?p=43494).
- Waterless cooling exists but costs more; Equinix AD1 uses water-cooled chillers — [AGBI](https://www.agbi.com/analysis/ai/2025/05/thirsty-for-data-water-scarcity-challenges-gulfs-ai-ambitions/).
- Khazna piloting treated sewage effluent; Khazna, DataVolt, Alfanar deploying liquid cooling claimed to cut cooling water up to 90% (unverified) — [Rest of World](https://restofworld.org/2025/gulf-ai-water-crisis/), [The National](https://www.thenationalnews.com/business/energy/2026/08/22/gulf-pours-billions-into-water-security-to-boost-ai-and-industry-ambitions/).
- Shift to air/liquid cooling and adiabatic-free chillers raises energy demand (water-energy trade-off) — [Gowling WLG](https://gowlingwlg.com/en-gb/insights-resources/articles/2025/building-and-powering-data-centres-in-the-gcc).

**Root causes:** heat (high cooling load, fewer free-cooling hours) → choice between water (evaporative, desalinated) and energy (dry/chiller) → both scarce or carbon-intensive; in India, institutional fragmentation (state vs centre) and DISCOM finances.

### Gaps
- Data localisation rules (India DPDP Act 2023 / 2025 Rules, RBI payment-data localisation; Saudi PDPL/NDMO, UAE rules) — not researched in this session; no sources retrieved.
- India grid reliability statistics (outage hours/voltage events) for DC zones not found.
- GCC grid reliability/large-load connection terms not found.
