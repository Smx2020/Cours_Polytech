public class Main
{


	public static void main(String[] args)
	{
		String s = "Hello World!";
		System.out.println(s);
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
		*/

		Card c = new Card(Value.valet, Color.trefle);
		Card d = new Card(Value.neuf, Color.coeur);

		System.out.println(c.compareTo(d));
	}
}
