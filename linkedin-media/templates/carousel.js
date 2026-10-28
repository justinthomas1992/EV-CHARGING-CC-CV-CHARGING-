const { chromium } = require('playwright');
const pages = [
 {k:"AI DATA CENTRES", h:"Power, not chips,<br>is the new bottleneck", b:"Where the real business opportunity sits for IPPs, EPCs and investors", n:"1 / 6"},
 {k:"THE GAP", h:"Fast to build.<br>Slow to power.", stats:[["18–24 months","to build an AI campus"],["~128 weeks","for a large power transformer (Wood Mackenzie)"],["5–10 years","for a grid connection in major hubs"]], n:"2 / 6"},
 {k:"ROOT CAUSE", h:"Why the gap exists", list:["AI demand arrives in 1–3 years; grids are planned over 5–10","Transformer and turbine factories were sized for flat 2010s demand","Interconnection queues are clogged with speculative requests","Campuses now draw 1–5 GW, the size of a power plant"], n:"3 / 6"},
 {k:"WORKED EXAMPLE", h:"Firm solar for 1 GW of load", stats:[["5.2 GW","solar PV"],["19 GWh","battery storage"],["~$6 B","total, Masdar/EWEC Abu Dhabi"]], b:"Rule of thumb: about 5 MW solar + 19 MWh storage per MW of round-the-clock load", n:"4 / 6"},
 {k:"OPPORTUNITIES", h:"Where to play", list:["IPPs: solar + BESS energy parks beside the load","EPCs: 220/400 kV substations, BESS integration, commissioning","Batteries in place of diesel backup","Storage that rides through grid faults and smooths AI load swings","India (~1.8 GW live, ~3.9 GW pipeline) and the GCC"], n:"5 / 6"},
 {k:"SOURCES", h:"Data behind this carousel", list:["IEA, Energy and AI (2025) and 2026 update","Wood Mackenzie transformer study via pv magazine (2025)","Masdar/EWEC RTC project: GreentechLead, Renewable Watch (2026)","ESS News on BESS at data centres (2026)","Cushman & Wakefield India data centre report (H1 2026)"], b:"Justin Thomas · Solar, BESS & power systems", n:"6 / 6"},
];
const css = `*{box-sizing:border-box}body{margin:0;font-family:Arial,Helvetica,sans-serif}
.p{width:1080px;height:1350px;background:#0b1f33;color:#fff;padding:110px 90px;display:flex;flex-direction:column;page-break-after:always;position:relative}
.k{color:#f5b700;font-size:30px;font-weight:700;letter-spacing:3px}.h{font-size:76px;font-weight:800;line-height:1.08;margin:26px 0 50px}
.b{font-size:34px;line-height:1.4;color:#d6e2ee;margin-top:30px}.s{background:#13314f;border-left:8px solid #2ec4b6;padding:30px 34px;margin-bottom:28px}
.sv{font-size:66px;font-weight:800;color:#2ec4b6}.sl{font-size:30px;margin-top:6px;color:#e6eef6}
ul{margin:0;padding-left:0;list-style:none}li{font-size:36px;line-height:1.35;margin-bottom:30px;padding-left:44px;position:relative}
li:before{content:"";position:absolute;left:0;top:14px;width:18px;height:18px;background:#2ec4b6}
.n{position:absolute;bottom:70px;right:90px;font-size:26px;color:#9fb3c8}.f{position:absolute;bottom:70px;left:90px;font-size:26px;color:#9fb3c8}`;
const html = `<html><head><style>${css}</style></head><body>${pages.map(p=>`<div class="p"><div class="k">${p.k}</div><div class="h">${p.h}</div>
${(p.stats||[]).map(([v,l])=>`<div class="s"><div class="sv">${v}</div><div class="sl">${l}</div></div>`).join('')}
${p.list?`<ul>${p.list.map(x=>`<li>${x}</li>`).join('')}</ul>`:''}${p.b?`<div class="b">${p.b}</div>`:''}
<div class="f">Justin Thomas</div><div class="n">${p.n}</div></div>`).join('')}</body></html>`;
(async()=>{const b=await chromium.launch();const pg=await b.newPage();await pg.setContent(html);
await pg.pdf({path:process.argv[2],width:'1080px',height:'1350px',printBackground:true,margin:{top:0,bottom:0,left:0,right:0}});await b.close();})();
