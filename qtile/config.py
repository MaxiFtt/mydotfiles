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

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()
#scrot
scrot_path="~/Photos/scrot/"
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f",lazy.window.toggle_fullscreen(),desc='toggle fullscreen'),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #custom commands
    Key([mod], "r",lazy.spawn("rofi -show drun"),desc="rofi shows .desktop files"),
    Key([mod, "control"], "x", lazy.spawn("shutdown now"), desc="Shutdown computer"),
    Key([mod, "control"], "z", lazy.spawn("slock"), desc="lock computer"),
    Key([mod], "b", lazy.spawn("brave"), desc="browser"),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s /home/maxif/Photos/scrot/'%Y-%m-%d_$wx$h.jpg'")),
    Key([mod, "shift"], "p", lazy.spawn("scrot /home/maxif/Photos/scrot/'%Y-%m-%d_$wx$h.jpg'")),
]
colors = [["#312d3f", "#312d3f"], # panel background
          ["#c68e7c", "#c68e7c"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#f55f5f", "#f55f5f"], # border line color for current tab f55f5f 
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7","#4f76c7"], # color for the 'even widgets'
          ["#e1acff","#e1acff"], # window name
          ["#D6573C","#B54D36"]] # border for screens

from libqtile.config import Group, Match
groups = [Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns'),
          Group("",layout="columns"),
          Group("",layout="columns"),
          Group("",layout="columns"),
          Group("",layout="max"),]
                                 
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

main_theme = {
    "b_width": 4,
    "margin": 4,
    "background": "/home/maxif/.config/backgrounds/water_huts.jpeg",
    "bar_height": 28,
    "font_size" : 14,
}
layouts = [
    layout.Columns(border_focus="#D6573C", border_normal="#7a4a24", border_width= main_theme["b_width"],margin= main_theme["margin"]),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    #layout.Matrix(border_focus="#D6573C", border_normal="#7a4a24",columns=2,border_width=4,margin=4),
    #layout.MonadTall(),
    # layout.MonadWide(),
    layout.RatioTile(border_focus="#903bd6",border_normal="#5d247a",border_width= main_theme["b_width"],margin= main_theme["margin"]),
    # layout.Tile(),
    # layout.TreeTab(
    #     border_focus="#D6573C",
    #     border_normal="#7a4a24",
    #     active_bg="#c68e7c" ,
    #     bg_color="#312d3f" ,
    #    margin=4),
    layout.VerticalTile(border_focus="#90d63b", border_normal="#3f701f",border_width= main_theme["b_width"],margin= main_theme["margin"]),
    # layout.Zoomy(),
]



widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper= main_theme["background"],
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.GroupBox(
                    background = colors[0],
                    foreground = colors[2],
                    fontsize = main_theme["font_size"],
                    block_highlight_text_color= colors[0],
                    highlight_method = "line",
                    this_current_screen_border = colors[1],
                    highlight_color = colors[1],
                    inactive= colors[1]),
                widget.Prompt(
                    background=colors[3],
                    fontsize = main_theme["font_size"]),
                widget.WindowName(
                    background=colors[0],
                    fontsize=main_theme["font_size"]),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                       text='',
                       background = colors[0],
                       foreground = "#f9bc02",
                       padding = 0,
                       fontsize = 57
                       ),
                widget.CryptoTicker(background = "#f9bc02",
                                    foreground=colors[0],
                                    fontsize=main_theme["font_size"],
                                    format=" : {symbol}{amount:.2f}",
                                    update_interval = 1800),
                widget.TextBox(
                       text='',
                       background = "#f9bc02",
                       foreground = "#0484ce",
                       padding = 0,
                       fontsize = 57
                       ),
                widget.CurrentLayout(background = "#0484ce",fontsize=main_theme["font_size"],foreground=colors[0]),
                widget.TextBox(
                       text='',
                       background = "#0484ce",
                       foreground = "d84404",
                       padding = 0,
                       fontsize = 57
                       ),
                widget.CPU(background = "d84404",
                           foreground=colors[0],
                           fontsize=main_theme["font_size"],
                           format=" {freq_current}GHz {load_percent}%"),
                widget.TextBox(
                       text='',
                       background = "d84404",
                       foreground = "#add802",
                       padding = 0,
                       fontsize = 57
                       ),
                widget.Battery(background= "#add802",fontsize=main_theme["font_size"],
                               foreground=colors[0],
                               charge_char="",
                               discharge_char="",
                               unknown_char=""),
                widget.TextBox(
                       text='',
                       background = "#add802",
                       foreground = "#0ad39a",
                       padding = 0,
                       fontsize = 57
                       ),
                widget.CheckUpdates(
                    background= "#0ad39a",
                    update_interval= 1800,
                    fontsize=main_theme["font_size"],
                    distro="Arch_checkupdates",
                    colour_have_updates=colors[0],
                    colour_no_updates=colors[0],
                    no_update_string="UP TO DATE"),
                widget.TextBox(
                       text='',
                       background = "#0ad39a",
                       foreground = "#2caa30",
                       padding = 0,
                       fontsize = 57
                       ),
                widget.Clock(format=' %d/%m/%Y %a %I:%M %p',fontsize=main_theme["font_size"],background = "#2caa30",foreground=colors[0]),
            ],
            main_theme["bar_height"],
            margin= main_theme["margin"],
            opacity = 1 
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
