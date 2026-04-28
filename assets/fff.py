# list_dirs_csv.py — выводит имена папок в текущей директории, разделённые запятыми
import os

dirs = [entry.name for entry in os.scandir('.') if entry.is_dir()]
print(' | '.join(sorted(dirs)))
