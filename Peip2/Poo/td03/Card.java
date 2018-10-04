public class Card
{
	private Color color;
	private Value value;

	public Card(Value v, Color c)
	{
		this.value = v;
		this.color = c;
	}

	public int compareTo(Card c)
	{
		return(this.value.value() - c.value.value());
	}

	public String toString()
	{
		return("" + this.value + " de " + this.color);
	}
}
