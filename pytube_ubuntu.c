#include <stdio.h>
#include <stdlib.h>
int main()
{
	system("sudo apt install python3 ffmpeg gcc && gcc vid_to_ogg.c -o vid_to_ogg && pip install pytube ");
	system("python3 pytube_playlists_tk.py");
}
