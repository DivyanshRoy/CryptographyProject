from EllipticCurve import EllipticCurve
from Elgamal import Elgamal
from Helper import Helper
from Key import Key
from Point import Point

'''
generateReferencePoint: Generate Base point for elliptic curve
	Input:-
		curvePoints: List of points on the Elliptic Curve
	Output:-
		Return Base point or Generator
'''
def generateReferencePoint(curvePoints, h):
	G = h.randomPoint(curvePoints)
	if G.getX() == 0 and G.getY() == 0:
		G = generateReferencePoint(curvePoints, h)
	return G

def main():
	# Elliptic Curve Parameters
	a = 17
	b = 50
	m = 191

	ec = EllipticCurve(a, b, m)
	curvePoints = ec.getCurvePoints()

	h = Helper()
	h.generateCharacterPointMappings(curvePoints)

	# Base Point/Generator of Elliptic Curve
	G = generateReferencePoint(curvePoints, h)
	el = Elgamal(G, len(curvePoints), h, ec)

	# Sender and Receiver's Public, Private keys
	sender = el.generateKey(len(curvePoints))
	receiver = el.generateKey(len(curvePoints))

	message = input("Enter message: ")
	print("Original message:", message)

	encryptedMessage = el.Encrypt(message, receiver.getPublicKey())
	print("Encrypted message:", encryptedMessage)

	decryptedMessage = el.Decrypt(encryptedMessage, receiver.getPrivateKey())
	print("Decrypted message:", decryptedMessage)

if __name__ == "__main__":
	main()
