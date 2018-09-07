/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: olivier <olivier@doussaud.org>             +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/06/11 10:51:54 by olivier           #+#    #+#             */
/*   Updated: 2018/06/11 11:07:16 by olivier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void ft_putchar(char c)
{
	write(1,&c,1);
}

void ft_putstr(char *str)
{
	while(*str)
	{
		ft_putchar(*str);
		str++;
	}
}

void ft_put_nb(int n)
{
	if (n == -2147483648)
	{
		ft_putstr("-2147483648");
		return;
	}
	if (n < 0)
	{
		ft_putchar('-');
		n = -n;
	}
	if ( n%10 == n)
		ft_putchar('0' + n);
	else
	{
		ft_put_nb(n/10);
		ft_putchar('0' + n%10);
	}
}

int main(int argc, char *argv[])
{
	int i = 1;
	while (i < argc)
	{
		ft_putstr(argv[i]);
		i++;
	}
	ft_put_nb(-1456158);
	return 0;
}
