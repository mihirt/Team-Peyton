#!/usr/bin/env python3
import dbus, dbus.mainloop.glib, sys
from gi.repository import GLib
import threading
import signal
import sys
import RPi.GPIO as GPIO
BUTTON_GPIO = 16
B2 = 12


def on_property_changed(interface, changed, invalidated):
    #    print(interface, changed, invalidated)
    if interface != 'org.bluez.MediaPlayer1':
        return
    for prop, value in changed.items():
        if prop == 'Status':
            print('Playback Status: {}'.format(value))
        elif prop == 'Track' and 'Title' in value:
            print('Music Info:')
            for key in ('Title', 'Artist', 'Album'):
                print('   {}: {}'.format(key, value.get(key, '')))


def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def playPause(channel):
    pp = play_prop.GetAll("org.bluez.MediaPlayer1")
    status = pp['Status']
    if "play" in status:
        player_iface.Pause()
    else:
        player_iface.Play()
    return True


def next(channel):
    player_iface.Next()
    return True


def on_playback_control(fd, condition):
    str = fd.readline()
    if str.startswith('play'):
        player_iface.Play()
    elif str.startswith('pause'):
        player_iface.Pause()
    elif str.startswith('next'):
        player_iface.Next()
    elif str.startswith('prev'):
        player_iface.Previous()
    """elif str.startswith('vol'):
        vol = int(str.split()[1])
        if vol not in range(0, 128):
            print('Possible Values: 0-127')
            return True
        transport_prop_iface.Set(
                'org.bluez.MediaTransport1',
                'Volume',
                dbus.UInt16(vol))"""
    return True


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([BUTTON_GPIO, B2], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_GPIO,
                          GPIO.RISING,
                          callback=playPause,
                          bouncetime=100)

    GPIO.add_event_detect(B2, GPIO.RISING, callback=next, bouncetime=100)

    signal.signal(signal.SIGINT, signal_handler)

    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    obj = bus.get_object('org.bluez', "/")
    mgr = dbus.Interface(obj, 'org.freedesktop.DBus.ObjectManager')
    player_iface = None
    transport_prop_iface = None
    player_prop = None
    for path, ifaces in mgr.GetManagedObjects().items():
        if 'org.bluez.MediaPlayer1' in ifaces:
            player_iface = dbus.Interface(bus.get_object('org.bluez', path),
                                          'org.bluez.MediaPlayer1')
            play_prop = dbus.Interface(bus.get_object('org.bluez', path),
                                       'org.freedesktop.DBus.Properties')
        elif 'org.bluez.MediaTransport1' in ifaces:
            transport_prop_iface = dbus.Interface(
                bus.get_object('org.bluez', path),
                'org.freedesktop.DBus.Properties')
    if not player_iface:
        sys.exit('Error: Media Player not found.')

    bus.add_signal_receiver(on_property_changed,
                            bus_name='org.bluez',
                            signal_name='PropertiesChanged',
                            dbus_interface='org.freedesktop.DBus.Properties')
    # GLib.io_add_watch(sys.stdin, GLib.IO_IN, on_playback_control)
    glib_thread = threading.Thread(target=GLib.MainLoop().run())
    glib_thread.daemon = True
    glib_thread.start()
    print("suppity")
    signal.pause()
