# svg-converter
# version 0.2.0-dev

# note: only use as workspace tool, logic and compute steps are not optimized.

import pathlib
import hashlib
import shutil
print('SVG CONVERTER')
media = [pathlib.Path(__file__).parent.parent / 'media']
for path in media:
	for entry in path.iterdir():
		if entry.is_dir() and entry not in media:
			media.append(entry)
		if entry.is_file():
			if entry.suffix == '.html':
				hash_html = hashlib.md5(entry.read_bytes()).hexdigest()
				svg = entry.with_suffix('.svg')
				if svg.exists():
					hash_svg = hashlib.md5(svg.read_bytes()).hexdigest()
					if hash_html == hash_svg:
							continue
					print(f"\tconverting html{entry.name}..." )
				else:
					print(f"\tcreating svg {entry.name}..." )
				shutil.copy(entry, svg)
				continue
			if entry.suffix == '.svg':
				html = entry.with_suffix('.html')
				if html.exists():
					continue
				print(f'\tcreating html {entry.name}...')
				shutil.copy(entry, html)
				continue
import time
print('\nBuild time:', time.strftime('%Y-%m-%d %H:%M:%S'))