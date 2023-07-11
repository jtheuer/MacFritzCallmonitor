# MacFritz call monitor
Shows incoming and outgoing calls as notification badges on MacOS

# Latest release: version 0.0.1

* Shows incoming/outgoing calls as notifications
* No addressbook feature, yet
* Fixed fritzbox address at `fritz.box`

# Build and run

```bash
$> virtualenv .env
$> . .env/bin/activate.fish  # for the fish shell
$> python setup.py py2app
$> open dist/MacFritz\ call\ monitor.app
```

# Thanks

This tool is build based on the excellent work of [rumps](https://github.com/jaredks/rumps) and [fritzconnection](https://github.com/kbr/fritzconnection).
