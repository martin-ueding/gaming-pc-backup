import os
import zipfile
import datetime
import socket

zipfilename = '{host}-{time}.zip'.format(
		host=socket.gethostname(),
		time=datetime.datetime.now().strftime('%Y-%m-%dT%H-%I-%S'),
		)

dirs_to_save = [
		r'I:\home\David Webb\Documents\NFS SHIFT',
		r'I:\home\David Webb\Documents\NFS Most Wanted',
		r'I:\home\David Webb\Documents\TmForever\Profiles',
		r'I:\Program Files\Steam\userdata',
		r'I:\home\David Webb\Documents\My Games\Crysis',
		r'C:\Users\David Webb\AppData\Roaming\DarknessII\76561198014546789',
		r'C:\Users\David Webb\AppData\Roaming\Ubisoft\Assassin\'s Creed',
		r'C:\Users\David Webb\AppData\Local\NFS Underground 2',
]

files_to_save = [
]

with zipfile.ZipFile(zipfilename, 'w') as z:
	for dir_to_save in dirs_to_save:
		for dirpath, dirnames, filenames in os.walk(dir_to_save):
			for file in filenames:
				print(file)
				z.write(os.path.join(dirpath, file))
	for file_to_save in files_to_save:
		z.write(file_to_save)
