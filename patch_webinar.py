from pathlib import Path

p = Path('webinar_params.tex')
s = p.read_text(encoding='utf-8')

# Example 1: labels directly above the red parameter lines.
marker1 = r'''\node[font=\small\bfseries,text=MCGreen,anchor=west] at (axis cs:6.14,6) {$E$};'''
labels1 = r'''\node[font=\small\bfseries,text=MCGreen,anchor=west] at (axis cs:6.14,6) {$E$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt] at (axis cs:-2.45,.70) {$a=-3$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt] at (axis cs:-2.45,3.70) {$a=0$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt] at (axis cs:-2.45,6.70) {$a=3$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt] at (axis cs:2.20,6.05) {$a=7$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt] at (axis cs:5.25,7.02) {$a=11$};'''
if '$a=-3$};\n\\node[font=\\scriptsize\\bfseries,text=MCRed' not in s:
    s = s.replace(marker1, labels1, 1)

# Example 2: just a little smaller so its answer remains on the same page.
s = s.replace(r'mcaxis,width=.95\textwidth,height=110mm,',
              r'mcaxis,width=.84\textwidth,height=94mm,', 1)

# Example 2: labels directly above the red parameter lines.
marker2 = r'''\node[font=\small\bfseries,text=MCGreen,anchor=east] at (axis cs:.86,3) {$B$};
\node[font=\small\bfseries,text=MCGreen,anchor=east] at (axis cs:.86,7) {$C$};
\node[font=\small\bfseries,anchor=south west] at (axis cs:3.08,5.08) {$A$};'''
labels2 = r'''\node[font=\small\bfseries,text=MCGreen,anchor=east] at (axis cs:.86,3) {$B$};
\node[font=\small\bfseries,text=MCGreen,anchor=east] at (axis cs:.86,7) {$C$};
\node[font=\small\bfseries,anchor=south west] at (axis cs:3.08,5.08) {$A$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt] at (axis cs:-.55,1.82) {$a=-1$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt] at (axis cs:5.45,6.73) {$a=1$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt] at (axis cs:4.45,7.22) {$a=\frac43$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt] at (axis cs:3.35,8.02) {$a=2$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt] at (axis cs:.72,5.70) {$a=6$};'''
if '$a=-1$};\n\\node[font=\\scriptsize\\bfseries,text=MCRed' not in s:
    s = s.replace(marker2, labels2, 1)

# Example 2 final polish: widen only horizontally to the left and move a=-1 into the free area.
s = s.replace(r'  xmin=-1,xmax=7,ymin=-2,ymax=10,',
              r'  xmin=-2.4,xmax=7,ymin=-2,ymax=10,', 1)
s = s.replace(r'  xtick={-1,0,1,2,3,4,5,6,7},',
              r'  xtick={-2,-1,0,1,2,3,4,5,6,7},', 1)
s = s.replace(r'\addplot[MCRed!62,line width=1pt,domain=-1:7] {-x+1};',
              r'\addplot[MCRed!62,line width=1pt,domain=-2.4:7] {-x+1};', 1)
s = s.replace(r'\addplot[MCRed!62,line width=1pt,domain=-1:7] {x+1};',
              r'\addplot[MCRed!62,line width=1pt,domain=-2.4:7] {x+1};', 1)
s = s.replace(r'\addplot[MCRed!62,line width=1pt,domain=-1:7] {4*x/3+1};',
              r'\addplot[MCRed!62,line width=1pt,domain=-2.4:7] {4*x/3+1};', 1)
s = s.replace(r'\addplot[MCRed!62,line width=1pt,domain=-1:4.4] {2*x+1};',
              r'\addplot[MCRed!62,line width=1pt,domain=-2.4:4.4] {2*x+1};', 1)
s = s.replace(r'\addplot[MCRed!62,line width=1pt,domain=-1:1.45] {6*x+1};',
              r'\addplot[MCRed!62,line width=1pt,domain=-1.6:1.45] {6*x+1};', 1)
s = s.replace(r'at (axis cs:-.55,1.82) {$a=-1$};',
              r'at (axis cs:-1.65,2.95) {$a=-1$};', 1)

# Example 3: label every red horizontal parameter level directly on the graph.
marker3 = r'''\node[font=\small\bfseries,anchor=south west] at (axis cs:3.12,6) {$E$};'''
labels3 = r'''\node[font=\small\bfseries,anchor=south west] at (axis cs:3.12,6) {$E$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt,anchor=east] at (axis cs:3.78,-5.65) {$a=-6$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt,anchor=east] at (axis cs:3.78,-1.65) {$a=-2$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt,anchor=east] at (axis cs:3.78,.35) {$a=0$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt,anchor=east] at (axis cs:3.78,2.35) {$a=2$};
\node[font=\scriptsize\bfseries,text=MCRed,fill=white,fill opacity=.9,text opacity=1,inner sep=1.2pt,anchor=east] at (axis cs:3.78,6.35) {$a=6$};'''
if '$a=-6$};\n\\node[font=\\scriptsize\\bfseries,text=MCRed' not in s:
    s = s.replace(marker3, labels3, 1)

# Example 3 final polish: widen to the right, continue the lines horizontally.
s = s.replace(r'  xmin=-4,xmax=4,ymin=-8,ymax=8,',
              r'  xmin=-4,xmax=5.5,ymin=-8,ymax=8,', 1)
s = s.replace(r'  xtick={-4,-3,-2,-1,0,1,2,3,4},',
              r'  xtick={-4,-3,-2,-1,0,1,2,3,4,5},', 1)
s = s.replace('domain=-4:4', 'domain=-4:5.5')
for old_y, new_y in [
    ('3.78,-5.65', '4.75,-5.65'),
    ('3.78,-1.65', '4.75,-1.65'),
    ('3.78,.35',   '4.75,.35'),
    ('3.78,2.35',  '4.75,2.35'),
    ('3.78,6.35',  '4.75,6.35'),
]:
    s = s.replace(f'at (axis cs:{old_y})', f'at (axis cs:{new_y})', 1)

# Example 3 final label placement: put all red parameter values at the left edge.
for y in ('-5.65', '-1.65', '.35', '2.35', '6.35'):
    s = s.replace(
        f'anchor=east] at (axis cs:4.75,{y})',
        f'anchor=west] at (axis cs:-3.72,{y})',
        1,
    )

p.write_text(s, encoding='utf-8')
