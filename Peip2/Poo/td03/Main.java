import PaD.*;

public class Main
{
	public static void main(String[] args)
	{
		PlancheADessin pad = new PlancheADessin();
		Jeu52 j = new Jeu52();
		Player p[] = new Player[4];

		p[0] = new Player("Bob");
		p[1] = new Player("Jean");
		p[2] = new Player("Billy");
		p[3] = new Player("George");

		j.shuffle(103);

		for (int i=0; i<4 ; i++ )
		{
			p[i].getCard(j,i*13,(i+1)*13);
			p[i].showHand(pad, 130*i);
		}
		
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

		//System.out.println(c.compareTo(d));
	}
}
