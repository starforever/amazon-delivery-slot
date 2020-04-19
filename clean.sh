#!/usr/bin/env zsh

black ${@}
isort ${@}
autoflake --in-place --remove-all-unused-imports --remove-unused-variables ${@}
