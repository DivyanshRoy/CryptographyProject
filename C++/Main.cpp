#include<bits/stdc++.h>
using namespace std;

#include "EllipticCurveCryptography.h"

/*
    generateReferencePoint: Generate Base point for elliptic curve
    Input:-
        curvePoints: List of points on the Elliptic Curve
    Output:-
        Return Base point or Generator
     */
    
Point generateReferencePoint(vector<Point> curvePoints, Helper h)
{
    Point G = h.randomPoint(curvePoints);
    if(G.getX()==0 && G.getY()==0)
        G = generateReferencePoint(curvePoints, h);
    return G;
}

int main(){
	srand(time(NULL));
	//Elliptic Curve Parameters
    long a,b,m;
    a = 17;
    b = 50;
    m = 191;

    EllipticCurveArithmetic ec(a, b, m);
    vector<Point> curvePoints = ec.getCurvePoints();

    Helper h = Helper();
    h.generateCharacterPointMappings(curvePoints);

	//Base Point/Generator of Elliptic Curve
    Point G = generateReferencePoint(curvePoints, h);
    EllipticCurveCryptography el(G, (long)curvePoints.size(), h, ec);
    //Receiver's Public and Private keys
    Key k = el.generateKey(curvePoints.size());
    
    string message;
    cout<<"Enter message: "<<endl;
    getline(std::cin, message);
    cout<<"Original message: "<<message<<endl;

    string encryptedMessage = el.Encrypt(message, k.getPublicKey());
    cout<<"Encrypted message: "<<encryptedMessage<<endl;
	
    string decryptedMessage = el.Decrypt(encryptedMessage, k.getPrivateKey());
    cout<<"Decrypted message: "<<decryptedMessage<<endl;
}

