#include <stdlib.h>
#include <string.h>
#include <stdio.h>
int main(int argc, char* argv[])
{
	char* argument = argv[1];
	char* argument2 = argv[2];
	if (argc == 1)
	{
		printf("run this with the system as an argument\nexample:	./pytube mac\nchoices:	ubuntu, mac");
		exit(1);
	}
	if (argc > 3)
	{
		printf("too many arguments!");
		exit(1);
	}
	char* ubuntu = "ubuntu";
	char* mac = "mac";
	if (strcmp(argument, ubuntu) == 0)
	{
		system("gcc pytube_ubuntu.c -o pytube_ubuntu && ./pytube_ubuntu");
	}
	else if (strcmp(argument, mac) == 0)
	{
		if (argc > 2)
		{
			if (strcmp(argument2, "brewed") == 0)
			{
				system("gcc pytube_mac.c -o pytube_mac && ./pytube_mac allbrewed");
	printf("allbrewed");
			}
			else
			{
 printf("NOT allbrewed");
				system("gcc pytube_mac.c -o pytube_mac && ./pytube_mac");
			}
		}
		else
		{
 printf("NOT allbrewed");
			system("gcc pytube_mac.c -o pytube_mac && ./pytube_mac");       
		}
	}
	printf("%s", argv[1]);
}
