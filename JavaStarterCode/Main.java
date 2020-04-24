package JavaStarterCode;

import java.util.Scanner;
import java.util.Vector;

public class Main {

    /*
    generateReferencePoint: Generate Base point for elliptic curve
    Input:-
        curvePoints: List of points on the Elliptic Curve
    Output:-
        Return Base point or Generator
     */
    private static Point generateReferencePoint(Vector<Point> curvePoints, Helper h)
    {
        Point G = h.randomPoint(curvePoints);
        if(G.getX()==0 && G.getY()==0)
            G = generateReferencePoint(curvePoints, h);
        return G;
    }

    public static void main(String[] args){
        //Elliptic Curve Parameters
        Long a,b,m;
        a = (long)17;
        b = (long)50;
        m = (long)191;


        EllipticCurveArithmetic ec = new EllipticCurveArithmetic(a, b, m);
        Vector<Point> curvePoints = ec.getCurvePoints();

        Helper h = new Helper();
        h.generateCharacterPointMappings(curvePoints);

        //Base Point/Generator of Elliptic Curve
        Point G = Main.generateReferencePoint(curvePoints, h);
        EllipticCurveCryptography el = new EllipticCurveCryptography(G, (long)curvePoints.size(), h, ec);

        //Receiver's Public and Private keys
        Key receiver = el.generateKey(curvePoints.size());


        String message;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter message: ");
        message = sc.nextLine();
        System.out.println("Original message: "+message);

        String encryptedMessage = el.Encrypt(message, receiver.getPublicKey());
        System.out.println("Encrypted message: "+encryptedMessage);

        String decryptedMessage = el.Decrypt(encryptedMessage, receiver.getPrivateKey());
        System.out.println("Decrypted message: "+decryptedMessage);
    }
}
