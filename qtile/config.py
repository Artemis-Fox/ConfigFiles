# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import subprocess
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import hook

mod = "mod4"
terminal = "kitty"
browser = "firefox"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])



keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # use comma and period to switch windows
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to previous screen"),
    Key([mod], "period", lazy.next_screen(), desc="Move Focus to next screen"),
    # Hot keys to launch apps
    Key([mod], "b", lazy.spawn(browser), desc="Spawns Firefox browser"),
    Key([mod], "f", lazy.spawn("nemo"), desc="spawns the nemo file manager"),
    Key(["control", "shift"], "f", lazy.spawn("joshuto"), desc="spawns the joshuto terminal file manager"),
    Key(["control", "shift"], "e", lazy.spawn("emacs"), desc="launches Emacs"),
    Key(["control", "shift"], "g", lazy.spawn("godot"), desc="launches the godot engine"),
    Key(["control", "shift"], "k", lazy.spawn("kdenlive"), desc="launches kdenlive"),
    Key([mod, "shift"],  "g", lazy.spawn("gimp"), desc="launches gimp"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "Return", lazy.spawn("rofi -show drun"), desc="Launches Rofi"),
]

groups = [Group(i) for i in ["爵", "", "", "", "ﳜ", "", "露", "", "壘"]]
group_hotkeys = "123456789"

for g, k in zip(groups, group_hotkeys):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                k,
                lazy.group[g.name].toscreen(),
                desc="Switch to group {g.name}",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                k,
                lazy.window.togroup(g.name, switch_group=False),
                desc="Switch to & move focused window to group {g.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


# colors
catppuccin ={
    "flamingo": "#F2CDCD",
    "mauve": "#DDB6F2",
    "pink": "#F5C2E7",
    "maroon": "#E8A2AF",
    "red": "#F28FAD",
    "peach": "#F8BD96",
    "yellow": "#FAE3B0",
    "green": "#ABE9B3",
    "teal": "#B5E8E0",
    "blue": "#96CDFB",
    "sky": "#89DCEB",
    "black": "#1E1E2E",
    "gray": "#6E6C7E",
    "white": "#D9E0EE",
    "lavender": "#C9CBFF",
    "rosewater": "#F5E0DC",
}

def layout_default():
    return{"margin": 20,
           "border_width": 3,
           "border_focus": catppuccin["red"],
           "border_normal": catppuccin["gray"]
           }

lt = layout_default()

layouts = [
    layout.MonadTall(**lt),
    layout.MonadWide(**lt),
    layout.TreeTab(**lt),
    layout.Max(**lt),
    layout.Floating(**lt),
    # layout.Bsp(**lt),
    # layout.Matrix(**lt),
    # layout.Tile(**lt),
]

widget_defaults = dict(
    font="Jetbrains Mono",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=10),
                widget.GroupBox(
                    fontsize=22,
                    active = catppuccin["peach"],
                    highlight_method='text',
                    this_current_screen_border=catppuccin["green"],
                    inactive=catppuccin["gray"],
                ),
                widget.Spacer(length=5),
                widget.TextBox("|"),
                widget.CurrentLayoutIcon(scale=0.8, foreground=catppuccin["white"]),
                widget.CurrentLayout(),
                widget.TextBox("|"),
                widget.WindowName(foreground=catppuccin["red"]),
                widget.Memory(measure_mem="G", format=('{MemUsed: .0f}{mm}/{MemTotal:.0f}{mm}')),
                widget.TextBox("|"),
                widget.TextBox("", fontsize="25", foreground=catppuccin["yellow"]),
                widget.Clock(format="%d/%m/%y %I:%M"),
                widget.TextBox("|"),
                widget.Systray(),
                widget.Spacer(length=10),

            ],
            24, opacity=0.7, background=catppuccin["black"],
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=10),
                widget.GroupBox(
                    fontsize=20,
                    active = catppuccin["peach"],
                    highlight_method='text',
                    this_current_screen_border=catppuccin["green"],
                    inactive=catppuccin["gray"],

                ),
                widget.TextBox("|"),
                widget.WindowName(foreground=catppuccin["red"]),
                widget.TextBox("", fontsize="25", foreground=catppuccin["yellow"]),
                widget.Clock(format="%d/%m/%y %I:%M"),
                widget.Spacer(length=10),

            ],
            24, opacity=0.7, background=catppuccin["black"],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
