#!/usr/bin/env bash

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
picom -b --animations-window-mass 0.5 --animation-for-open-window zoom --animation-stiffness 350 &
udiskie & 
nitrogen --restore &
xrdb ~/.Xresources &
flameshot &
