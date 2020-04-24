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
		privateKey = self.h.randomNumber(keyLen)
		publicKey = self.ec.multiply(self.G, privateKey, self.h)
		return Key(publicKey, privateKey)

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
			A = self.ec.multiply(self.G, r, self.h)
			B = self.ec.add(self.h.charToPoint(plaintext[i]),
							self.ec.multiply(publicKey, r, self.h), self.h)

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
			DM = self.ec.subtract(c2, self.ec.multiply(c1, privateKey, self.h), self.h)
			plaintext += self.h.pointToChar(DM)

		return plaintext
