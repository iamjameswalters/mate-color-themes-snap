#!/usr/bin/env python3
import os, shutil

theme_colors = ("aqua", "blue", "brown", "orange", "pink", "purple", "red", "teal", "yellow")

os.mkdir("Theme Snaps")

for color in theme_colors:
    snap_name = "mate-themes-" + color
    os.mkdir("Theme Snaps/" + snap_name)
    os.mkdir("Theme Snaps/" + snap_name + "/snap")
    os.mkdir("Theme Snaps/" + snap_name + "/utils")
    shutil.copy("utils/split-gtk-theme.sh", "Theme Snaps/" + snap_name + "/utils")
    with open("yaml_template.txt", "r") as generic_template:
        with open("Theme Snaps/" + snap_name + "/snap/snapcraft.yaml", "w") as new_yaml:
            color_capitalized = color.capitalize()
            template = generic_template.read()
            formatted_template = template.format(color=color, color_capital=color_capitalized)
            new_yaml.write(formatted_template)
