import java.util.Random;
import PaD.*;

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

	public void shuffle(int n)
	{
		Card c;
		int a,b;

		for (int i = 0; i < n ;i++)
		{
			a = this.randInt(0, 51);
			b = this.randInt(0, 51);

			c = this.deck[a];
			this.deck[a] = this.deck[b];
			this.deck[b] = c;
		}
	}

	public void draw(PlancheADessin pad, double x, double y)
	{
		for (int i=0;i<4 ;i++ )
			for (int j=0;j< 13 ;j++ )
				deck[i*13 +j].draw(pad,x + j*70, y + i*100);
	}

	private int randInt(int min, int max)
	{
		if (min >= max) {
			throw new IllegalArgumentException("max must be greater than min");
		}

		Random r = new Random();
		return r.nextInt((max - min) + 1) + min;
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
