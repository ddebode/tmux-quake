#!/usr/bin/env bash

DEFAULT_QUAKE_KEY="\`"
QUAKE_KEY=$(tmux show-option -gqv @tilde-key)
QUAKE_KEY=${QUAKE_KEY:-$DEFAULT_QUAKE_KEY}

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
tmux bind -n $QUAKE_KEY run-shell "$CURRENT_DIR/quake.py"
