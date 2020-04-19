#!/usr/bin/env zsh

black ${@}

autoflake \
  --in-place \
  --remove-all-unused-imports \
  --remove-unused-variables \
  ${@}

isort ${@}
