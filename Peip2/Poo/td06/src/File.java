public class File extends Item {
	public File(String name)
	{
		this.name = name;
	}

	@Override
	String getName()
	{
		return (this.name);
	}

	@Override
	void display(int n)
	{
		System.out.println("\t|".repeat(n) + this.name);
	}
}
