package JavaStarterCode;


import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.Vector;

public class EllipticCurveArithmetic {

    private Long a,b,m;
    private Map<Point, Long> pointInverseMapping;

    /*
    EllipticCurve: Initialise an elliptic curve with Curve Parameters
    Curve Equation: y^2 = (x^3 + ax + b) modulo m
     */
    public EllipticCurveArithmetic(Long a, Long b, Long m){
        this.a = a;
        this.b = b;
        this.m = m;
    }

    /*
    getM: Return m
     */
    public Long getM(){
        return m;
    }

    /*
    getCurvePoints: Generate curve points which follow the Elliptic Curve equation y^2 = (x^3 + ax + b) modulo m
    Output:-
        Return list of Elliptic curve points
     */
    public Vector<Point> getCurvePoints(){
        Long x,y;
        pointInverseMapping = new TreeMap<>();
        Map<Long, Vector<Long> > mx = new TreeMap<Long, Vector<Long> >();
        Map<Long, Vector<Long> > my = new TreeMap<Long, Vector<Long> >();
        Vector<Long> tmp;

        for(x = new Long(0) ; x < m ; x++)
        {
            Long v = ( (x*x*x) + (a*x) + b ) % m;
            if(mx.containsKey(v))
            {
                tmp = mx.get(v);
                tmp.add(x);
                mx.put(v, tmp);
            }
            else
            {
                tmp = new Vector<Long>();
                tmp.add(x);
                mx.put(v,tmp);
            }
        }

        for(y = new Long(0) ; y < m ; y++)
        {
            Long v = ( (y*y) ) % m;
            if(my.containsKey(v))
            {
                tmp = my.get(v);
                tmp.add(y);
                my.put(v, tmp);
            }
            else
            {
                tmp = new Vector<Long>();
                tmp.add(y);
                my.put(v,tmp);
            }
        }

        Vector<Point> points = new Vector<Point>();

        Set<Long> set = mx.keySet();
        for(Long s:set)
        {
            if(my.containsKey(s))
            {
                Vector<Long> vx = mx.get(s);
                Vector<Long> vy = my.get(s);
                for(Long x1:vx)
                {
                    for(Long y1:vy)
                    {
                        points.add(new Point(x1,y1));
                    }
                }
            }
        }
        points.add(new Point((long)0,(long)0));
        return points;
    }

    /*
    modInverse: Calculate the modular inverse of a with m as modulus
    Output:-
        Return a^-1 modulo m
     */
    public Long modInverse(Long a, Long m, Helper h)
    {
        Point inverse;
        //Start writing code here

        //End writing code here
        return inverse;
    }


    /*
    add: Add 2 Elliptic curve points
    Input:-
        p1: Point 1
        p2: Point 2
    Output:-
        Return a Point which is the addition of p1 and p2 according to Elliptic curve arithmetic.
     */
    public Point add(Point p1, Point p2, Helper h)
    {
        Point sum;
        //Start writing code here

        //End writing code here
        return sum;
    }

    /*
    addWithItself: Add a point to itself.
    Input:-
        p: Point p
    Output:-
        Return the sum of p and p using Elliptic curve arithmetic
     */
    public Point addWithItself(Point p, Helper h)
    {
        Point sum;
        //Start writing code here

        //End writing code here
        return sum;
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
    public Point multiply(Point p, Long l, Helper h)
    {
        Point product;
        //Start writing code here

        //End writing code here
        return product;
    }

    /*
    subtract: Return the difference between 2 curve points
    Input:-
        p1: Point p1
        p2: Point p2
    Output:-
        Return difference of p1 and p2.
     */
    public Point subtract(Point p1, Point p2, Helper h)
    {
        Point p3 = new Point(p2.getX(),m-p2.getY());
        return add(p1,p3, h);
    }
}
