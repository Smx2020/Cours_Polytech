import java.io.*;

public class HTTPServer extends Server
{

	public HTTPServer() throws IOException
	{
		super(80,false);
	}
	public HTTPServer (int port) throws IOException
	{
		super(port, false);
	}

	public HTTPServer (int port,boolean v) throws IOException
	{
		super(port,v);
	}

	public static void main(String[] args)
	{
		HTTPServer serv=null;
		try
		{
			serv = new HTTPServer(1234, true);
		}
		catch (IOException e)
		{
			System.out.println("Problem while creating server!");
			System.exit(-1);	// code erreur <> 0 pour signaler qu'il y a u pb
		}
		try
		{
			while (true)
				serv.talk();
		}
		catch
		(IOException e) {
			System.out.println("Problem while talking to the client!");
		}
		finally {
			System.out.println("Killing the server");
			serv.close();
		}
	}

	public void talk() throws IOException
	{
		this.acceptConn();

		if (getRequest())
			repRequest();
		else
			errRequest();

		this.closeConn();
	}

	private boolean getRequest() throws IOException
	{
		boolean request = false;

		String creply = this.readline();
		if (creply != null) {
			String[] head = creply.split(" ");

			if (head.length == 3 && (head[0].equals("GET") || head[0].equals("POST"))) {
				request = true;
				while (creply != null && !(creply.isEmpty())) {
					creply = this.readline();
				}
			}

			if (head.equals("POST")) {
				creply = readcars(30);
			}
		}
		return(request);
	}

	private void repRequest()
	{
		this.writeline("HTTP/1.1 200 OK");
		this.writeline("Content-type: text/plain; charset = utf-8\n");
		this.writeline("La Requete a bien ete recu.");
	}

	private void errRequest()
	{
		this.writeline("HTTP/1.1 200 OK");
		this.writeline("Content-type: text/plain; charset = utf-8\n");
		this.writeline("Il y a eu une erreur lors de la requete.");
	}

}
