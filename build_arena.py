#!/usr/bin/env python3
"""Bundle the 3D arena into one self-contained HTML asset.

three.js and every game module are inlined, so the WebView needs no network at
all — the match runs fully offline (which is the point: Hotspot Wi-Fi only).

The weapon/agent/arena catalog is compiled from the SAME TypeScript file the
React Native side imports, so there is exactly one source of truth.

  python3 tools/build_arena.py
"""
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
GAME = os.path.join(TOOLS, "game")
OUT = os.path.join(ROOT, "assets", "arena.html")

MODULES = [
    "00_core.js",
    "10_arena.js",
    "20_soldier.js",
    "30_combat.js",
    "40_movement.js",
    "50_fx.js",
    "60_hud.js",
    "70_main.js",
]


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def compile_catalog():
    """Compile src/constants/catalog.ts to plain ES2019 JS with the real tsc."""
    src = os.path.join(ROOT, "src", "constants", "catalog.ts")
    work = tempfile.mkdtemp(prefix="catalog-")
    try:
        shutil.copyfile(src, os.path.join(work, "catalog.ts"))
        tsc = os.path.join(ROOT, "node_modules", ".bin", "tsc")
        cmd = [tsc, "catalog.ts", "--ignoreConfig", "--target", "es2019",
               "--module", "es2015", "--outDir", "out", "--skipLibCheck"]
        p = subprocess.run(cmd, cwd=work, capture_output=True, text=True)
        out = os.path.join(work, "out", "catalog.js")
        if p.returncode != 0 or not os.path.isfile(out):
            print("tsc failed:\n" + (p.stdout + p.stderr)[-2000:], file=sys.stderr)
            return None
        js = read(out)
        # the engine is a classic script, not a module: drop the export keywords
        js = js.replace("export const ", "const ").replace("export function ", "function ")
        return "/* ===== catalog (compiled from src/constants/catalog.ts) ===== */\n" + js
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main():
    three_path = os.path.join(ROOT, "node_modules", "three", "build", "three.min.js")
    if not os.path.isfile(three_path):
        print("three.min.js missing — run npm install first", file=sys.stderr)
        return 1
    three = read(three_path)

    data_js = compile_catalog()
    if data_js is None:
        return 1

    parts = [data_js]
    for name in MODULES:
        path = os.path.join(GAME, name)
        if not os.path.isfile(path):
            print(f"missing module {name}", file=sys.stderr)
            return 1
        parts.append(f"/* ===== {name} ===== */\n" + read(path))
    game = "\n\n".join(parts)

    html = read(os.path.join(TOOLS, "arena.src.html"))
    html = html.replace("<!--THREE-->", "<script>\n" + three + "\n</script>")
    html = html.replace("<!--GAME-->", "<script>\n" + game + "\n</script>")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    kb = os.path.getsize(OUT) // 1024
    print(f"wrote {OUT} ({kb} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
