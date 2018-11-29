import java.util.Random;	//importe les fonctions pour l'aleatoire
import PaD.*;				//importe les fonctions du pad

public class Jeu52
{
	Card deck[]= new Card[52];		//Creer un tableau de 52 cartes

	Jeu52()		//Constructeur du jeu de cartes
	{
		int i = 0;

		for (Color c: Color.values())			//c prendra la valeur de toutes les couleurs
		{
			for (Rank r: Rank.values())			//r prendra la valeur de tout les rangs
			{
				this.deck[i] = new Card(r,c);	//ajoute la carte au deck
				i++;
			}
		}
	}

	public Card getCard(int n)					//donne la carte n du deck
	{
		return(deck[n]);
	}

	public void shuffle(int n)					//Melange les cartes (fais n swapp de 2 cartes)
	{
		Card c;
		int a,b;

		for (int i = 0; i < n ;i++)				// Fais n fois
		{
			a = this.randInt(0, 51);			// 1 ere carte a echanger
			b = this.randInt(0, 51);			// 2 eme carte a echanger

			c = this.deck[a];					// Echange les 2 cartes
			this.deck[a] = this.deck[b];
			this.deck[b] = c;
		}
	}

	public void	order()					//Range les cartes dans l'ordre (tri a bulles)
	{
		Card c;							//Pointeur de carte tampon
		Boolean end = false;			//Indique si le triage est finis
		while (!end)
		{
			end = true;
			for (int i=0; i<51; i++)
			{
				if (this.deck[i+1].sup(this.deck[i]))
				{
					end = false;					//Indique que le jeu n'etait pas organise
					c = this.deck[i];				//Remet les 2 cartes dans l'ordre
					this.deck[i] = this.deck[i+1];
					this.deck[i+1] = c;
				}
			}
		}
	}

	public void draw(PlancheADessin pad, double x, double y)	//Affiche le jeu de carte sur la pad en x,y
	{
		for (int i=0;i<4 ;i++ )										//La rangee
			for (int j=0;j< 13 ;j++ )								//la colonne
				deck[i*13 +j].draw(pad,x + j*70, y + i*100);		//Affiche la colonne
	}

	private int randInt(int min, int max)		//Donne un entier aleatoire entre min et max
	{
		if (min >= max) {
			throw new IllegalArgumentException("max must be greater than min");
		}

		Random r = new Random();
		return r.nextInt((max - min) + 1) + min;
	}

	public String toString()	//Convertit le jeu de carte en une chaine de caractere
	{
		String out = "";
		for (int i=0; i<52; i++)
		{
			out = out + this.deck[i] + "\n";
		}
		return(out);
	}
}
