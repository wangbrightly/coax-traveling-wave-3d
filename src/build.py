# 把 three.min.js 和 OrbitControls.js 内嵌进 HTML，产出可离线双击打开的单文件
import sys, pathlib
src, three, orbit, out = map(pathlib.Path, sys.argv[1:5])
s = src.read_text(encoding='utf-8')
s = s.replace('/*__THREE__*/', three.read_text(encoding='utf-8')).replace('/*__ORBIT__*/', orbit.read_text(encoding='utf-8'))
out.write_text(s, encoding='utf-8'); print(out, out.stat().st_size, 'bytes')
