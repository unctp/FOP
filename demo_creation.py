# this script creates demo files for testing functionality.
import os
import random
import string
from pathlib import Path


def random_text(length=80):
    return ''.join(random.choice(string.ascii_letters + string.digits + ' _-') for _ in range(length))


def make_demo_file(path: str, size: int = 10):
    lines = []
    for _ in range(size):
        lines.append(random_text(random.randint(20, 80)))
    Path(path).write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    base_dir = Path(__file__).resolve().parent
    demo_dir = base_dir / 'demo_files'
    demo_dir.mkdir(exist_ok=True)

    for i in range(random.randint(3, 8)):
        filename = f'demo_{i + 1}_{random.randint(1000, 9999)}.txt'
        make_demo_file(demo_dir / filename, random.randint(5, 15))

    print(f'created demo files in {demo_dir}')


if __name__ == '__main__':
    main()
