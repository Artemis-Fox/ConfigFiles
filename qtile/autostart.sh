#!/usr/bin/env bash

/usr/lib/xfce-polkit/xfce-polkit &
picom -b --animations --animation-window-mass 0.5 --animation-for-open-window zoom --animation-stiffness 350 &
udiskie &
nitrogen --restore &
dunst &
xrdb ~/.Xresources &
flameshot &
