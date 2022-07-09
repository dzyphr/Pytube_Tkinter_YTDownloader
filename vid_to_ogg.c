#include <stdint.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 65792
int convert(char* argstr1);
int main(int argc, char* argv[])
{
	if (argc != 2)
	{
		printf("\nProvide FilePath\n");
		exit(1);
	}
	char* argstr1 = argv[1];
	convert(argstr1);
}
int convert(char* path)
{
	char init[SIZE] = "\'";
	strcat(init, path);
	strcat(init, "\'");
	char cmd[SIZE];
	char cmd_1[SIZE] = "ffmpeg -i ";
	char cmd_2[SIZE] = " -vn -ar 44100 -ac 2 -ab 192k -f ogg ";
	char cmd_3[SIZE]= " -y"; //will replace existing
	strcat(cmd_1, init);
	strcpy(cmd, cmd_1);
	strcat(cmd, cmd_2);
	int initlen = strlen(init);
	init[initlen-5] = '\0';//remove previous extention
	strcat(init, ".ogg\'"); //add oggvorbis ext
	strcat(cmd, init);
	strcat(cmd , cmd_3);	
	//printf("%s", cmd);
	system(cmd);
}
