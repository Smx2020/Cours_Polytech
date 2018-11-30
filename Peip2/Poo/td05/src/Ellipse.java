public class Ellipse extends Polygone
{
	protected double a;
	protected double b;

	Ellipse()
	{
		super();
		this.a = 0;
		this.b = 0;
	}

	Ellipse(double r)
	{
		super();
		this.a = r;
		this.b = r;
	}

	Ellipse(double a, double b)
	{
		super();
		assert(a <= b);
		this.a = a;
		this.b = b;
	}

	public void setA(double a)
	{
		this.a = a;
	}

	public void setB(double b)
	{
		this.b = b;
	}

	public double area()
	{
		return(Math.PI*a*b);
	}

	public double lenght()
	{
		return(Math.PI*Math.sqrt( 2*(a*a + b*b)) );
	}
}