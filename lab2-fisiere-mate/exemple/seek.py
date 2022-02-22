## numere.txt ##
# 1234567890
################

with open("numere.txt", "rb") as f:
	patru = f.read(4)
	print(patru)			# b'1234'
	
	cinci = f.read(1)
	print(cinci)			# b'5'

	f.seek(-2, 1)
	patruIar = f.read(1)
	print(patruIar.decode("utf-8"))	# 4

	f.seek(-1, 2)
	zero = f.read(1)
	print(zero)				# b'0'

	f.seek(0)				# echivalent cu f.seek(0, 0)
	unu = f.read(1)
	print(unu)				# b'1'