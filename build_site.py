"""Builds site/index.html (the hosted, installable version) from index.html (the claude.ai page)."""
import os
HERE=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(HERE,"index.html")).read()
i=src.index('<div id="fit">');head,body=src[:i].strip(),src[i:].strip()
html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#07080b">
<meta name="description" content="NeonSpin DJ: a four-deck DJ app with scratchable jog wheels, auto beatmatching, FX, headphone cue, MIDI and mix recording.">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="NeonSpin DJ">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icons/favicon.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0;font:14px system-ui,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head}
</head>
<body>
{body}
</body>
</html>
'''
open(os.path.join(HERE,"site","index.html"),"w").write(html)
print("site/index.html built,",len(html),"bytes")
