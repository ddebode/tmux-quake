#!/usr/bin/env bash

DEFAULT_TILDE_KEY="\`"
TILDE_KEY=$(tmux show-option -gqv @tilde-key)
TILDE_KEY=${TILDE_KEY:-$DEFAULT_TILDE_KEY}

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
tmux bind -n $TILDE_KEY run-shell "$CURRENT_DIR/tilde.py"
