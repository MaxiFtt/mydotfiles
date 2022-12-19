#!/usr/bin/env bash

if [ x"$@" = x"scrot" ]
then
	cd ~/Photos/scrot/;
	scrot -s;
	exit 0
fi
echo "scrot"
