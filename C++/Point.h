#include<bits/stdc++.h>
using namespace std;

class Point{
	long x,y;
	
	public:
	
	Point(){}
	
	/*
    Point: Initialise with x and y coordinates of Elliptic curve point
     */
    
	Point(long x, long y){
		this->x = x;
		this->y = y;
	}
	
	/*
    getX: Return x coordinate of Elliptic curve point
     */
    
	long getX()
    {
        return x;
    }
    
    /*
    getY: Return y coordinate of Elliptic curve point
     */
    
    long getY()
    {
        return y;
    }

	/*
    setX: Store x coordinate of Elliptic curve point
     */
    
    void setX(long x)
    {
        this->x = x;
    }

	/*
    setY: Store y coordinate of Elliptic curve point
     */
    
    void setY(long y)
    {
        this->y = y;
    }
};
