#!/usr/bin/env python3
"""Generates the animated SVG cards used by README.md (no third-party services)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
W = 860
FONT = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"
BG, PANEL, BORDER = "#0d1117", "#161b22", "#30363d"
TEXT, DIM = "#c9d1d9", "#8b949e"
GREEN, CYAN, PINK, YELLOW, BLUE, ORANGE = "#3fb950", "#39d0d8", "#f778ba", "#e3b341", "#79c0ff", "#ffa657"


def frame(h, title, body, style=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{title}">
<style>
text{{font-family:{FONT};}}
{style}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;opacity:1!important}}}}
</style>
<clipPath id="win"><rect width="{W}" height="{h}" rx="12"/></clipPath>
<g clip-path="url(#win)">
<rect width="{W}" height="{h}" fill="{BG}"/>
<rect width="{W}" height="36" fill="{PANEL}"/>
<circle cx="22" cy="18" r="6" fill="#ff5f57"/><circle cx="42" cy="18" r="6" fill="#febc2e"/><circle cx="62" cy="18" r="6" fill="#28c840"/>
<text x="{W/2}" y="23" font-size="13" fill="{DIM}" text-anchor="middle">{title}</text>
{body}
</g>
<rect x=".5" y=".5" width="{W-1}" height="{h-1}" rx="12" fill="none" stroke="{BORDER}"/>
</svg>
"""


def hero():
    h = 290
    elf = [
        "7f 45 4c 46 02 01 01 00  00 00 00 00 00 00 00 00  |.ELF............|",
        "03 00 3e 00 01 00 00 00  60 10 00 00 00 00 00 00  |..>.....`.......|",
        "40 00 00 00 00 00 00 00  30 78 49 44 41 00 00 00  |@.......0xIDA...|",
        "00 00 00 00 40 00 38 00  0d 00 40 00 1f 00 1e 00  |....@.8...@.....|",
        "06 00 00 00 04 00 00 00  40 00 00 00 00 00 00 00  |........@.......|",
        "62 69 6e 61 72 79 70 69  6c 6f 74 00 70 77 6e 00  |binarypilot.pwn.|",
        "2f 6c 69 62 36 34 2f 6c  64 2d 6c 69 6e 75 78 2d  |/lib64/ld-linux-|",
        "78 38 36 2d 36 34 2e 73  6f 2e 32 00 66 6c 61 67  |x86-64.so.2.flag|",
        "48 54 42 7b 2e 2e 2e 7d  00 47 4e 55 00 00 00 00  |HTB{...}.GNU....|",
    ]
    rows = "".join(
        f'<text x="94" y="{62 + i * 24}" font-size="14" textLength="672" xml:space="preserve">{i * 16:08x}  {r.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")}</text>'
        for i, r in enumerate(elf)
    )
    tag = "&gt; building autonomous agents that pwn CTFs · shipping in public"
    tw, tx = 558, 151
    style = f"""
.hex{{fill:{GREEN};opacity:.13}}
.scan{{animation:scan 6s linear infinite}}
@keyframes scan{{from{{transform:translateY(36px)}}to{{transform:translateY({h}px)}}}}
.t{{font-size:96px;font-weight:800;letter-spacing:6px}}
.g1{{fill:{CYAN};animation:g1 4s steps(1) infinite}}
.g2{{fill:{PINK};animation:g2 4s steps(1) infinite}}
@keyframes g1{{0%,100%{{transform:translate(0,0);opacity:0}}6%{{transform:translate(-5px,2px);opacity:.9}}9%{{transform:translate(4px,-1px);opacity:.9}}12%{{opacity:0}}54%{{transform:translate(-3px,0);opacity:.8}}57%{{opacity:0}}}}
@keyframes g2{{0%,100%{{transform:translate(0,0);opacity:0}}6%{{transform:translate(5px,-2px);opacity:.9}}9%{{transform:translate(-4px,1px);opacity:.9}}12%{{opacity:0}}54%{{transform:translate(3px,1px);opacity:.8}}57%{{opacity:0}}}}
.dot{{animation:pulse 1.6s ease-in-out infinite}}
@keyframes pulse{{50%{{opacity:.25}}}}
.cur{{animation:blink 1s steps(1) infinite}}
@keyframes blink{{50%{{opacity:0}}}}
"""
    body = f"""
<g class="hex">{rows}</g>
<rect class="scan" width="{W}" height="2" fill="{GREEN}" opacity=".25"/>
<radialGradient id="glow"><stop offset="0" stop-color="{BG}" stop-opacity=".95"/><stop offset="1" stop-color="{BG}" stop-opacity="0"/></radialGradient>
<ellipse cx="430" cy="150" rx="330" ry="105" fill="url(#glow)"/>
<g text-anchor="middle">
<text class="t g1" x="430" y="172">0xIDA</text>
<text class="t g2" x="430" y="172">0xIDA</text>
<text class="t" x="430" y="172"><tspan fill="{GREEN}">0x</tspan><tspan fill="#f0f6fc">IDA</tspan></text>
</g>
<clipPath id="type"><rect x="{tx}" y="196" height="26" width="0"><animate attributeName="width" from="0" to="{tw}" dur="3.2s" begin="0.4s" fill="freeze"/></rect></clipPath>
<text x="{tx}" y="214" font-size="15" fill="{TEXT}" textLength="{tw}" clip-path="url(#type)">{tag}</text>
<rect class="cur" x="{tx}" y="200" width="9" height="18" fill="{GREEN}"><animate attributeName="x" from="{tx}" to="{tx + tw + 4}" dur="3.2s" begin="0.4s" fill="freeze"/></rect>
<circle class="dot" cx="28" cy="{h - 22}" r="5" fill="{GREEN}"/>
<text x="42" y="{h - 17}" font-size="13" fill="{GREEN}">online</text>
<text x="{W - 20}" y="{h - 17}" font-size="13" fill="{DIM}" text-anchor="end">0xida: ELF 64-bit LSB pie executable, not stripped</text>
"""
    return frame(h, "0xida@github: ~", body, style)


def disasm():
    A, M, O, C = 24, 262, 336, 566  # column x positions
    lines = [
        (None, [("c", A, "; =============== S U B R O U T I N E ===============")]),
        (None, [("c", A, "; Attributes: noreturn, ships-in-public")]),
        (0x401000, [("n", M - 62, "whoami"), ("k", M + 10, "proc near")]),
        (0x401000, [("m", M, "push"), ("o", O, "rbp")]),
        (0x401001, [("m", M, "mov"), ("o", O, "rbp, rsp")]),
        (0x401004, [("m", M, "lea"), ("o", O, "rdi, aName"), ("s", C, '; "IDA"')]),
        (0x40100B, [("m", M, "lea"), ("o", O, "rsi, aFocus"), ("s", C, '; "autonomous CTF agents"')]),
        (0x401012, [("m", M, "lea"), ("o", O, "rdx, aStack"), ("s", C, '; "Python, TypeScript, Go, C"')]),
        (0x401019, [("m", M, "lea"), ("o", O, "rcx, aArena"), ("s", C, '; "HackTheBox, FlagYard"')]),
        (0x401020, [("j", M, "call"), ("n", O, "build_learn_ship")]),
        (0x401025, [("j", M, "jmp"), ("n", O, "short whoami"), ("c", C, "; never returns")]),
        (0x401027, [("n", M - 62, "whoami"), ("k", M + 10, "endp")]),
    ]
    col = {"c": DIM, "n": BLUE, "k": PINK, "m": TEXT, "o": ORANGE, "s": GREEN, "j": YELLOW}
    out = []
    for i, (addr, parts) in enumerate(lines):
        y = 66 + i * 23
        seg = ""
        if addr is not None:
            seg += f'<text x="{A}" y="{y}" fill="{DIM}">.text:{addr:08X}</text>'
        for kind, x, txt in parts:
            txt = txt.replace("&", "&amp;").replace('"', "&quot;")
            seg += f'<text x="{x}" y="{y}" fill="{col[kind]}">{txt}</text>'
        out.append(f'<g class="l" style="animation-delay:{0.25 + i * 0.22:.2f}s">{seg}</g>')
    h = 66 + len(lines) * 23 + 6
    ipy = 66 + 9 * 23 - 16
    style = f"""
text{{font-size:14px}}
.l{{opacity:0;animation:in .35s ease-out forwards}}
@keyframes in{{from{{opacity:0;transform:translateX(-8px)}}to{{opacity:1;transform:none}}}}
.ip{{opacity:0;animation:ip 1.4s ease-in-out 3.2s infinite}}
@keyframes ip{{0%,100%{{opacity:.08}}50%{{opacity:.22}}}}
"""
    body = f'<rect class="ip" x="0" y="{ipy}" width="{W}" height="22" fill="{YELLOW}"/>' + "".join(out)
    return frame(h, "IDA View-A — whoami", body, style)


def project():
    h = 250
    stages = [("recon", CYAN), ("analyze", BLUE), ("exploit", PINK), ("flag", GREEN)]
    x0, gap, bw, y = 70, 190, 150, 150
    nodes, path = "", ""
    for i, (name, c) in enumerate(stages):
        x = x0 + i * gap
        nodes += (
            f'<rect x="{x}" y="{y}" width="{bw}" height="40" rx="8" fill="{PANEL}" stroke="{c}" class="n" style="animation-delay:{i * 0.9:.1f}s"/>'
            f'<text x="{x + bw / 2}" y="{y + 25}" font-size="14" fill="{c}" text-anchor="middle">{name}</text>'
        )
        if i < len(stages) - 1:
            path += f'<line x1="{x + bw}" y1="{y + 20}" x2="{x + gap}" y2="{y + 20}" stroke="{BORDER}" stroke-width="2" stroke-dasharray="4 5" class="d"/>'
    x_end = x0 + 3 * gap + bw / 2
    style = f"""
.n{{animation:lit 3.6s ease-in-out infinite}}
@keyframes lit{{0%,30%,100%{{stroke-width:1;fill:{PANEL}}}12%{{stroke-width:2.5;fill:#1f2733}}}}
.d{{animation:dash 1s linear infinite}}
@keyframes dash{{to{{stroke-dashoffset:-9}}}}
.fl{{animation:fl 3.6s steps(1) infinite}}
@keyframes fl{{0%,74%{{opacity:.25}}75%,100%{{opacity:1}}}}
"""
    body = f"""
<text x="28" y="76" font-size="26" font-weight="800" fill="#f0f6fc">binarypilot</text>
<rect x="222" y="57" width="74" height="24" rx="12" fill="none" stroke="{BLUE}"/><text x="259" y="74" font-size="12" fill="{BLUE}" text-anchor="middle">Python</text>
<rect x="306" y="57" width="98" height="24" rx="12" fill="none" stroke="{GREEN}"/><text x="355" y="74" font-size="12" fill="{GREEN}" text-anchor="middle">HackTheBox</text>
<rect x="414" y="57" width="84" height="24" rx="12" fill="none" stroke="{YELLOW}"/><text x="456" y="74" font-size="12" fill="{YELLOW}" text-anchor="middle">FlagYard</text>
<text x="{W - 28}" y="74" font-size="13" fill="{DIM}" text-anchor="end">open →</text>
<text x="28" y="110" font-size="15" fill="{TEXT}">Autonomous CTF solver — agent-based, built for HackTheBox + FlagYard.</text>
{path}{nodes}
<circle r="5" fill="#f0f6fc"><animate attributeName="cx" values="{x0 + bw / 2};{x_end}" dur="3.6s" repeatCount="indefinite"/><animate attributeName="cy" values="{y - 10};{y - 10}" dur="3.6s" repeatCount="indefinite"/></circle>
<text x="28" y="{h - 20}" font-size="13" fill="{DIM}">[agent] loop until solved</text>
<text class="fl" x="{W - 28}" y="{h - 20}" font-size="13" fill="{GREEN}" text-anchor="end">[+] flag captured</text>
"""
    return frame(h, "~/projects/binarypilot", body, style)


def stack():
    h = 150
    langs = [("Python", 71, "#3572A5"), ("TypeScript", 13, "#3178c6"), ("Go", 6, "#00ADD8"),
             ("C", 3, "#8b949e"), ("Jinja", 2, "#a52a22"), ("JavaScript", 2, "#f1e05a"), ("other", 3, BORDER)]
    bx, bw, x = 28, W - 56, 28
    segs, legend, lx = "", "", 28
    for name, pct, c in langs:
        w = bw * pct / 100
        segs += f'<rect x="{x:.1f}" y="62" width="{w:.1f}" height="18" fill="{c}"/>'
        x += w
        if name != "other":
            legend += f'<circle cx="{lx + 5}" cy="113" r="5" fill="{c}"/><text x="{lx + 16}" y="118" font-size="13" fill="{TEXT}">{name} <tspan fill="{DIM}">{pct}%</tspan></text>'
            lx += 16 + (len(name) + 5) * 8 + 22
    body = f"""
<clipPath id="bar"><rect x="{bx}" y="62" height="18" rx="9" width="0"><animate attributeName="width" from="0" to="{bw}" dur="1.6s" begin="0.3s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1" keyTimes="0;1"/></rect></clipPath>
<rect x="{bx}" y="62" width="{bw}" height="18" rx="9" fill="{PANEL}"/>
<g clip-path="url(#bar)">{segs}</g>
{legend}
"""
    return frame(h, "$ which --all toolchain", body)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, fn in [("hero", hero), ("whoami", disasm), ("binarypilot", project), ("stack", stack)]:
        (OUT / f"{name}.svg").write_text(fn())
        print("wrote", name)
