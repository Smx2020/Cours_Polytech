import PaD.*;

public class Main
{
	public static void main(String[] args) throws InterruptedException
	{
		PlancheADessin pad = new PlancheADessin(true);	//Creer un planche a dessin
		Jeu52 j = new Jeu52();						//Creer un jeu de 52 cartes
		Player p[] = new Player[4];					//Creer un tableau de 4 joueurs

		p[0] = new Player("Bob");					//Creer J1
		p[1] = new Player("Jean");					//Creer J2
		p[2] = new Player("Billy");					//Creer J3
		p[3] = new Player("George");				//Creer J4

		j.draw(pad,0,0);			//Affiche le jeu de carte triee sur le Pad
		System.out.println("Le jeu de carte triee :");
		System.out.println(j);		//Affiche le jeu de carte triee sur le terminal

		j.shuffle(103);				//Melanges les cartes (103 swap de 2 cartes)
		Thread.sleep(2000);			//Met en pause le programme pendant 2s
		pad.clear();				//efface le pad
		pad.redraw();				//Redessine le pad

		j.draw(pad,0,0);			//Affiche le jeu de carte melange sur le Pad
		System.out.println("Le jeu de carte melange :");
		System.out.println(j);		//Affiche le jeu de carte melange sur le terminal

		j.order();					//Range les cartes du jeu

		Thread.sleep(2000);			//Met en pause le programme pendant 2s
		pad.clear();				//efface le pad
		pad.redraw();				//Redessine le pad

		j.draw(pad,0,0);			//Affiche le jeu de carte triee sur le Pad
		System.out.println("Le jeu de carte triee :");
		System.out.println(j);		//Affiche le jeu de carte triee sur le terminal

		Thread.sleep(2000);			//Met en pause le programme pendant 2s
		pad.clear();				//efface le pad
		pad.redraw();				//Redessine le pad

		j.shuffle(103);				//Melanges les cartes (103 swap de 2 cartes)

		System.out.println("Main des joueurs :\n");

		for (int i=0; i<4 ; i++ )
		{
			p[i].getCard(j,i*13,(i+1)*13);	//Prend 13 cartes du jeu j
			p[i].showHand(pad, 130*i);		//Affiche sa main
			System.out.println(p[i]);		//affiche le joueur sur le terminal
		}

		Thread.sleep(2000);			//Met en pause le programme pendant 2s
		pad.clear();				//efface le pad
		pad.redraw();				//Redessine le pad

		System.out.println("Main des joueurs remelange:\n");

		for (int i=0; i<4 ; i++ )
		{
			p[i].shuffle(42);				//Melanges les cartes de la main (42 swap de 2 cartes)
			p[i].showHand(pad, 130*i);		//Affiche sa main
			System.out.println(p[i]);		//affiche le joueur sur le terminal
		}

		Thread.sleep(2000);			//Met en pause le programme pendant 2s
		pad.clear();				//efface le pad
		pad.redraw();				//Redessine le pad

		System.out.println("Main des joueurs range:\n");

		for (int i=0; i<4 ; i++ )
		{
			p[i].order();					//range les cartes de la main
			p[i].showHand(pad, 130*i);		//Affiche sa main
			System.out.println(p[i]);		//affiche le joueur sur le terminal
		}

		Thread.sleep(2000);			//Met en pause le programme pendant 2s
		pad.clear();				//efface le pad
		pad.redraw();				//Redessine le pad

		//	La partie jeu	//
		//boolean[] turn = true;

		Player player,bot;							//Creer joueur et bot
		player = new Player("player");
		bot = new Player("bot", false);		//les cartes de bot seront face cache
		j.setCard(Rank.valet, Color.trèfle, 51);
		j.shuffle(42);


		player.getCard(j,0,25);
		bot.getCard(j,25,51);

		player.showHand(pad,300);
		bot.showHand(pad,0);

	}
}
