/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   display.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: olivier <olivier@doussaud.org>             +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/01/21 13:47:59 by olivier           #+#    #+#             */
/*   Updated: 2018/01/21 13:50:39 by olivier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include "display.h"

void put_char(char c)
{
	write(1,&c,1);
}

void put_str(char* str)
{
	while (*str)
	{
		write(1,str,1);
		str++;
	}
}

void put_nb(int n)
{
	if (n == -2147483648 )
	{
		put_str("-2147483648");
		return;
	}
	if (n < 0)
	{
		put_char('-');
		put_nb(-n);
		return;
	}
	if (n < 10)
		put_char(n + '0');
	else
	{
		put_nb(n/10);
		put_char(n%10 + '0');
	}
}
