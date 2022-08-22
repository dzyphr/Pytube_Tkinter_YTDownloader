#include <stdlib.h>
#include <string.h>
#include <stdio.h>
int main(int argc, char* argv[])
{
	char* argument = argv[1];
	if (argc == 1)
	{
		printf("run this with the system as an argument\nexample:	./pytube mac\nchoices:	ubuntu, mac");
		exit(1);
	}
	if (argc > 2)
	{
		printf("too many arguments!");
		exit(1);
	}
	char* ubuntu = "ubuntu";
	char* mac = "mac";
	if (strcmp(argument, ubuntu) == 0)
	{
		printf("workin");
		system("gcc pytube_ubuntu.c -o pytube_ubuntu && ./pytube_ubuntu");
	}
	else if (strcmp(argument, mac) == 0)
	{
		//soon
	}
	printf("%s", argv[1]);
}
