/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package JavaStarterCode;


/**
 *
 * @author singh
 */
public class Point {
    private Long x,y;
    
    public Point() {}

    /*
    Point: Initialise with x and y coordinates of Elliptic curve point
     */
    public Point(Long x, Long y)
    {
        this.x = x;
        this.y = y;
    }

    /*
    getX: Return x coordinate of Elliptic curve point
     */
    public Long getX()
    {
        return x;
    }

    /*
    getY: Return y coordinate of Elliptic curve point
     */
    public Long getY()
    {
        return y;
    }

    /*
    setX: Store x coordinate of Elliptic curve point
     */
    public void setX(Long x)
    {
        this.x = x;
    }

    /*
    setY: Store y coordinate of Elliptic curve point
     */
    public void setY(Long y)
    {
        this.y = y;
    }
}
