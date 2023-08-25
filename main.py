from sys import argv
from pathlib import Path

DEFAULT_EXCLUDES = [
    '.idea', 'venv', '.gitignore', '.ignore', '.env', '.env.passwords', '__pycache__', '__init__.py', 'output.txt',
    'README.md', '.git'
]


def parse_arguments() -> tuple[str | None, list[str] | None]:
    args_len = len(argv)
    if args_len == 1:
        return None, None
    if args_len > 3:
        if argv[2] == 'no-excludes':
            return argv[1], None
        if argv[2] == 'ext-excludes':
            return argv[1], argv[3:] + DEFAULT_EXCLUDES
        else:
            return argv[1], argv[2:]
    return argv[1], DEFAULT_EXCLUDES


def crawl_dir(cur_dir_path: Path, excludes: list[str] = None) -> None:
    for dir_elem in cur_dir_path.iterdir():
        if excludes and dir_elem.name in excludes:
            continue
        if dir_elem.is_dir():
            crawl_dir(dir_elem, excludes)
        elif dir_elem.is_file():
            print_content(dir_elem)


def print_content(file_path: Path) -> None:
    with open(file_path) as file:
        try:
            content = file.read()
            if content:
                print(f'# {file.name}\n{content}\n')
        except UnicodeDecodeError:
            return


def main() -> None:
    crawling_dir, excludes = parse_arguments()
    if not crawling_dir:
        print('No crawling directory')
        return
    if not excludes:
        print('No excludes\n')
    crawl_dir(Path(crawling_dir), excludes)


if __name__ == '__main__':
    main()
