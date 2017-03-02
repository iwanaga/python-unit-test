#!/bin/bash

watchmedo shell-command \
    -W \
    --patterns="*.py;*.txt" \
    --recursive \
    --ignore-directories \
    --command="./bin/run_spec.sh" \
    .
