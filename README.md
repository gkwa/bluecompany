# bluecompany

## Purpose

Learn how to use [[mistletoe]] to parse [[Obsidian]] markdown links with the intention of deduping links.


## Usage




```bash
# Show help:
bluecompany 
bluecompany --help

# Get 10 random paths and fetch links from all into list of dicts
rg --files --glob='*.md' ~/Documents/Obsidian\ Vault | sort -R | head -10 | bluecompany
bluecompany "$(rg --files --glob='*.md' ~/Documents/Obsidian\ Vault | sort -R | head -10)"
```


