import sys, os

if not os.path.isdir(f"{sys.argv[2]}"): os.mkdir(f"{sys.argv[2]}")
files = os.listdir(sys.argv[1])

for file in files:
    if not " - " in file: continue
    if file.count(' - ') > 1: continue
    artist, filename = file.split(" - ")
    if not os.path.isdir(f"{sys.argv[2]}{artist}"): os.mkdir(f"{sys.argv[2]}{artist}")
    if not os.path.isfile(f"{sys.argv[2]}{artist}/{filename}"): os.symlink(f"{sys.argv[1]}{file}", f"{sys.argv[2]}{artist}/{filename}")