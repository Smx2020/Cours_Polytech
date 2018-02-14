/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: olivier <olivier@doussaud.org>             +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/01/19 17:45:54 by olivier           #+#    #+#             */
/*   Updated: 2018/02/14 14:36:30 by olivier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "linked_list.h"
#include "display.h"
#include "bot.h"

int main(int argc, char const *argv[])
{
	linked_list *test= NULL;
	int i;
	int *data;

	//set_data(&test,59,59);
	//set_data(&test,99,99);


	i = 0;
	while (i<100)
	{
		get_data(&test,i);
		i++;
	}

	i = 0;
	while (i<100)
	{
		set_data(&test,i,i);
		i++;
	}

	/*
	i = 0;
	while (i<100)
	{
		if (i%10 == 0)
		put_str("\n");
		put_nb(get_data(&test,i));
		put_str(",");
		i++;
	}*/
	put_nb(bot(403));
	//disp();
	// i = 0;
	// data = test->data;
	// while (i < 60)
	// {
	// 	if (i % 10 == 0)
	// 	put_str("\n");
	// 	put_nb(data[i]);
	// 	put_str(",");
	// 	i++;
	// }
    //
	// test = test->next;
	// data = test->data;
	// i = 0;
	// while (i < 40)
	// {
	// 	if (i % 10 == 0)
	// 	put_str("\n");
	// 	put_nb(data[i]);
	// 	put_str(",");
	// 	i++;
	// }
	/*i = 1;
	while (i<3)
	{
		put_nb(i);
		set_data(&test,i,i);
		i++;
	}
	put_str("\n####\n");
	i = 50;
	while (i<60)
	{
		data = test->data;
		put_nb(data[0]);
		test = test->next;
		i++;
	}*/
	return 0;
}
