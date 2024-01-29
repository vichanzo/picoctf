#!/usr/bin/env bash
wget -N --mirror --convert-links --adjust-extension --page-requisites --no-parent http://saturn.picoctf.net:56849/
echo "\n\nFlag:\n"
inner_flag=$( grep -rw 'saturn.picoctf.net:56849/' -e 'picoCTF' | cut -d "{" -f2 | cut -d "}" -f1 )  # Get middle part of flag
echo "picoCTF{"$inner_flag"}"| tee flag.txt
