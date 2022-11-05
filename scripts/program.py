#!/usr/bin/python3

import pandas as pd
import sys

csv = sys.argv[1]
df = pd.read_csv(csv)

lines = []
for i, row in df.iterrows():
    lines += ['<p>']
    lines += ['<b>%s</b><br />' % row['Time']]
    lines += ['<b>%s</b><br />' % row['Title']]
    lines += ['<i>%s</i><br />' % row['Authors']]
    lines += ['<div class="buttons">']
    lines += ['<a class="button is-primary" href="" disabled>']
    lines += ['<span class="icon is-small">']
    lines += ['<i class="fas fa-file-alt"></i>']
    lines += ['</span>']
    lines += ['<span>Paper</span>']
    lines += ['</a>']
    lines += ['<a class="button is-primary" href="%s">' % row['Session']]
    lines += ['<span class="icon is-small">']
    lines += ['<i class="fas fa-chalkboard-teacher"></i>']
    lines += ['</span>']
    lines += ['<span>Session</span>']
    lines += ['</a>']
    lines += ['</div>']
    lines += ['</p>']
    lines += ['\n']
    lines += ['<hr>']
    lines += ['\n']
print('\n'.join(lines))

