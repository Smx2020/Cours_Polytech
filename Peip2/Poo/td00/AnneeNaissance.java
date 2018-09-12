import java.util.Scanner;

public class AnneeNaissance
{
	public static void main(String [] args)
	{
		String prenom;
		int age;
		Scanner sc = new Scanner(System.in);
		// créer un objet Scanner pour lire sur l'entrée standard
		// lire le prénom
		System.out.print("Votre prénom : ");
		prenom = sc.nextLine();
		// lire l'âge
		System.out.print("Votre âge : ");
		age = sc.nextInt();
		// afficher l'année de naissance
		System.out.println(prenom + ",vous êtes né en " + (2018 - age));

		int i;
		int moy,nb;

		System.out.print("Nombre de notes : ");
		nb = sc.nextInt();
		i = 0;
		moy = 0;
		while (i < nb)
		{
			System.out.print("Note n°" + i + 1 + " :");
			moy += sc.nextInt();
			i++;
		}
		System.out.println( "" + moy/nb);
	}
}
