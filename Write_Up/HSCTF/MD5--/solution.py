from Crypto.Hash import MD4
import re

i = 0
while True:
	bf_payload = ("0e%d"%i)
	h = MD4.new()
	hash = h.update(bf_payload)
	hash = h.hexdigest()
	print("Input : %s , Output : %s"%(bf_payload,h.hexdigest()))
	i = i + 1
	if(hash[:2]=="0e" and hash[:2].isdigit()):
		print("Done, payload = %s"%bf_payload)
		print("The hash = %s"%hash)
		break
