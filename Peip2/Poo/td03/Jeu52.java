public class Jeu52
{
	Card deck[]= new Card[52];

	Jeu52()
	{
		int i = 0;


		for (Color c: Color.values())
		{
			for (Rank r: Rank.values())
			{
				this.deck[i] = new Card(r,c);
				i++;
			}
		}
	}

	public String toString()
	{
		String out = "";
		for (int i=0; i<52; i++)
		{
			out = out + this.deck[i] + "\n";
		}
		return(out);
	}
}
