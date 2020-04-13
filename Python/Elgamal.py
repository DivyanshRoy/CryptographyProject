from EllipticCurve import EllipticCurve
from Helper import Helper
from Key import Key
from Point import Point

class Elgamal:
	def __init__(self, G, numPoints, h, ec):
		self.G = G
		self.numPoints = numPoints
		self.h = h
		self.ec = ec

	def generateKey(self, keyLen):
		privateKey = self.h.randomNumber(keyLen)
		publicKey = self.ec.multiply(self.G, privateKey, self.h)
		return Key(publicKey, privateKey)

	def Encrypt(self, plaintext, publicKey):
		msgLen = len(plaintext)
		ciphertext = ""
		a = []
		g = []

		for i in range(0, msgLen):
			r = self.h.randomNumber(self.numPoints)
			a.append(self.ec.multiply(self.G, r, self.h))

			p = self.h.charToPoint(plaintext[i])
			g.append(self.ec.add(p,
					 self.ec.multiply(publicKey, r, self.h), self.h))

			A = a[len(a) - 1]
			B = g[len(g) - 1]

			ciphertext += self.h.pointToStream(A, self.ec.getM())
			ciphertext += self.h.pointToStream(B, self.ec.getM())

		return (ciphertext, a, g)

	def Decrypt(self, ciphertext, privateKey, a, g):
		m = []
		for i in range(0, len(a)):
			prod = self.ec.multiply(a[i], privateKey, self.h)
			m.append(self.ec.subtract(g[i], prod, self.h))

		plaintext = ""
		for i in m:
			plaintext += self.h.pointToChar(i)

		return plaintext

