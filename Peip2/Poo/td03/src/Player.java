import PaD.*;	//importe les fonctions du pad
import java.util.Random;	//importe les fonctions pour l'aleatoire

public class Player
{
	private String name="Bob";		//Le nom du joueur
	private Card[] myCard;			//Sa main de cartes
	private int length=0;			//nb de cartes en main
	private boolean show = true;

	Player(String name)	//Constructeur necessitant que le nom
	{
		this.name = name;
	}

	Player(String name, boolean show)
	{
		this.name = name;
		this.show = show;
	}

	public void getCard(Jeu52 j,int start,int end)	//Prend les carte de start a end du jeu j
	{
		this.length = end - start + 1;		//Calcul le nb de cartes
		this.myCard = new Card[length];		//Cree un tableau assez grand pour
		for (int i=0;i < length - 1 ;i++ )
		{
			this.myCard[i] = j.getCard(start + i);	//Recupere les cartes concerne
		}
	}

	public void	order()					//Range les cartes dans l'ordre (tri a bulles)
	{
		Card c;							//Pointeur de carte tampon
		Boolean end = false;			//Indique si le triage est finis
		while (!end)
		{
			end = true;
			for (int i=0; i<this.length - 2; i++)
			{
				if (this.myCard[i+1].sup(this.myCard[i]))
				{
					end = false;					//Indique que le jeu n'etait pas organise
					c = this.myCard[i];				//Remet les 2 cartes dans l'ordre
					this.myCard[i] = this.myCard[i+1];
					this.myCard[i+1] = c;
				}
			}
		}
	}

	public void shuffle(int n)					//Melange les cartes (fais n swapp de 2 cartes)
	{
		Card c;
		int a,b;

		for (int i = 0; i < n ;i++)				// Fais n fois
		{
			a = this.randInt(0, this.length-2);			// 1 ere carte a echanger
			b = this.randInt(0, this.length-2);			// 2 eme carte a echanger

			c = this.myCard[a];					// Echange les 2 cartes
			this.myCard[a] = this.myCard[b];
			this.myCard[b] = c;
		}
	}

	public void showHand(PlancheADessin pad, double h)	//afiche la main sur le pad a la hauteur h
	{
		Dessinable n = new Texte(0, h, this.name);		//Cree le nom du joueur en texte affichable par le pad
		pad.ajouter(n);									//affiche le nom du joueur sur le pad

		for (int i=0; i<length-1; i++)
		{
			if (show)
				this.myCard[i].draw(pad, (i%13)*70, h + 100*(i/13) + 25);		//affiche la carte
			else
				this.myCard[i].blankCardDraw(pad, (i%13)*70, h + 100*(i/13) + 25);		//affiche une carte face cache
		}
	}

	private int randInt(int min, int max)		//Donne un entier aleatoire entre min et max
	{
		if (min >= max) {
			throw new IllegalArgumentException("max must be greater than min");
		}

		Random r = new Random();
		return r.nextInt((max - min) + 1) + min;
	}

	public String toString()		//Convertit le joueur en une chaine de caractere
	{
		String out = this.name + " :\n";
		for (int i=0; i<length-1; i++)
		{
			out = out + this.myCard[i] + "\n";
		}
		return(out);
	}
}
