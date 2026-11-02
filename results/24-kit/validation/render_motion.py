import asyncio, subprocess, shutil
from pathlib import Path
from playwright.async_api import async_playwright
d = Path(__file__).parent.resolve()/"03-motion"; fr = d/"_frames"; fr.mkdir(exist_ok=True)
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width":1080,"height":1080})
        await pg.goto((d/"motion-021.html").as_uri()+"?t=0&clean"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
        for f in range(150):
            await pg.evaluate(f"frame({f*1000/30})"); await pg.screenshot(path=str(fr/f"f{f:03d}.png"))
        for t in (700,1450,2200,5000):
            await pg.evaluate(f"frame({t})"); await pg.screenshot(path=str(d/f"motion-021_t{t}.png"))
        await b.close()
asyncio.run(main())
subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate","30","-i",str(fr/"f%03d.png"),"-c:v","libx264","-pix_fmt","yuv420p","-crf","16","-movflags","+faststart",str(d/"motion-021_5s.mp4")],check=True)
shutil.rmtree(fr)
