# NeonSpin DJ

A 4-deck DJ app in a single file: `index.html`.

## Why host it yourself
On claude.ai the app runs in a locked-down frame. These features need it hosted on its own HTTPS site:
- MIDI controllers (Chrome or Edge, on a computer or Android)
- Choosing output devices, and a separate headphone device
- Microphone input
- 4-output interfaces (outputs 3–4 for headphone cue)

Split cue works everywhere: left = main, right = cue, both mono.

## Free hosting, about 2 minutes
**Netlify Drop:** go to https://app.netlify.com/drop and drag this folder onto the page. You get an https:// link straight away. Sign up (free) to keep the link.

**GitHub Pages:**
1. Make a new public repository and upload `index.html`.
2. Open Settings → Pages, and under Source pick "Deploy from a branch", choose `main`, then click Save.
3. Your app is live at `https://<your-username>.github.io/<repo>/` within a minute.

## Hardware
- **USB sound card on a phone:** connect it with a USB-C (or Lightning camera) adapter. In Setup, set Headphone cue to "Split cue". Use a 3.5 mm to 2× RCA cable: white goes to the speakers, red to your headphones.
- **Laptop:** in Setup, set Headphone cue to "Separate device" and pick the USB card or the laptop jack for headphones. Click "Show device names" first.
- **MIDI controller:** in Setup, click Connect MIDI, then MIDI Learn. Click a control on screen and move it on the controller. For a jog wheel, click the platter, spin the wheel, then touch its top.
