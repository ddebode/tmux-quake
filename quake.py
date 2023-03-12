#!/usr/bin/env python3

import os
from typing import List

class TmuxPane:
    title: str
    index: int
    active: int
    def __init__(self, title, index, active):
        self.title = title
        self.index = index
        self.active = active

def get_panes():
    ret = []
    panes = os.popen("tmux list-panes -F \"#{pane_title}:#{pane_index}:#{pane_active}\"")
    while panes:
        myline = panes.readline()
        if myline == "":
            break
        titleAndIndex = myline.strip().split(":")
        tmuxPane = TmuxPane(titleAndIndex[0], titleAndIndex[1], titleAndIndex[2])
        ret.append(tmuxPane);
    panes.close()
    return ret;

def create_quake_pane():
    os.system("tmux splitw -l 30% -c \"#{pane_current_path}\"")
    os.system("tmux select-pane -T tilde-pane")

def get_tilde_pane(tmuxPanes: List[TmuxPane]):
    for tmuxPane in tmuxPanes:
        if("tilde-pane" in tmuxPane.title):
            return tmuxPane
    return None

def kill_pane(index):
    command = "tmux kill-pane -t " + str(index)
    os.system(command)


tmuxPanes = get_panes()
tildePane = get_tilde_pane(tmuxPanes)
if(tildePane != None):
    kill_pane(tildePane.index)
else:
    create_quake_pane()
