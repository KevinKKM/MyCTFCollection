import Crypto

h = MD4.new()
h.update("Hello")
print(h.hexdigest())