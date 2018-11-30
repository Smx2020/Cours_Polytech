public class Main
{
	public static void main(String[] args)
	{
		Rectangle r = new Rectangle(5,5);
		Square s = new Square(1);
		Ellipse e = new Ellipse(1,1);

		s.setl(10);
		System.out.println(r);
		System.out.println(s);
		System.out.println("" + e.area() + " " + e.lenght());

	}
}
