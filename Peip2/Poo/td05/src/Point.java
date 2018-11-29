public class Point
{
	private double x = 0.0;
	private double y = 0.0;

	Point()
	{
		this.x = 0;
		this.y = 0;
	}

	Point(double x, double y)
	{
		this.x = x;
		this.y = y;
	}

	public double getX()
	{
		return x;
	}

	public double getY()
	{
		return y;
	}

	public String toString() {
		return(" Point (x = " + this.x +", y = "+ this.y +")");
	}
}
