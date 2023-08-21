# PyDirCrawler

Tool for crawling passed directory recursively, printing to console files contents.

## Usage

Print content of every file:
```console
python main.py <path-to-dir-to-crawl> no-excludes
```

Print content of every file except some files or dirs:
```console
python main.py <path-to-dir-to-crawl> <excluded-file-1> <excluded-file-2> ...
```

Print content of every file except: .idea, venv, .gitignore, .ignore, .env, .env.passwords, \_\_pycache__, \_\_init__.py, output.txt, README.md, .git:
```console
python main.py <path-to-dir-to-crawl> 
```

Print content of every file except mentioned above and append your own:
```console
python main.py <path-to-dir-to-crawl> ext-excludes <excluded-file-1> <excluded-file-2> ...
```