public abstract class Polygone
{
	protected Point origin;

	Polygone()
	{
		this.origin = new Point();
	}

	Polygone(Point p)
	{
		this.origin = p;
	}

	public abstract double lenght();
	public abstract double area();

}
