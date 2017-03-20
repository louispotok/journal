import os
import sys

entry_directory = os.path.expanduser("~/Dropbox/journal/entries")
files = os.listdir(entry_directory)
entries = [int(f.split('.')[0]) for f in files if f.endswith('.journal')]

# the bash script actually does the right thing if there are no entries,
# this is just to avoid a noisy error
if entries:
    latest_idx = max(entries)
    sys.stdout.write(str(latest_idx))
