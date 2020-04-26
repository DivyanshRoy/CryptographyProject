from Python.EllipticCurveArithmetic import EllipticCurveArithmetic
from Python.EllipticCurveCryptography import EllipticCurveCryptography
from Python.Helper import Helper

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

    person = input()
    encryptedOutput = input()
    decryptedOutput = input()

    G = generateReferencePoint(curvePoints, h)
    el = EllipticCurveCryptography(G, len(curvePoints), h, ec)

    ################################
    # Test 1 evaluation begin
    ################################

    file1 = open(str("testcases/" + person + "_test1.txt"), "r").read().split("\n")
    row1 = file1[0].split(" ")
    G.setX(int(row1[0]))
    G.setY(int(row1[1]))

    row3 = file1[2]
    message = row3

    file1 = open(str("res/" + person + "_private_key_test1.txt"), "r").read().split("\n")
    private_key = int(file1[0])
    try:
        decryptedMessage = el.Decrypt(encryptedOutput, private_key)
        if decryptedMessage==message:
            print("Test 1 passed")
        else:
            print("Test 1 failed")
    except:
        print("Test 1 failed")

    ################################
    # Test 1 evaluation end
    ################################

    ################################
    #Test 2 evaluation begin
    ################################

    file1 = open(str("testcases/" + person + "_test2.txt"), "r").read().split("\n")
    row1 = file1[0].split(" ")
    G.setX(int(row1[0]))
    G.setY(int(row1[1]))

    row2 = file1[1]
    private_key = int(row2)

    row3 = file1[2]
    encrytedMessage = row3

    decryptedMessage = el.Decrypt(encrytedMessage, private_key)
    if decryptedMessage==decryptedOutput:
        print("Test 2 passed")
    else:
        print("Test 2 failed")
        print("Expected Output: ", decryptedMessage)
        print("Actual Output: ", decryptedOutput)
    ################################
    # Test 2 evaluation end
    ################################

if __name__ == "__main__":
    main()
