#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
int main(int argc, char* argv[])
{
	if (argc > 1)
	{
		printf("%s - %s", argv[0], argv[1]);
		if (strcmp(argv[1], "allbrewed")==0)
		{
		}
	}else
	{
		system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"");
	}
	//program dependencies installed through homebrew
	system("brew install \\python@3.10 \\ffmpeg \\gcc \\python-tk@3.10 \\virtualenv");
	//build mp4 to ogg conversion tool with gcc and install pytube dependency with pip manager
	system("gcc vid_to_ogg.c -o vid_to_ogg");
	system("virtualenv pytube_env ");
	system("source pytube_env/bin/activate && pip install pytube && python3 pytube_playlists_tk.py && deactivate && rm -r pytube_env");
}
