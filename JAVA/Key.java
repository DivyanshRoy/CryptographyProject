package JAVA;


public class Key {
    private Point publicKey;
    private Long privateKey;

    public Key() {}

    /*
    Key: Initialise class with a user's Public and Private Key
    Input:-
        publicKey: User's Public Key
        privateKey: User's Private Key
     */
    public Key(Point publicKey, Long privateKey)
    {
        this.publicKey = publicKey;
        this.privateKey = privateKey;
    }

    /*
    getPublicKey: Return Public Key for user
     */
    public Point getPublicKey()
    {
        return publicKey;
    }

    /*
    getPrivateKey: Return Private Key for user
     */
    public Long getPrivateKey()
    {
        return privateKey;
    }

    /*
    setPublicKey: Store Public Key of user
     */
    public void setPublicKey(Point publicKey)
    {
        this.publicKey = publicKey;
    }

    /*
    setPrivateKey: Store Private Key of user
     */
    public void setPrivateKey(Long privateKey)
    {
        this.privateKey = privateKey;
    }
}
