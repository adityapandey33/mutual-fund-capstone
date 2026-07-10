from pathlib import Path
out = Path('output')
# create a simple all-in-one archive listing paths to help the user
bundle = out/'submission_files_list.txt'
text = '\n'.join(sorted([p.name for p in out.iterdir() if p.is_file()]))
bundle.write_text(text)
print(bundle.name)