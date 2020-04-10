package JAVA;
import JAVA.Point;



public class Key {
    private Point publicKey;
    private Long privateKey;

    public Key() {}

    public Key(Point publicKey, Long privateKey)
    {
        this.publicKey = publicKey;
        this.privateKey = privateKey;
    }

    public Point getPublicKey()
    {
        return publicKey;
    }

    public Long getPrivateKey()
    {
        return privateKey;
    }

    public void setPublicKey(Point publicKey)
    {
        this.publicKey = publicKey;
    }

    public void setPrivateKey(Long privateKey)
    {
        this.privateKey = privateKey;
    }
}
