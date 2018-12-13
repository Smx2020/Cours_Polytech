import java.util.*;

public class Folder extends Item{
	private LinkedList<Item> content = new LinkedList<>();

	public Folder(String name)
	{
		this.name = name;
	}


	public void add(Item f)
	{
		this.content.add(f);
	}

	@Override
	String getName()
	{
		return(this.name);
	}

	@Override
	void display(int n)
	{
		System.out.println("\t|".repeat(n) + this.name + " /");
		for (Item i:this.content)
			i.display(n+1);
	}
}
