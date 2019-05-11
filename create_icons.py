from pathlib import Path

from cairosvg import svg2png
from PIL import Image

p  = Path('.')

for folder in ['icons', 'add-ons']:
  for i in p.glob(folder + '/*.svg'):
    i = str(i)
    svg2png(url=i,write_to=i + '.png', scale=20)
    
icons = [Image.open(str(i)) for i in list(p.glob('icons/*.png'))]
add_ons = [Image.open(str(i)) for i in list(p.glob('add-ons/*.png'))]

for f in p.glob('**/*.png'):
  f.unlink()

img_size = 1000
add_size = 400

for i in icons:
  res = i.crop(i.getbbox())
  res = res.resize((img_size, img_size))
  res.save('dist/' + i.filename.split('/')[-1].replace('.svg', ''))

for i in icons:
  res = i.crop(i.getbbox())
  res = res.resize((img_size, img_size))
  cos = add_ons[0]
  cos = cos.crop(cos.getbbox())
  cos = cos.resize((add_size, add_size))
  res.paste(cos, box=(img_size - add_size, img_size - add_size), mask=cos)
  res.save('dist/costs_' + i.filename.split('/')[-1].replace('.svg', ''))