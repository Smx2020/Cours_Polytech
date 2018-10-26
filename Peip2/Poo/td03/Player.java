import PaD.*;

public class Player
{
	private String name="Bob";
	private Card[] myCard;
	private int length=0;

	Player(String name)
	{
		this.name = name;
	}

	public void getCard(Jeu52 j,int start,int end)
	{
		this.length = end - start + 1;
		this.myCard = new Card[length];
		for (int i=0;i < length - 1 ;i++ )
		{
			this.myCard[i] = j.getCard(start + i);
		}
	}

	public void showHand(PlancheADessin pad, double h)
	{
		Dessinable n = new Texte(0, h, this.name);

		for (int i=0; i<length-1; i++)
		{
			pad.ajouter(n);
			this.myCard[i].draw(pad, i*70, h + 25);
		}
	}

	public String toString()
	{
		String out = "";
		for (int i=0; i<length-1; i++)
		{
			out = out + this.myCard[i] + "\n";
		}
		return(out);
	}
}
