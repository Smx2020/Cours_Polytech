import PaD.*;	//importe les fonctions du pad

public class Card
{
	private Color color;		//Couleur de la carte (ex: pique)
	private Rank rank;			//Valeur de la carte (ex: as)
	Image img;					//Image de la carte

	Card(Rank r, Color c)	//Constructeur de la carte necessitant la Couleur et le rang
	{
		this.rank = r;
		this.color = c;
		this.img = new Image(this.toFile());
	}

	public	Color getColor()	//Getter de color
	{
		return(this.color);
	}
	public	Rank getRank()		//Getter de rank
	{
		return(this.rank);
	}

	public void draw(PlancheADessin pad, double x, double y)	//Affiche la carte sur le pad en x,y
	{
		img.setOrig(x,y);
		pad.ajouter(img);
	}

	public int compareTo(Card c)								//Compare les valeurs des cartes ()
	{
		return(this.rank.value() - c.rank.value());
	}

	public Boolean sup(Card c)									//Donne l'ordre entre this et c (this <= c)
	{
		if (this.color.ordinal() == c.getColor().ordinal())
		{
			if (this.rank.ordinal() > c.getRank().ordinal())
				return(false);
			else
				return(true);
		}
		else
			return(this.color.ordinal() <= c.getColor().ordinal());
	}

	private String toFile()										//Donnne l'adresse du fichier image en fonction de la carte
	{
		return("../Cartes/" + this.rank + "-" + this.color + ".gif");
	}

	public String toString()									//Convertit l'objet carte en chaine de caractere
	{
		return("" + this.rank + " de " + this.color);
	}
}
