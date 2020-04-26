#include<bits/stdc++.h>
using namespace std;

#include "Key.h"

class Helper {
    map<int, Point> asciiToPoint;
    map<pair<long, long>, int> pointToAscii;

	public:
		
	/*
    getSegmentSize: Each segment is a representation of a point using lowercase characters of the English alphabet.
                    Return the minimum segment size needed to represent each point with a distinct segment.
    Input:-
        m: Modulo size of Elliptic Curve
    Output:-
        Return minimum length of segment
     */
    
    int getSegmentSize(long m)
    {
        long numPoints = (long)(m*m + 1);
        int size = 0;
        while(numPoints != 0)
        {
            numPoints /= 26;
            size++;
        }
        return size;
    }

	/*
    generateCharacterPointMappings: Map Elliptic curve points to Ascii characters and vice-versa
    Input:-
        curvePoints: List of points on Elliptic Curve
     */
    
    void generateCharacterPointMappings(vector<Point> curvePoints){
        int numPoints = curvePoints.size();
        int maxMappings = min(numPoints, (int)65536);

        vector<int> asciicodes;

        for(int i = 0; i<maxMappings ; i++)
        {
            asciicodes.push_back(i);
        }
//        random_shuffle(asciicodes.begin(), asciicodes.end());

        map<int, Point> asciiToPoint;
        map<pair<long, long>, int> pointToAscii;

        int sno = 0;

		for(int i=0; i<asciicodes.size();i++){
			int asciicode = asciicodes[i];
            asciiToPoint[asciicode] = curvePoints[sno];
            Point p = curvePoints[sno];
            pointToAscii[make_pair(p.getX(), p.getY())] = asciicode;
            sno++;
        }
        this->asciiToPoint = asciiToPoint;
        this->pointToAscii = pointToAscii;
    }

	/*
    charToPoint: Return Point mapped to a character
     */
    Point charToPoint(char c)
    {
        return asciiToPoint[c];
    }

    /*
    pointToChar: Return character mapped to a Point
     */
    char pointToChar(Point p)
    {
        return (char)pointToAscii[make_pair(p.getX(), p.getY())];
    }

    /*
    streamToPoint: Convert a sequence of segments representing a list of points to the corresponding points
    Input:-
        stream: Sequence of segments
        m: Modulo for Elliptic Curve
    Output:-
        Return list of points
     */
    vector<Point> streamToPoint(string stream, long m)
    {
        int segmentSize = getSegmentSize(m);
        vector<Point> v;
        int i=0;
        while(i<stream.length())
        {
            string temp = stream.substr(i, i+segmentSize);
            i+=segmentSize;

            long val = 0;
            int j;
            for(j=0;j<segmentSize;j++)
            {
                int d = temp[j] - 'a';
                val = val*26 + d;
            }
            v.push_back(Point(val/m,val%m));
        }

        return v;
    }

    /*
    pointToStream: Convert a point to a segment
    Input:-
        p: Elliptic curve point
        m: Modulo for Elliptic Curve
    Output:-
        Return segment representing the point
     */

    string pointToStream(Point p, long m)
    {
        string stream = "";
        int segmentSize = getSegmentSize(m);
        long val = p.getX()*m + p.getY();
        string temp = "";
        for(int i=0;i<segmentSize;i++)
        {
            temp += (char)('a' + val%26);
            val /= 26;
        }
        for(int i=segmentSize-1;i>=0;i--)
        {
            stream += temp[i];
        }
        return stream;
    }


    /*
    randomPoint: Return a random point from the Elliptic curve
    Input:-
        curvePoints: List of all points on the Elliptic Curve
     */

    Point randomPoint(vector<Point> curvePoints)
    {
        int numPoints = curvePoints.size();
        int r = rand()%numPoints;
        return curvePoints[r];
    }

    /*
    randomNumber: Return a random number in the range [0, m-1]
     */

    long randomNumber(long m)
    {
        long r = (long)(rand()%(m-1))+1;
        return r;
    }


    /*
    modulus: Return l modulo m
     */

    long modulus(long l, long m)
    {
        while(l<0)
        {
            l += m;
        }
        l %= m;
        return l;
    }
};

