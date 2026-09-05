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

p.write_text(s, encoding='utf-8')
