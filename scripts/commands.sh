#!/bin/sh

# The shell will terminate script execution when a command fails
set -e

if [ "$RUN_MAIN" != "true" ]; then
    wait_psql.sh
    collectstatic.sh
    migrate.sh

fi 

runserver.sh