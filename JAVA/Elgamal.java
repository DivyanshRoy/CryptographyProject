package JAVA;
import JAVA.Point;


import java.util.Vector;

public class Elgamal {

    Point G;
    Long numPoints;
    Helper h;
    EllipticCurve ec;

    public Elgamal(Point G, Long numPoints, Helper h, EllipticCurve ec){
        this.G = G;
        this.numPoints = numPoints;
        this.h = h;
        this.ec = ec;
    }

    public Key generateKey(int len){
        Point publicKey;
        Long privateKey;
        privateKey = Helper.randomNumber((long)len);
        publicKey = ec.multiply(G, privateKey, h);
        return new Key(publicKey,privateKey);
    }

    public String Encrypt(String str, Point public_key)
    {
        int len=str.length(),i;
        Long r;
        Point A, B;
        String str1=new String("");
        for(i=0;i<len;i++)
        {
            r=Helper.randomNumber(numPoints);
            A=ec.multiply(public_key, r, h);
            B=ec.add(h.charToPoint(str.charAt(i)), ec.multiply(G, r, h), h);
            str1+=h.pointToStream(A, ec.getM());
            str1+=h.pointToStream(B, ec.getM());
        }
        return str1;
    }

    public String Decrypt(String str,Long private_key)
    {
        String str1 = "";
        Vector<Point> v = h.streamToPoint(str, ec.getM());

        int len = v.size();

        for(int i=0;i<len;i+=2)
        {
            Point c1 = v.elementAt(i);
            Point c2 = v.elementAt(i+1);
            Point DM=ec.subtract(c2, ec.multiply(c1, ec.modInverse(private_key, numPoints, h), h), h);
            str1+=h.pointToChar(DM);
        }

        return str1;
    }

}
