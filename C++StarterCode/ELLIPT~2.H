#include<bits/stdc++.h>
using namespace std;

#include "EllipticCurveArithmetic.h"


class EllipticCurveCryptography {

    Point G;
    long numPoints;
    Helper h;
    EllipticCurveArithmetic ec;

	public:
	
	/*
    EllipticCurveCryptography: Initialise classes needed for Encryption
    Inputs:-
        G: Base Point of elliptic curve
        numPoints: Number of points in Elliptic curve
        h: Instance of Helper class
        ec: Instance of EllipticCurve class
     */

    EllipticCurveCryptography(Point G, long numPoints, Helper h, EllipticCurveArithmetic& ec): ec(&ec){
        this->G = G;
        this->numPoints = numPoints;
        this->h = h;
        this->ec.a = ec.a;
		this->ec.b = ec.b;
		this->ec.m = ec.m;
    }

	/*
    generateKey: Generate Public,Private key for user
    Input:-
        len: Number of points in Elliptic curve
    Output:-
        Return generated key
     */
    
    Key generateKey(int len){
        Point publicKey;
        long privateKey;
        //Generate a pair of Public and Private Keys
        //Start writing code here

        //End writing code here
        return Key(publicKey,privateKey);
    }

	/*
    Encrypt: Encrypt a message using Receiver's Public Key
    Input:-
        str: Plaintext message
        public_key: Receiver's Public Key
    Output:-
        Return Encrypted message
     */
    
    string Encrypt(string str, Point public_key)
    {
        int len=str.length(),i;
        long r;
        Point A, B;
        string str1="";
        for(i=0;i<len;i++)
        {
            r=h.randomNumber(numPoints);
            //Encrypt each character and store the ciphertext points in A and B
            //Start writing code here

            //End writing code here
            str1+=h.pointToStream(A, ec.getM());
            str1+=h.pointToStream(B, ec.getM());
        }
        return str1;
    }

	/*
    Decrypt: Decrypt the ciphertext using Receiver's Private Key
    Input:-
        str: Ciphertext
        private_key: Receiver's Private Key
    Output:-
        Return generated key
     */
    
    string Decrypt(string str, long private_key)
    {
        string plaintext = "";
        vector<Point> v = h.streamToPoint(str, ec.getM());

        int len = v.size();

        for(int i=0;i<len;i+=2)
        {
            Point c1 = v[i];
            Point c2 = v[i+1];
            //Decrypt message character from c1 and c2 and append it to plaintext
            //Start writing code here

            //End writing code here
        }

        return plaintext;
    }

};

