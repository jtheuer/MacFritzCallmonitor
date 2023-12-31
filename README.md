# MacFritz call monitor
Shows incoming and outgoing calls as notification badges on MacOS. Requires a FritzBox.

# Latest release: version 0.0.1

<img width="361" alt="image" src="https://github.com/jtheuer/MacFritzCallmonitor/assets/96364/8633b300-113b-4284-bb28-ac01e587f5d9">
<img width="785" alt="image" src="https://github.com/jtheuer/MacFritzCallmonitor/assets/96364/eb071c66-b0a4-4cce-bbeb-4635a0e229e3">

* Shows incoming/outgoing calls as notifications
* No addressbook feature, yet
* Fixed fritzbox address at `fritz.box`

[Download](https://github.com/jtheuer/MacFritzCallmonitor/releases/download/0.0.1/MacFritz.call.monitor.app.zip)

# Build and run

```bash
$> virtualenv .env
$> . .env/bin/activate.fish  # for the fish shell
$> python setup.py py2app
$> open dist/MacFritz\ call\ monitor.app
```

# Thanks

This tool is build based on the excellent work of [rumps](https://github.com/jaredks/rumps) and [fritzconnection](https://github.com/kbr/fritzconnection).
