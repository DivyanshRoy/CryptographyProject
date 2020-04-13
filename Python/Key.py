from Point import Point

class Key:
	def __init__(self, publicKey, privateKey):
		self.publicKey = publicKey
		self.privateKey = privateKey

	def getPublicKey(self):
		return self.publicKey

	def getPrivateKey(self):
		return self.privateKey

