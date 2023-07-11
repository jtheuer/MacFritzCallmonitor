import time
from functools import partial

import rumps
import queue
import threading
from fritzconnection.core.fritzmonitor import FritzMonitor

from fritz.utils import parse_call_log


class FritzCallMonitor(rumps.App):
    def __init__(self, debug=False):
        super(FritzCallMonitor, self).__init__("Calls", "📞")
        rumps.debug_mode(debug)
        self.menu_status = rumps.MenuItem("Not connected", callback=None, key=None, icon=None, dimensions=None, template=None)
        self.menu_show_incoming = rumps.MenuItem("Show incoming calls", callback=self._click_toggle, key=None, icon=None, dimensions=None, template=None)
        self.menu_show_incoming.state = True
        self.menu_show_outgoing = rumps.MenuItem("Show outgoing calls", callback=self._click_toggle, key=None, icon=None, dimensions=None, template=None)
        self.menu = [self.menu_status, self.menu_show_incoming, self.menu_show_outgoing, "Test"]

    def _click_toggle(self, menu):
        menu.state = not menu.state

    @rumps.clicked("Test")
    def test(self, _):
        self.show_incoming_call("+49 123 456", "+49 789 000", "just a test")

    def show_outgoing_call(self, from_number, to_number, time):
        if self.menu_show_outgoing.state:
            rumps.notification(f"Call to {to_number}", f"from {from_number}", time)

    def show_incoming_call(self, from_number, to_number, time):
        if self.menu_show_incoming.state:
            rumps.notification(f"Call from {from_number}", f"to {to_number}", time)

    def fritzbox_status(self, hostname, is_connected=False):
        icon = "🟢" if is_connected else "⚪"
        self.menu_status.title = f"{icon} {hostname}"


def call_monitor(fritz_call_monitor, address='fritz.box'):
    try:
        while True:
            try:
                print(f"Connecting to {address}")
                # as a context manager FritzMonitor will shut down the monitor thread
                with FritzMonitor(address) as monitor:
                    event_queue = monitor.start()
                    fritz_call_monitor.fritzbox_status(address, True)
                    print(f"Connected to {address}")
                    while monitor.is_alive:
                        try:
                            event = event_queue.get(timeout=10)
                        except queue.Empty:
                            continue
                        else:
                            result = parse_call_log(event)
                            if result:
                                if result['type'] == 'RING':
                                    fritz_call_monitor.show_incoming_call(result['from'], result['to'], result['time'])
                                elif result['type'] == 'CALL':
                                    fritz_call_monitor.show_outgoing_call(result['from'], result['to'], result['time'])
                            print(event)
                            print(str(result))
                print(f"Disconnected from {address}")
            except TimeoutError:
                print(f"Timeout on {address}. Reconnecting...")

            fritz_call_monitor.fritzbox_status(address, True)
            time.sleep(5)
    except (OSError, KeyboardInterrupt) as err:
        print(err)


if __name__ == "__main__":
    fritz = FritzCallMonitor(debug=True)
    threading.Thread(target=partial(call_monitor, fritz), name="background_monitor").start()
    fritz.run()
    print("end")
