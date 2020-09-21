Very minimal personal journaling system.

The entries/ directory is used to store files that look like:
    1.journal
    2.journal
    etc

Running "bash journal.sh" will:
* find the highest-numbered entry in the entries/ folder
* open vim in a new entry with a new highest number

You will need to make journal.py executable, like:

`chmod +x journal.py`

Also I recommend aliasing, eg add the following line to your ~/.bashrc file:

`alias journal="bash /path/to/here/journal.sh"`

---
Update: I now prefer a system where each date has its own journal entry. What I use now is a simple function in my .bashrc instead:

```
# journal program
function journal() {
	JOURNAL_DIR="/path/to/journal"
	if test "$1" == "list"
	then
		echo "navigating to journal entries"
		cd $JOURNAL_DIR/
	else
		vi $JOURNAL_DIR/$(date +'%Y-%m-%d').md
	fi
}
```
