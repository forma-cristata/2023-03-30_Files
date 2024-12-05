from pathlib import Path

path = Path('guest.txt')
all_names = path.read_text().splitlines()

for name in all_names:
    print(name)
    