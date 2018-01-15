#define WIN 1
#define LOST -1

int	rec(int allu, int myTurn)
{
	int i = 1;
	if (allu <= 0)
		return((myTurn) ? WIN : LOST);
	if (myTurn)
	{
		while (i < 4)
		{
			if (rec(allu-i,!myTurn) == WIN)
				return(WIN);
			i++;
		}
		return(LOST);
	}
	else
	{
		while (i < 4)
		{
			if (rec(allu-i,!myTurn) == LOST)
				return(LOST);
			i++;
		}
		return(WIN);
	}
}

int	bot(int allu)
{
	int i = 1;
	while (i < 4)
	{
		if (rec(allu - i, 0) == 1)
			return(i);
		i += 1;
	}
	return(1);
}

int main(int argc, char const *argv[])
{
	bot(35);
	return 0;
}
