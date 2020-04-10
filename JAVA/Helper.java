package JAVA;
import JAVA.Point;

import javafx.util.Pair;


import java.sql.*;
import java.util.*;

public class Helper {
    Map<Integer, Point> asciiToPoint;
    Map<Pair<Long, Long>, Integer> pointToAscii;

    public int getSegmentSize(Long m)
    {
        Long numPoints = (long)(m*m + 1);
        int size = 0;
        while(numPoints != 0)
        {
            numPoints /= 26;
            size++;
        }
        return size;
    }

    public void generateCharacterPointMappings(Vector<Point> curvePoints){
        Integer numPoints = curvePoints.size();
        Integer maxMappings = Math.min(numPoints, (int)65536);

        Vector<Integer> asciicodes = new Vector<Integer>();

        for(Integer i = (int)0; i<maxMappings ; i++)
        {
            asciicodes.add(i);
        }
        Collections.shuffle(asciicodes);

        Map<Integer, Point> asciiToPoint = new HashMap<Integer, Point>();
        Map<Pair<Long, Long>, Integer> pointToAscii = new HashMap<Pair<Long, Long>, Integer>();

        Integer sno = (int)0;

        for(Integer asciicode:asciicodes)
        {
            asciiToPoint.put(asciicode, curvePoints.get(sno));
            Point p = curvePoints.get(sno);
            pointToAscii.put(new Pair(p.getX(), p.getY()), asciicode);
            sno++;
        }
        this.asciiToPoint = asciiToPoint;
        this.pointToAscii = pointToAscii;
    }

    public Point charToPoint(char c)
    {
        return asciiToPoint.get((int)c);
    }

    public char pointToChar(Point p)
    {
        return (char)pointToAscii.get(new Pair(p.getX(), p.getY())).intValue();
    }

    public Vector<Point> streamToPoint(String stream, Long m)
    {
        int segmentSize = getSegmentSize(m);
        Vector<Point> v = new Vector<>();
        int i=0;
        while(i<stream.length())
        {
            String temp = stream.substring(i, i+segmentSize);
            i+=segmentSize;

            Long val = (long)0;
            int j;
            for(j=0;j<segmentSize;j++)
            {
                int d = temp.charAt(j) - 'a';
                val = val*26 + d;
            }
            v.add(new Point(val/m,val%m));
        }

        return v;
    }

    public String pointToStream(Point p, Long m)
    {
        String stream = "";
        int segmentSize = getSegmentSize(m);
        Long val = p.getX()*m + p.getY();
        String temp = "";
        for(int i=0;i<segmentSize;i++)
        {
            temp += (char)('a' + val%26);
            val /= 26;
        }
        for(int i=segmentSize-1;i>=0;i--)
        {
            stream += temp.charAt(i);
        }
        return stream;
    }


    public Point randomPoint(Vector<Point> curvePoints)
    {
        Integer numPoints = curvePoints.size();
        Random random=new Random();
        Integer r = random.nextInt(numPoints);

        return curvePoints.get(r);
    }

    public static Long randomNumber(Long m)
    {
        Random random=new Random();
        Long r = (long)(random.nextInt(m.intValue()-1))+1;
        return r;
    }

    public Long modulus(Long l, Long m)
    {
        while(l<0)
        {
            l += m;
        }
        l %= m;
        return l;
    }
}
