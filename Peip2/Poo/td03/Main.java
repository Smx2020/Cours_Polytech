import PaD.*;

public class Main
{


	public static void main(String[] args)
	{
		PlancheADessin pad = new PlancheADessin();
		Jeu52 j = new Jeu52();
		/*
		for (Color c: Color.values())
		{
			System.out.println(c);
		}
		System.out.println("");
		for (Value v: Value.values())
		{
			System.out.println("" + v + " : " + v.value );
		}


		Card c = new Card(Rank.valet, Color.pique);
		Card d = new Card(Rank.neuf, Color.coeur);
		c.draw(pad,0,0);
		d.draw(pad,64,0);
		*/
		System.out.println(j);
		j.shuffle(52);
		System.out.println(j);
		j.draw(pad,10,10);
		//System.out.println(c.compareTo(d));
	}
}
