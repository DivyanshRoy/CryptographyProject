from Point import Point

class Key:
	'''
	__init__: Initialise class with a user's Public and Private Key
    Input:-
        publicKey: User's Public Key
        privateKey: User's Private Key
	'''
	def __init__(self, publicKey, privateKey):
		self.publicKey = publicKey
		self.privateKey = privateKey

	# getPublicKey: Return Public Key for user
	def getPublicKey(self):
		return self.publicKey

	# getPrivateKey: Return Private Key for user
	def getPrivateKey(self):
		return self.privateKey
