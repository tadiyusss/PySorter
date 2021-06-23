import os 
import shutil

downloads_dir = 'C:\\Users\\mypc\\Downloads'
images = ['jpg', 'bmp', 'jpeg', 'gif', 'png'
, 'jfif']
videos = ['mp4']
documents = ['docx', 'pdf', 'txt', 'doc']
others = ['exe', 'zip', 'rar', 'tar', 'gz', 'iso', 'htm']
count = 0
files = os.listdir(downloads_dir)
if len(files) > 1:
	for x in files:
		try:
			try:
				if x.split('.')[1] in images:
					shutil.move(x, 'Images')
					print('[+] Moved ' + x + ' to Images directory')
			except IndexError:
				pass
			try:
				if x.split('.')[1] in videos:
					shutil.move(x, 'Videos')
					print('[+] Moved ' + x + ' to Videos directory')
			except IndexError:
				pass
			try:
				if x.split('.')[1] in documents:
					shutil.move(x, 'Documents')
					print('[+] Moved ' + x + ' to Documents directory')
			except IndexError:
				pass
			try:
				if x.split('.')[1] != '':
					if x != 'sort.py':
						shutil.move(x, 'Others')
						print('[+] Moved ' + x + ' to Others directory')
			except IndexError:
				pass
		except Exception as e:
			pass
		count += 1 
