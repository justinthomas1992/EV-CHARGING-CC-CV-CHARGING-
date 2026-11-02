# Why India Chose a 1,000 km HVDC Line Over Batteries for 6 GW of Rajasthan Solar

*A long-form follow-up to my LinkedIn post on the Barmer-II transmission award.*
*Original post: https://lnkd.in/p/efqjrxSx*

---

## The headline

On 2 September 2026, POWERGRID won the Barmer-II transmission scheme. It is a ±800 kV HVDC link rated at 6,000 MW, running about 1,000 km from western Rajasthan to South Kalamb in Maharashtra. The quoted annual transmission charge is ₹32.44 billion (₹3,244 crore) (Renewable Watch). GE Vernova T&D India is supplying the converter terminals (SolarQuarter).

What makes it interesting is less the size than the decision behind it. Early estimates suggested that a battery option, 6 GW for 4.25 hours, could be cheaper than a new corridor. CTUIL's detailed costing reversed that. The National Committee on Transmission (NCT) then chose LCC HVDC as the option with the lowest capital cost: an estimated ₹24,974 crore, with 48 months to commission the first pole (T&D India).

So a regulator looked at the "batteries instead of wires" argument for a large renewable energy zone (REZ), costed it properly, and chose the wire. Here is why, and what it means for people building solar, storage and transmission.

---

## Root cause, three levels down

### 1. Technical: moving energy is a different job from shifting it in time

Barmer's problem is distance. The solar is in the Thar desert, and the demand is in the load centres of western and central India. A battery shifts energy **in time**. A transmission line moves it **in space**.

A 25.5 GWh battery (6 GW × 4.25 h) at Barmer can hold midday solar and release it in the evening. But it releases it at Barmer, into the same congested network that stopped the energy getting out in the first place. Storage at the source cannot replace a corridor when the binding limit is export capacity. It can only change *when* you hit that limit.

### 2. Commercial: the two assets are paid for different services

- **The HVDC line** is a regulated transmission asset, built under BOOT and paid on **availability**. If the line is available, it earns its charge, however much energy flows.
- **A BESS** is paid for capacity and energy services. A recent reference is the Gujarat standalone storage tender at about ₹2.80 lakh/MW/month with no viability gap funding (VGF).

These revenue models are tied to different products. Comparing the two price tags directly is like comparing a road toll with a warehouse lease.

### 3. System: without a corridor, the energy is stranded whatever you store

Solar far from load with no export path is stranded capacity. Adding storage behind the bottleneck raises the value of each MWh you *can* export, but it does not create export capacity. The corridor is the precondition. Storage optimises within it.

---

## The numbers (illustrative, not like-for-like)

| Item | Value | How it is derived |
|---|---|---|
| HVDC annual charge | ₹3,244 crore/yr | Quoted: ₹32.44 bn |
| HVDC estimated capex | ₹24,974 crore | NCT estimate |
| HVDC charge per MW-month | ≈ ₹0.45 lakh | 3,244 cr ÷ 6,000 MW ÷ 12 |
| BESS reference tariff | ₹2.80 lakh/MW/month | Gujarat tender, no VGF |
| BESS 6 GW at that tariff | ≈ ₹20,160 crore/yr | 6,000 × ₹2.80 lakh × 12 |
| BESS energy | 25.5 GWh | 6 GW × 4.25 h |

On this crude basis, a battery fleet of the same MW rating costs about **six times** the corridor's annual charge. But I want to be clear about what this table does **not** show:

- The BESS figure buys a service (4-hour shifting, firming, ancillary support) that the line does not provide.
- The line buys a service (1,000 km of bulk transfer) that the battery cannot provide at all.
- Tariffs, durations, degradation, augmentation and asset lives all differ.

The gap is large and points one way, but it measures two different services. It is not a head-to-head on equal terms.

### A rough break-even framing

To give a feel for the question I asked at the end of the post: spreading the corridor's ₹24,974 crore capex over the 25.5 GWh battery it was compared against gives about **₹9,800/kWh** (roughly US$115/kWh at ₹85/$). That is a very crude "capex parity" marker. A real comparison has to account for round-trip losses, cycle life, augmentation, the network reinforcement that a battery-only option would *still* need, and the fact that a 4-hour battery does not cover multi-day or seasonal gaps. Treat it as a starting point for discussion, not a threshold.

---

## Storage is a complement, not a substitute

The most useful insight is the reframe. A solar-only corridor is well used for a few hours a day and lightly used the rest of the time. Storage **behind** the corridor can:

- **Relieve curtailment** in hours when generation exceeds line capacity.
- **Raise corridor utilisation** by pushing stored midday energy through the line in the evening.
- **Support ramping** and local voltage and frequency services at the REZ.
- **Ease local congestion** on the AC collection network feeding the converter station.

Seen this way, the right question is not "line *or* battery?" but "what size of battery makes the line worth more?"

---

## What developers and engineers should do

1. **Place BESS where it adds capacity value**, not as a substitute for a corridor.
2. **Pitch storage as a complement:** curtailment relief, ramping and local congestion management.
3. **Link solar COD and PPA schedules to the corridor date**, not the plant date. A finished plant with no export path is a stranded asset.
4. **Price 48–54 months of corridor risk** into PPAs, financing and contingency, including commissioning one pole at a time.
5. **Track the NCT.** It has asked for BESS cost-benefit checks on future schemes, so the next decision may not go the same way.

---

## Where this view could be wrong

- The NCT has explicitly asked for BESS to be compared again **case by case**. Barmer-II is one data point, not a rule.
- **Battery prices keep falling.** A lower cost per kWh, longer durations and better augmentation economics could flip the result for a smaller or closer REZ.
- **Hybrid designs** (a smaller corridor plus storage) were not the headline comparison. A well-optimised hybrid could beat both pure options.
- **Execution risk** on a 1,000 km UHVDC line, including right-of-way, converter supply chains and pole-by-pole commissioning, can erode the capital cost advantage if it slips.

---

## The open question

For the transmission and storage experts:

> **At what BESS price per kWh does storage start to beat a new HVDC corridor for a REZ? And does the answer change if we compare a hybrid (smaller corridor plus storage) rather than battery versus line?**

I'd like to see real cost-benefit models in the comments.

---

### Sources cited in the original post

- Renewable Watch: Barmer-II award and annual transmission charge
- SolarQuarter: GE Vernova T&D India converter terminal supply
- T&D India: NCT selection of LCC HVDC, ₹24,974 crore estimate, 48-month first-pole timeline
- Gujarat standalone BESS tender: ₹2.80 lakh/MW/month reference (no VGF)

*Derived figures in this article (per MW-month charge, ₹/kWh parity marker) are my own illustrative calculations from the numbers above.*

`#HVDC #BESS #SolarEnergy #Transmission #IndiaEnergy #PowerSystems #EnergyStorage`
