const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1200,height:627}});
  await p.setContent(`<html><body style="margin:0;font-family:Arial,sans-serif;background:#0b1f33;color:#fff;width:1200px;height:627px;display:flex;flex-direction:column;justify-content:center;padding:0 70px;box-sizing:border-box">
  <div style="color:#f5b700;font-size:26px;font-weight:700;letter-spacing:2px">AI DATA CENTRES</div>
  <div style="font-size:60px;font-weight:800;line-height:1.1;margin:14px 0 36px">Power, not chips,<br>is the new bottleneck</div>
  <div style="display:flex;gap:28px">
   ${[["18–24 mo","to build a campus"],["~128 wks","for a large power transformer"],["5–10 yrs","for a grid connection in major hubs"]].map(([a,b])=>`<div style="flex:1;background:#13314f;border-left:6px solid #2ec4b6;padding:22px"><div style="font-size:44px;font-weight:800;color:#2ec4b6">${a}</div><div style="font-size:22px;margin-top:6px">${b}</div></div>`).join('')}
  </div>
  <div style="font-size:16px;color:#9fb3c8;margin-top:30px">Sources: Wood Mackenzie (Q2 2025), IEA, industry reporting · Justin Thomas</div></body></html>`);
  await p.screenshot({path: process.argv[2]}); await b.close();
})();
