import sys, asyncio
from pathlib import Path
from playwright.async_api import async_playwright
async def shot(url, out, w, h, scale=1, guides=False):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width": w, "height": h}, device_scale_factor=scale)
        await pg.goto(url); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
        await pg.screenshot(path=out, clip={"x":0,"y":0,"width":w,"height":h}); await b.close()
base = Path(__file__).parent.resolve()
mm = 96/25.4
async def main():
    W, H = round(76*mm), round(126*mm)
    await shot((base/"01-front/front-021.html").as_uri(), str(base/"01-front/front-021_paper.png"), W, H, 4)
    await shot((base/"01-front/front-021.html").as_uri()+"?guides", str(base/"01-front/front-021_paper_guides.png"), W, H, 4)
    await shot((base/"02-poster/poster-021.html").as_uri(), str(base/"02-poster/poster-021.png"), 1080, 1440)
asyncio.run(main())
