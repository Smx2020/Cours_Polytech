#include <unistd.h>

void ft_putstr(char* str)
{
	while (*str)
	{
		write(1,str,1);
		str++;
	}
}

int main(int argc, char const *argv[])
{
	char a = 254;
	ft_putstr(&a);
	return 0;
}
