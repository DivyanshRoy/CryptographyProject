package JavaStarterCode;


import java.util.Vector;

public class EllipticCurveCryptography {

    Point G;
    Long numPoints;
    Helper h;
    EllipticCurveArithmetic ec;

    /*
    EllipticCurveCryptography: Initialise classes needed for Encryption
    Inputs:-
        G: Base Point of elliptic curve
        numPoints: Number of points in Elliptic curve
        h: Instance of Helper class
        ec: Instance of EllipticCurve class
     */
    public EllipticCurveCryptography(Point G, Long numPoints, Helper h, EllipticCurveArithmetic ec){
        this.G = G;
        this.numPoints = numPoints;
        this.h = h;
        this.ec = ec;
    }

    /*
    generateKey: Generate Public,Private key for user
    Input:-
        len: Number of points in Elliptic curve
    Output:-
        Return generated key
     */
    public Key generateKey(int len){
        Point publicKey;
        Long privateKey;
        //Generate a pair of Public and Private Keys
        //Start writing code here

        //End writing code here
        return new Key(publicKey,privateKey);
    }

    /*
    Encrypt: Encrypt a message using Receiver's Public Key
    Input:-
        str: Plaintext message
        public_key: Receiver's Public Key
    Output:-
        Return Encrypted message
     */
    public String Encrypt(String str, Point public_key)
    {
        int len=str.length(),i;
        Long r;
        Point A, B;
        String str1=new String("");
        for(i=0;i<len;i++)
        {
            r= Helper.randomNumber(numPoints);
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
        Return plaintext message
     */
    public String Decrypt(String str, Long private_key)
    {
        String plaintext = "";
        Vector<Point> v = h.streamToPoint(str, ec.getM());

        int len = v.size();
        for(int i=0;i<len;i+=2)
        {
            Point c1 = v.elementAt(i);
            Point c2 = v.elementAt(i+1);
            Point message;
            //Decrypt message character from c1 and c2 and append it to plaintext
            //Start writing code here

            //End writing code here
        }
        return plaintext;
    }

}
