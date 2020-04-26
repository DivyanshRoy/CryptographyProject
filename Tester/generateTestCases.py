from Python.EllipticCurveArithmetic import EllipticCurveArithmetic
from Python.EllipticCurveCryptography import EllipticCurveCryptography
from Python.Helper import Helper
from Python.Key import Key
from Python.Point import Point
import random
import string

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

    ec = EllipticCurveArithmetic(a, b, m)
    curvePoints = ec.getCurvePoints()

    h = Helper()
    h.generateCharacterPointMappings(curvePoints)

    names = open("names.txt", "r").read().split("\n")
    for person in names:
        G = generateReferencePoint(curvePoints, h)
        el = EllipticCurveCryptography(G, len(curvePoints), h, ec)

        receiver = el.generateKey(len(curvePoints))

        N = 64
        message = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k = N))
        file2 = open(str("testcases/"+person+"_test1.txt"), "w")
        file2.write(str(G.getX())+" "+str(G.getY())+"\n")
        file2.write(str(receiver.getPublicKey().getX()) + " " + str(receiver.getPublicKey().getY()) + "\n")
        file2.write(str(message+"\n"))
        file2.close()

        file3 = open(str("res/" + person + "_private_key_test1.txt"), "w")
        file3.write(str(receiver.getPrivateKey()) + "\n")
        file3.close()

        G = generateReferencePoint(curvePoints, h)
        el = EllipticCurveCryptography(G, len(curvePoints), h, ec)
        receiver = el.generateKey(len(curvePoints))
        N = 8
        message = ''.join(random.choices(string.ascii_lowercase +
                                         string.digits, k=N))
        encryptedMessage = el.Encrypt(message, receiver.getPublicKey())
        file2 = open(str("testcases/" + person + "_test2.txt"), "w")
        file2.write(str(G.getX()) + " " + str(G.getY()) + "\n")
        file2.write(str(receiver.getPrivateKey()) + "\n")
        file2.write(str(encryptedMessage + "\n"))
        file2.close()

if __name__ == "__main__":
    main()
