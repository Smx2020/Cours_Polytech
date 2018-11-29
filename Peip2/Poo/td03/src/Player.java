import PaD.*;	//importe les fonctions du pad

public class Player
{
	private String name="Bob";		//Le nom du joueur
	private Card[] myCard;			//Sa main de cartes
	private int length=0;			//nb de cartes en main

	Player(String name)	//Constructeur necessitant que le nom
	{
		this.name = name;
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

	public void showHand(PlancheADessin pad, double h)	//afiche la main sur le pad a la hauteur h
	{
		Dessinable n = new Texte(0, h, this.name);		//Cree le nom du joueur en texte affichable par le pad
		pad.ajouter(n);									//affiche le nom du joueur sur le pad

		for (int i=0; i<length-1; i++)
		{
			this.myCard[i].draw(pad, i*70, h + 25);		//affiche les cartes 1 par 1
		}
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
