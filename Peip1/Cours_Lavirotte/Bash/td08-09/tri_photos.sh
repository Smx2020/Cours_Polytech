#!/bin/bash

mkdir $2

for file in $(ls $1/*)
do
	temp=$(exif -t"0x0132" $file  | grep "Value" | cut -c10-)
	ymd=$(echo $temp | cut -d' ' -f1 | tr ":" "-")
	hour=$(echo $temp | cut -d' ' -f2 | tr ":" "-")
	anne=$(echo $ymd | cut -d'-' -f1 )

	mkdir -p $2/$anne
	filename=$ymd"_"$hour".jpg"

	cp $file $2/$anne/$filename
done
