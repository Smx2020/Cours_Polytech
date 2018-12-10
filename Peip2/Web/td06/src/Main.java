import java.io.*;

public class Main
{
	public static void main(String[] args)
	{
		HTTPServer myserver = null;

		try
		{
			myserver = new HTTPServer(1234,true);
		}
		catch(IOException e)
		{
			System.out.println("Problem while creating server!");
			System.exit(-1);	// code erreur <> 0 pour signaler qu'il y a u pbm
		}
		try
		{
			dialogue(myserver);
		}
		catch
		(IOException e) {
			System.out.println("Problem while talking to the client!");
		}
		finally {
			System.out.println("Killing the server");
			myserver.close();
		}
	}

	// methode de dialogue correspondant à l'écho par le serveur d'une (seule) chaine lue cad reçue (envoyée) du client
	private static void dialogue (Server myserver) throws IOException {
		myserver.acceptConn();
		String creply = null;
		creply = myserver.readline();
		if (creply != null) {
			//if not EOF, then the client is still there and we can write to him
			myserver.writeline(creply);
			creply = null;
		}
		myserver.closeConn();
	}

}