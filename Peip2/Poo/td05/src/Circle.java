public class Circle extends Ellipse
{
	private double r;

	Circle()
	{
		super(1,1);
		this.r = 1;
	}

	Circle(double r)
	{
		super(r,r);
		this.r = r;
	}

	@Override
	public void setA(double r)
	{
		super.setA(r);
		super.setB(r);
	}

	@Override
	public void setB(double r)
	{
		super.setA(r);
		super.setB(r);
	}
}
