package JavaStarterCode;


import java.util.Vector;

public class Elgamal {

    Point G;
    Long numPoints;
    Helper h;
    EllipticCurve ec;

    /*
    Elgamal: Initialise classes needed for Encryption
    Inputs:-
        G: Base Point of elliptic curve
        numPoints: Number of points in Elliptic curve
        h: Instance of Helper class
        ec: Instance of EllipticCurve class
     */
    public Elgamal(Point G, Long numPoints, Helper h, EllipticCurve ec){
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
        privateKey = Helper.randomNumber((long)len);
        publicKey = ec.multiply(G, privateKey, h);
        return new Key(publicKey,privateKey);
    }

    /*
    keyInverse: Get Private Key for a user's Public Key
    Input:-
        p: Public Key
    Output:-
        Return Private Key for p
     */
    private Long keyInverse(Point p){
        for(Long i=(long)1;i<numPoints;i++){
            Point m = ec.multiply(p, i, h);
            if(m.getX()==G.getX() && m.getY()==G.getY())
                return i;
        }
        return (long)0;
    }

    /*
    Encrypt: Encrypt a message using Receiver's Public Key abd Sender's Private Key
    Input:-
        str: Plaintext message
        public_key: Receiver's Public Key
        private_key: Sender's Private Key
    Output:-
        Return Encrypted message
     */
    public String Encrypt(String str, Point public_key, Long private_key)
    {
        int len=str.length(),i;
        Long r;
        Point A, B;
        Point K = ec.multiply(public_key, private_key, h);
        String str1=new String("");
        for(i=0;i<len;i++)
        {
            r= Helper.randomNumber(numPoints);
            A=ec.multiply(K, r, h);
            B=ec.add(h.charToPoint(str.charAt(i)), ec.multiply(G, r, h), h);
            str1+=h.pointToStream(A, ec.getM());
            str1+=h.pointToStream(B, ec.getM());
        }
        return str1;
    }

    /*
    Decrypt: Decrypt the ciphertext using Sender's Public Key and Receiver's Private Key
    Input:-
        str: Ciphertext
        public_key: Sender's Public Key
        private_key: Receiver's Private Key
    Output:-
        Return generated key
     */
    public String Decrypt(String str, Point public_key, Long private_key)
    {
        String str1 = "";
        Vector<Point> v = h.streamToPoint(str, ec.getM());

        int len = v.size();
        Point K = ec.multiply(public_key, private_key, h);
        Long k_inverse = keyInverse(K);
        for(int i=0;i<len;i+=2)
        {
            Point c1 = v.elementAt(i);
            Point c2 = v.elementAt(i+1);
            Point DM=ec.subtract(c2, ec.multiply(c1, k_inverse, h), h);
            str1+=h.pointToChar(DM);
        }

        return str1;
    }

}
