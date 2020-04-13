from EllipticCurve import EllipticCurve
from Elgamal import Elgamal
from Helper import Helper
from Key import Key
from Point import Point

def generateReferencePoint(curvePoints, h):
	G = h.randomPoint(curvePoints)
	if G.getX() == 0 and G.getY() == 0:
		G = generateReferencePoint(curvePoints, h)
	return G

def main():
	a = 17
	b = 50
	m = 191

	ec = EllipticCurve(a, b, m)
	curvePoints = ec.getCurvePoints()

	h = Helper()
	h.generateCharacterPointMappings(curvePoints)

	G = generateReferencePoint(curvePoints, h)
	el = Elgamal(G, len(curvePoints), h, ec)
	k = el.generateKey(len(curvePoints))

	message = input("Enter message: ")
	print("Original message:", message)

	encryptedMessage, alpha, gamma = el.Encrypt(message, k.getPublicKey())
	print("Encrypted message:", encryptedMessage)

	decryptedMessage = el.Decrypt(encryptedMessage,
								  k.getPrivateKey(), alpha, gamma)
	print("Decrypted message:", decryptedMessage)

if __name__ == "__main__":
	main()
