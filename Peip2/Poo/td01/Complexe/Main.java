public class Main
{
	public static void main(String [] args)
	{
		Complexe c = new Complexe(50,70);
		Complexe d = new Complexe(50,70.00001);

		System.out.println("Hello World!");

		System.out.println("" + c.different(d));
	}
}
