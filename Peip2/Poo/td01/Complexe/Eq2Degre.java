public class Eq2Degre
{
	private static final double epsilon = 1E-10;
	private Complexe rac1,rac2;

	public Eq2Degre(double a, double b, double c)
	{
		this.resoudre(a,b,c);
	}

	private void resoudre(double a, double b, double c)
	{
		double d = b*b -4*a*c;

		if (d >= 0)
		{
			if (b > 0)
			{
				this.rac1 = new Complexe((-b + Math.sqrt(d)) / (2*a));
				this.rac2 = new Complexe((c/a) / this.rac1.partieReelle());
			}
			else
			{
				this.rac2 = new Complexe((-b + Math.sqrt(d)) / (2*a));
				this.rac1 = new Complexe((c/a) / this.rac2.partieReelle());
			}
		}
		else
		{
			this.rac1 = new Complexe(-b / (2*a), Math.sqrt(-d) / (2*a));
			this.rac2 = new Complexe(-b / (2*a), -Math.sqrt(-d) / (2*a));
		}
	}

	public Complexe premiereRacine()
	{
		return(this.rac1);
	}

	public Complexe deuxiemeRacine()
	{
		return(this.rac2);
	}

	public String toString()
	{
		return("r1 = " + this.rac1 + ", r2 = " + this.rac2);
	}
}
