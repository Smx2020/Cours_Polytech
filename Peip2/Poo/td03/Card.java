import PaD.*;

public class Card
{
	private Color color;
	private Rank rank;
	Image img;

	public Card(Rank r, Color c)
	{
		this.rank = r;
		this.color = c;
		this.img = new Image(this.toFile());
	}

	public void draw(PlancheADessin pad, double x, double y)
	{
		img.setOrig(x,y);
		pad.ajouter(img);
	}

	public int compareTo(Card c)
	{
		return(this.rank.value() - c.rank.value());
	}

	private String toFile()
	{
		return("Cartes/" + this.rank + "-" + this.color + ".gif");
	}

	public String toString()
	{
		return("" + this.rank + " de " + this.color);
	}
}
