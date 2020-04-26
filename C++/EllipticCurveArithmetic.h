#include<bits/stdc++.h>
using namespace std;

#include "Helper.h"

class EllipticCurveArithmetic {
	public:
	long a,b,m;
	EllipticCurve(){
	}
	
	/*
    EllipticCurveArithmetic: Initialise an elliptic curve with Curve Parameters
    Curve Equation: y^2 = (x^3 + ax + b) modulo m
     */
    EllipticCurveArithmetic (long a, long b, long m){
        this->a = a;
        this->b = b;
        this->m = m;
    }
    
    EllipticCurveArithmetic(EllipticCurveArithmetic *ec){
    	this->a = ec->a;
		this->b = ec->b;
		this->m = ec->m;
	}
    
    /*
    getM: Return m
     */
    long getM(){
        return m;
    }

	/*
    getCurvePoints: Generate curve points which follow the Elliptic Curve equation y^2 = (x^3 + ax + b) modulo m
    Output:-
        Return list of Elliptic curve points
     */
    vector<Point> getCurvePoints(){
        long x,y;
        map<long, vector<long> > mx;
        map<long, vector<long> > my;
        
        for(x = 0; x < m ; x++)
        {
        	vector<long> tmp;
            long v = ( (x*x*x) + (a*x) + b ) % m;
            if(mx.find(v)!=mx.end())
            {
                mx[v].push_back(x);
            }
            else
            {
                tmp.push_back(x);
                mx[v] = tmp;
            }
        }

        for(y = 0; y < m ; y++)
        {
        	vector<long> tmp;
            long v = ( (y*y) ) % m;
            if(my.find(v)!=my.end())
            {
            	my[v].push_back(y);
            }
            else
            {
                tmp.push_back(y);
                my[v] = tmp;
            }
        }

        vector<Point> points;
		for(map<long, vector<long> >::iterator iter=mx.begin(); iter!=mx.end(); iter++)
        {

        	long s = iter->first;
        	if(my.find(s)!=my.end())
            {
                vector<long> vx = mx[s];
                vector<long> vy = my[s];
                for(int i=0;i<vx.size();i++)
                {
                	long x1 = vx[i];
                	for(int j=0;j<vy.size();j++)
                    {
                    	long y1 = vy[j];
                        points.push_back(Point(x1,y1));
                    }
                }
            }
        }
        points.push_back(Point((long)0,(long)0));
        vector<long> hashedPoints;
        for(int i=0;i<points.size();i++){
        	Point p = points[i];
        	long v = p.getX()*this->m + p.getY();
        	hashedPoints.push_back(v);
		}
        sort(hashedPoints.begin(), hashedPoints.end());
        points.clear();
        
        for(int i=0;i<hashedPoints.size();i++){
        	long h = hashedPoints[i];
        	points.push_back(Point(h/this->m, h%this->m));
		}        
        return points;
    }

	/*
    modInverse: Calculate the modular inverse of a with m as modulus
    Output:-
        Return a^-1 modulo m
     */
    long modInverse(long a, long m, Helper h)
    {
        a = h.modulus(a, m);
        a = a%m;
        long x;
        for(x = 1; x<m ; x++)
        {
            if(((a*x)%m)==1)
                return x;
        }
        return x;
    }


    /*
    add: Add 2 Elliptic curve points
    Input:-
        p1: Point 1
        p2: Point 2
    Output:-
        Return a Point which is the addition of p1 and p2 according to Elliptic curve arithmetic.
     */

    Point add(Point p1, Point p2, Helper h)
    {
        long x1 = p1.getX();
        long y1 = p1.getY();
        long x2 = p2.getX();
        long y2 = p2.getY();

        if(x1 == 0 && y1 == 0)
        {
            return p2;
        }
        if(x2 == 0 && y2 == 0)
        {
            return p1;
        }

        if(x1 == x2 && y1 == m-y2)
            return Point((long)0, (long)0);
        if(x1 == x2 && y1 == y2)
        {
            return addWithItself(p1, h);
        }
        long s,d,n;
        n = h.modulus(y2-y1, m);
        d = h.modulus(x2-x1, m);
        d = modInverse(d, m, h);
        s = h.modulus(d*n, m);
        long x3,y3;
        x3 = h.modulus((s*s)-x1-x2, m);
        y3 = h.modulus((s*(x1-x3))-y1, m);
        return Point(x3,y3);

    }
    
    /*
    addWithItself: Add a point to itself.
    Input:-
        p: Point p
    Output:-
        Return the sum of p and p using Elliptic curve arithmetic
     */

    Point addWithItself(Point p, Helper h)
    {
        long x,y;
        x=p.getX();
        y=p.getY();

        if(y == 0)
            return Point((long)0, (long)0);
        long s,d;
        s = h.modulus((3 * x * x) + a, m);
        d = (2 * y);
        d = h.modulus(modInverse(h.modulus(d, m), m, h), m);
        s = h.modulus(s * d, m);
        long xd, yd;
        xd=h.modulus((s * s)-(2 * x), m);
        yd=h.modulus((s * (x - xd) - y), m);
        return Point(xd, yd);
    }

    /*
    multiply: Multiply a Point with a scalar number
    Input:-
        p: Point p
        l: Scalar to be used for multiplication
    Output:-
        Return the multiplication of p with l.
        Hint: Multiplication is just repeated addition.
        Challenge: Make this operation O(log(l)) instead of O(l).
     */

    Point multiply(Point p, long l, Helper h)
    {
        if(l==1)
        {
            return p;
        }
        Point halfMultiply = multiply(p, l/2, h);
        Point ans = addWithItself(halfMultiply, h);

        if((l % 2) == 1)
        {
            ans = add(ans, p, h);
        }
        return ans;
    }

    /*
    subtract: Return the difference between 2 curve points
    Input:-
        p1: Point p1
        p2: Point p2
    Output:-
        Return difference of p1 and p2.
     */

    Point subtract(Point p1, Point p2, Helper h)
    {
        Point p3 = Point(p2.getX(),m-p2.getY());
        return add(p1,p3, h);
    }
};

