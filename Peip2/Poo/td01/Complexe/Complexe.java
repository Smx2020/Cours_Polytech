public class Complexe
{
	private double reel;
	private double img;
	public static Complexe I = new Complexe(0,1);

	public Complexe()
	{
		this.reel = 0;
		this.img = 0;
	}

	public Complexe(double reel, double img)
	{
		this.reel = reel;
		this.img = img;
	}

	public double partieReelle()
	{
		return(this.reel);
	}

	public double partieImaginaire()
	{
		return(this.img);
	}

	public double rho()
	{
		return(Math.sqrt(this.reel*this.reel + this.img*this.img));
	}

	public double theta()
	{
		double o;		//doesn't work with (0, 0)
		o = Math.atan(this.img/this.reel);
		if (this.reel < 0)
		{
			if (this.img > 0)
				return(Math.PI + o);
			else
				return(-Math.PI + o);
		}
		return(o);
	}

	public static Complexe polComplexe(double n, double p)
	{
		double x,y;
		x = p*Math.cos(n);
		y = p*Math.sin(n);
		Complexe c = new Complexe(x,y);
		return(c);
	}

	public Complexe plus(Complexe c)
	{
		double x,y;
		x = this.reel + c.partieReelle();
		y = this.img + c.partieImaginaire();

		return(new Complexe(x,y));
	}

	public Complexe moins(Complexe c)
	{
		double x,y;
		x = this.reel - c.partieReelle();
		y = this.img - c.partieImaginaire();

		return(new Complexe(x,y));
	}

	public Complexe mult(Complexe c)
	{
		double p,o;
		p = this.rho() * c.rho();
		o = this.theta() + c.theta();
		return(Complexe.polComplexe(o,p));
	}

	public Complexe div(Complexe c)
	{
		double p,o;
		p = this.rho() / c.rho();
		o = this.theta() - c.theta();
		return(Complexe.polComplexe(o,p));
	}

	public boolean egal(Complexe c)
	{
		boolean c1,c2;
		c1 = this.reel == c.partieReelle();
		c2 = this.img == c.partieImaginaire();
		return(c1 && c2);
	}

	public boolean different(Complexe c)
	{
		return(!this.egal(c));
	}

	public String toString()
	{
		return("(" + reel + ", " + img + ")");
	}
}
