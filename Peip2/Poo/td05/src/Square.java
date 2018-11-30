public class Square extends Rectangle
{
	private double side;

	Square()
	{
		super(1,1);
	}

	Square(double s)
	{
		super(s,s);
	}

	@Override
	protected void setL(double s)
	{
		super.setL(s);
		super.setl(s);
	}

	@Override
	protected void setl(double s)
	{
		this.setL(s);
	}

}
