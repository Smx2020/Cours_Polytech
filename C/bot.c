#include "linked_list.h"
#include "display.h"
#include <stdlib.h>

#define WIN 1
#define LOST -1

linked_list *dico=NULL;

int	rec(int allu, int myTurn)
{
	int i = 1;
	int check = get_data(&dico,allu);
	int value;

	if (allu <= 0)
		return((myTurn) ? LOST : WIN);

	// if (check != 0)
	// {
	// 	if (myTurn)
	// 		return(check);
	// 	return(-check);
	// }

	if (myTurn)
	{
		while (i < 4)
		{
			value =rec(allu-i,!myTurn);
			set_data(&dico,allu-i,value);
			if (value == WIN)
				return(WIN);
			i++;
		}
		return(LOST);
	}
	else
	{
		while (i < 4)
		{
			value =rec(allu-i,!myTurn);
			set_data(&dico,allu-i,-value);
			if (value == LOST)
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
void disp(void)
{
	put_str("Test\n");
	put_nb(get_data(&dico,1));
	put_nb(get_data(&dico,2));
	put_nb(get_data(&dico,3));
	put_nb(get_data(&dico,4));
	put_nb(get_data(&dico,5));
	put_str("Test\n");
}
