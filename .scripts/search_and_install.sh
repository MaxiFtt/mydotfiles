#!/bin/bash
sudo pacman -Ss $1 | less && sudo pacman -S $1
