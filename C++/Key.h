#include<bits/stdc++.h>
using namespace std;

#include "Point.h"


class Key{
	Point publicKey;
	long privateKey;
	public:
	
	Key(){}
	
	/*
    Key: Initialise class with a user's Public and Private Key
    Input:-
        publicKey: User's Public Key
        privateKey: User's Private Key
     */

	Key(Point publicKey, long privateKey){
		this->publicKey = publicKey;
		this->privateKey = privateKey;
	}
	
	/*
    getPublicKey: Return Public Key for user
     */
    
	Point getPublicKey()
    {
        return publicKey;
    }


	/*
    getPrivateKey: Return Private Key for user
     */
    
    long getPrivateKey()
    {
        return privateKey;
    }

	/*
    setPublicKey: Store Public Key of user
     */
    
    void setPublicKey(Point publicKey)
    {
        this->publicKey = publicKey;
    }

	/*
    setPrivateKey: Store Private Key of user
     */
	void setPrivateKey(long privateKey)
    {
        this->privateKey = privateKey;
    }
};
