public class Main
{
	public static void main(String [] args)
	{
		Complexe c = new Complexe(50,70);
		Complexe d = new Complexe(50,70.00001);

		Eq2Degre e = new Eq2Degre(1E-13,-200,1);

		System.out.println("Hello World!");

		System.out.println(c);
		System.out.println(e);
	}
}
