import os

dirs = [entry.name for entry in os.scandir('assets') if entry.is_dir()]
print(' | '.join(sorted(dirs)))

