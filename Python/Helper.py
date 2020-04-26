import random
from Point import Point

class Helper:
	def __init__(self):
		self.asciiToPoint = {}
		self.pointToAscii = {}

	'''
	getSegmentSize: Each segment is a representation of a point using lowercase characters of the English alphabet.
                    Return the minimum segment size needed to represent each point with a distinct segment.
    Input:-
        m: Modulo size of Elliptic Curve
    Output:-
        Return minimum length of segment
	'''
	def getSegmentSize(self, m):
		numPoints = ((m ** 2) + 1)
		size = 0
		while (numPoints != 0):
			numPoints //= 26
			size += 1
		return size

	'''
	generateCharacterPointMappings: Map Elliptic curve points to Ascii characters and vice-versa
    Input:-
        curvePoints: List of points on Elliptic Curve
	'''
	def generateCharacterPointMappings(self, curvePoints):
		numPoints = len(curvePoints)
		maxMappings = min(numPoints, 2 ** 16)

		asciiCodes = []
		for i in range(0, maxMappings):
			asciiCodes.append(i)
		# random.shuffle(asciiCodes)
		asciiToPoint = {}
		pointToAscii = {}
		sno = 0

		for asciiCode in asciiCodes:
			p = curvePoints[sno]
			p = (p.getX(), p.getY())
			pointToAscii[p] = asciiCode
			asciiToPoint[asciiCode] = p
			sno += 1
		self.asciiToPoint = asciiToPoint
		self.pointToAscii = pointToAscii

	# charToPoint: Return Point mapped to a character
	def charToPoint(self, c):
		p = self.asciiToPoint[ord(c)]
		p = Point(p[0], p[1])
		return p

	# pointToChar: Return character mapped to a Point
	def pointToChar(self, p):
		p = (p.getX(), p.getY())
		return chr(self.pointToAscii[p])

	'''
	streamToPoint: Convert a sequence of segments representing a list of points to the corresponding points
    Input:-
        stream: Sequence of segments
        m: Modulo for Elliptic Curve
    Output:-
        Return list of points
	'''
	def streamToPoint(self, stream, m):
		segmentSize = self.getSegmentSize(m)
		v = []
		i = 0

		while i < len(stream):
			temp = stream[i:i+segmentSize]
			val = 0
			for j in range(0, segmentSize):
				d = ord(temp[j]) - ord('a')
				val = (val * 26) + d

			p = Point(val // m, val%m)
			v.append(p)
			i += segmentSize

		return v

	'''
	pointToStream: Convert a point to a segment
    Input:-
        p: Elliptic curve point
        m: Modulo for Elliptic Curve
    Output:-
        Return segment representing the point
	'''
	def pointToStream(self, p, m):
		stream = ""
		temp = ""
		segmentSize = self.getSegmentSize(m)
		val = (p.getX() * m) + p.getY()

		for i in range(0, segmentSize):
			temp += chr(ord('a') + (val % 26))
			val //= 26

		while i >= 0:
			stream += temp[i]
			i -= 1

		return stream

	'''
	randomPoint: Return a random point from the Elliptic curve
    Input:-
        curvePoints: List of all points on the Elliptic Curve
	'''
	def randomPoint(self, curvePoints):
		numPoints = len(curvePoints)
		r = random.randint(0, numPoints - 1)
		return curvePoints[r]

	# randomNumber: Return a random number in the range [0, m-1]
	def randomNumber(self, m):
		return random.randint(0, int(m) - 2) + 1

	# modulus: Return l modulo m
	def modulus(self, l, m):
		while l < 0:
			l += m
		l %= m
		return l
