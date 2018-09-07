#!/bin/bash
echo -n "Quelle est votre année de naissance ?"
read n
anne=$(date +"%Y")
let age=($anne-$n)
echo "Vous êtes né en "$d", vous avez donc "$age" ans."
