from pathlib_mate import Path


root = Path(__file__).parent

for p in root.select_file():
    print(p)
    p.moveto(new_basename=p.basename.replace(" ", ""))
