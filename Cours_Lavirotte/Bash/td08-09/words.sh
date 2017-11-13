#!/bin/bash

list=$(cat test.txt |tr [:punct:] "\n" |tr [:space:] "\n"| grep -v '^$')
words=$(echo $list |wc -w)
u_words=$(echo $list |tr " " "\n"| sort -u |wc -w)
echo "Nombre de mots dans ce texte: "$words
echo "Nombre de mots différents dans ce texte: "$u_words

echo $list | tr " " "\n"|sort | uniq -c
