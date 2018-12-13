public class Main {
	public static void main(String[] args)
	{
		File f = new File("test.c");
		File c = new File("test.h");
		File p = new File("Gros_Pron.mkv");
		File d = new File("test.py");
		File e = new File("elite.tilt");
		File g = new File("Shining Crystal.exe");
		File t = new File("Toto.ini");

		Folder fold = new Folder("Folder3");
		Folder fol = new Folder("Folder2");
		Folder fo = new Folder("Folder1");
		Folder fi = new Folder("Fifi");
		Folder fu = new Folder("Fufu");


		//System.out.println("Hello World!");

		fold.add(f);
		fold.add(c);
		fol.add(p);
		fol.add(fold);
		fol.add(d);
		fo.add(g);
		fo.add(fol);
		fo.add(fi);
		fi.add(t);
		fo.add(e);
		fo.add(fu);

		//f.display(0);
		fo.display(0);
	}
}
