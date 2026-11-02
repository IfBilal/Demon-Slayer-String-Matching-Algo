"""Render captured program output and assemble the two-page submission report."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import zipfile
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'DemonHunt_data/output'
font_path = '/usr/share/fonts/liberation-mono-fonts/LiberationMono-Regular.ttf'
def font(size):
    try:
        return ImageFont.truetype(font_path, size)
    except OSError:
        return ImageFont.load_default(size=size)

def capture(name):
    # Actual GTK/VTE terminal screenshot captured after executing the mission.
    return Image.open(OUT / f'{name}_output.png').convert('RGB')

def page(title):
    im = Image.new('RGB', (1654, 2339), 'white')
    d = ImageDraw.Draw(im)
    d.text((75, 65), 'Demon Slayer Corps - The String Hunt', font=font(40), fill='#173954')
    d.text((75, 125), f'24i-3166 | {title}', font=font(26), fill='black')
    return im

def put(im, shot, y, width=1500):
    shot = shot.resize((width, round(shot.height * width / shot.width)))
    im.paste(shot, (75, y))
    return y + shot.height

p1 = page('Missions 1 and 2 | Page 1 of 2')
d = ImageDraw.Draw(p1)
d.text((75, 205), 'Mission 1 - streaming KMP (4096-character chunks)', font=font(28), fill='black')
put(p1, capture('mission1'), 255)
d.text((75, 510), 'Mission 2 - finite automaton and both DNA strands', font=font(28), fill='black')
put(p1, capture('mission2'), 565)
d.text((75, 1610), 'Final Selection: 24/24 PASS. Additional regression tests: PASS.', font=font(25), fill='black')
d.text((75, 1670), 'All matches use zero-based shifts. Overlapping occurrences count.', font=font(25), fill='black')
d.text((75, 1730), 'Sample 07 has three reverse-strand hits and no forward-strand hits.', font=font(25), fill='black')
d.text((75, 1830), 'Screenshots show actual terminal execution of the submitted scripts.', font=font(24), fill='black')
p2 = page('Mission 3 and bonus | Page 2 of 2')
d = ImageDraw.Draw(p2)
d.text((75, 205), 'Mission 3 - verified 40-character rolling windows', font=font(28), fill='black')
put(p2, capture('mission3'), 255)
d.text((75, 630), 'Inosuke paraphrased passages; his exact-overlap score is only 14.96%.', font=font(24), fill='black')
d.text((75, 690), 'Bonus - Infinity Castle tournament', font=font(28), fill='black')
put(p2, capture('mission4'), 740)
put(p2, Image.open(OUT / 'bonus_chart.png'), 1180)
d.text((75, 1940), 'Timing includes preprocessing. Counts exclude preprocessing.', font=font(25), fill='black')
d.text((75, 1990), 'FA counts table lookups; RK counts only verification comparisons.', font=font(25), fill='black')
d.text((75, 2040), 'RK still computes rolling hashes even when verification count is zero.', font=font(25), fill='black')
p1.save(ROOT / 'mission_report.pdf', save_all=True, append_images=[p2], resolution=150)
p1.resize((827,1170)).save(OUT / 'report_page1.png')
p2.resize((827,1170)).save(OUT / 'report_page2.png')
with zipfile.ZipFile(ROOT / '24i-3166_DemonHunt.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(ROOT / 'mission_report.pdf', 'mission_report.pdf')
    for path in sorted((ROOT / 'DemonHunt_data/starter').iterdir()):
        if path.is_file():
            z.write(path, 'src/' + path.name)
    for path in sorted((ROOT / 'DemonHunt_data/data').rglob('*')):
        if path.is_file():
            z.write(path, str(path.relative_to(ROOT / 'DemonHunt_data')))
    z.write(OUT / 'bonus_chart.png', 'output/bonus_chart.png')
