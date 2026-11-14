#!/usr/bin/env python3
"""Bundle css + js into one self-contained dist/index.html."""
import re,pathlib
r=pathlib.Path(__file__).parent;h=(r/'index.html').read_text()
h=h.replace('<link rel="stylesheet" href="css/style.css">','<style>'+(r/'css/style.css').read_text()+'</style>')
h=re.sub(r'(<script src="js/\w+\.js"></script>)+',lambda m:'<script>'+''.join((r/p).read_text()+'\n' for p in re.findall(r'src="(js/\w+\.js)"',m.group(0)))+'</script>',h)
(r/'dist').mkdir(exist_ok=True);(r/'dist/index.html').write_text(h);print('built dist/index.html',len(h),'bytes')
