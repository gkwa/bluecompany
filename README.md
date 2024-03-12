# bluecompany

## Purpose

Learn how to use [[mistletoe]] to parse [[Obsidian]] markdown links with the intention of deduping links.


## Usage


```bash
# install
pip install git+https://github.com/taylormonacelli/bluecompany

# Show help:
bluecompany 
bluecompany --help

# Set basedir:
bluecompany config dir ~/Documents/Obsidian\ Vault

# Show config:
bluecompany config

# Process markdown files:
bluecompany process --include=.md
bluecompany process --include=.md --exclude=.obsidian

# months later when you've forgotten everything:
z bluecompany
. .venv/bin/activate
bluecompany process --include=.md --exclude=.obsidian >/tmp/data.json
less -RSi /tmp/data.json
```
