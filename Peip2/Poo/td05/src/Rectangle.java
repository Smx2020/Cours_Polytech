import org.w3c.dom.css.Rect;

public class Rectangle extends Polygone
{
	protected double l;
	protected double L;

	Rectangle()
	{
		super();
		this.l = 0;
		this.L = 0;
	}

	Rectangle(double L, double l)
	{
		super();
		this.L = L;
		this.l = l;
	}

	Rectangle(Point p, double L, double l)
	{
		super(p);
		this.L = L;
		this.l = l;
	}

	public String toString()
	{
		String out = "";
		int maxI = (int)(this.l*2);
		int maxJ = (int)(this.L*2);

		for(int i=0; i < maxI; i++)
		{
			for(int j=0;j < maxJ; j++)
			{
				if (i == 0 || i == maxI-1)
				{
					if (j == 0 || j == maxJ-1)
						out = out + "+";
					else
						out	= out + "-";
				}
				else if (j == 0 || j == maxJ-1)
					out = out + "|";
				else
					out = out + " ";
			}
			out = out + "\n";
		}

	return (out);
	}
}
