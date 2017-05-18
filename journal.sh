#!/bin/bash

# from http://stackoverflow.com/a/246128/3393459 
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

latest=$(python $DIR/journal.py)
new_idx=$((latest+1))
new_filepath="$DIR/entries/$new_idx.journal"
echo "writing to $new_filepath"
vi $new_filepath
