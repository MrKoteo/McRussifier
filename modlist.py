import os, subprocess

def copy(txt: str):
    subprocess.run(["clip"],input=str(txt),text=True,check=True,shell=True,)

dirs = [entry.name for entry in os.scandir('assets') if entry.is_dir()]
print(len(dirs))
res = ' | '.join(sorted(dirs))
print(res)
copy(res)
print('\nСкопировано в буфер обмена!')

