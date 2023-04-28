import requests
import os

url = ''
mdir = 'August21'
month = 'August'
mm = '08'
year = '2021'
os.mkdir(mdir)
for i in range(1,32):
	num = i
	if num < 10:
		# ******** URL for 2022 ********
		#url = f'https://lua.rlp.de/fileadmin/lua/Downloads/Corona/Rohdaten_{month}_{year}/Corona-Fallmeldungen-RLP-{year}-{mm}-0{num}.xlsx'

		# ******** URL for 2021 ********
		url = f'https://lua.rlp.de/fileadmin/lua/Downloads/Corona/Rohdaten_{year}/Corona-Fallmeldungen-RLP-{year}-{mm}-0{num}.xlsx'

		r = requests.get(url, allow_redirects=True)
		open(f'{mdir}/Corona-Fallmeldungen-RLP-{year}-{mm}-0{num}.xlsx', 'wb').write(r.content)

	elif num >= 10 and num <= 32:
		# ******** URL for 2022 ********
		#url = f'https://lua.rlp.de/fileadmin/lua/Downloads/Corona/Rohdaten_{month}_{year}/Corona-Fallmeldungen-RLP-{year}-{mm}-{num}.xlsx'

		# ******** URL for 2021 ********
		url = f'https://lua.rlp.de/fileadmin/lua/Downloads/Corona/Rohdaten_{year}/Corona-Fallmeldungen-RLP-{year}-{mm}-{num}.xlsx'

		r = requests.get(url, allow_redirects=True)
		open(f'{mdir}/Corona-Fallmeldungen-RLP-{year}-{mm}-{num}.xlsx', 'wb').write(r.content)