from EllipticCurveArithmetic import EllipticCurveArithmetic
from Helper import Helper
from Key import Key
from Point import Point

class EllipticCurveCryptography:
	'''
	__init__: Initialise classes needed for Encryption
    Inputs:-
        G: Base Point of elliptic curve
        numPoints: Number of points in Elliptic curve
        h: Instance of Helper class
        ec: Instance of EllipticCurveArithmetic class
	'''
	def __init__(self, G, numPoints, h, ec):
		self.G = G
		self.numPoints = numPoints
		self.h = h
		self.ec = ec

	'''
	generateKey: Generate Public,Private key for user
    Input:-
        len: Number of points in Elliptic curve
    Output:-
        Return generated key
	'''
	def generateKey(self, keyLen):
		# Write your code below

		# Write your code above
		return

	'''
	Encrypt: Encrypt a message using Receiver's Public Key
    Input:-
        str: Plaintext message
        public_key: Receiver's Public Key
    Output:-
        Return Encrypted message
	'''
	def Encrypt(self, plaintext, publicKey):
		msgLen = len(plaintext)
		ciphertext = ""
		for i in range(0, msgLen):
			r = self.h.randomNumber(self.numPoints)
			# Encrypt each character and store the ciphertext points in A and B
			# Write your code below

			# Write your code above
			ciphertext += self.h.pointToStream(A, self.ec.getM())
			ciphertext += self.h.pointToStream(B, self.ec.getM())

		return ciphertext

	'''
	Decrypt: Decrypt the ciphertext using Receiver's Private Key
    Input:-
        str: Ciphertext
        private_key: Receiver's Private Key
    Output:-
        Return decrypted message
	'''
	def Decrypt(self, ciphertext, privateKey):
		v = self.h.streamToPoint(ciphertext, self.ec.getM())
		plaintext = ""
		for i in range(0, len(v), 2):
			c1 = v[i]
			c2 = v[i + 1]
			# Decrypt message character from c1/c2 and append it to plaintext
			# Write your code below

			# Write your code above
			
		return plaintext
