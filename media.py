#!/usr/bin/env python3
import dbus, dbus.mainloop.glib, sys
from gi.repository import GLib
import threading
import signal
import sys
import RPi.GPIO as GPIO
B1 = 22
B2 = 12
B3 = 25
B4 = 24
B5 = 23
B6 = 13
B7 = 9
B8 = 5
import play_audio_pygame as play_audio
#minor edit test

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
    print("16 called!")
    pp = play_prop.GetAll("org.bluez.MediaPlayer1")
    status = pp['Status']
    if "play" in status:
        player_iface.Pause()
        play_audio.say_pause()
    else:
        player_iface.Play()
        play_audio.say_play()
    return True


def next(channel):
    print("12 called!")
    player_iface.Next()
    play_audio.say_skip()
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
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([B1, B2, B3, B4, B5, B6, B7, B8],
               GPIO.IN,
               pull_up_down=GPIO.PUD_UP)
    # GPIO.add_event_detect(BUTTON_GPIO,
    #                       GPIO.RISING,
    #                       callback=playPause,
    #                       bouncetime=500)
    #
    # GPIO.add_event_detect(B2, GPIO.RISING, callback=next, bouncetime=500)
    GPIO.add_event_detect(B1,
                          GPIO.RISING,
                          callback=play_audio.B1,
                          bouncetime=500)
    GPIO.add_event_detect(B2,
                          GPIO.RISING,
                          callback=play_audio.B2,
                          bouncetime=500)
    GPIO.add_event_detect(B3,
                          GPIO.RISING,
                          callback=play_audio.B3,
                          bouncetime=500)
    GPIO.add_event_detect(B4,
                          GPIO.RISING,
                          callback=play_audio.B4,
                          bouncetime=500)
    GPIO.add_event_detect(B5,
                          GPIO.RISING,
                          callback=play_audio.B5,
                          bouncetime=500)
    GPIO.add_event_detect(B6,
                          GPIO.RISING,
                          callback=play_audio.B6,
                          bouncetime=500)
    GPIO.add_event_detect(B7,
                          GPIO.RISING,
                          callback=play_audio.B7a,
                          bouncetime=500)
    GPIO.add_event_detect(B8,
                          GPIO.RISING,
                          callback=play_audio.B8,
                          bouncetime=500)
    signal.signal(signal.SIGINT, signal_handler)

    # dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    # bus = dbus.SystemBus()
    # obj = bus.get_object('org.bluez', "/")
    # mgr = dbus.Interface(obj, 'org.freedesktop.DBus.ObjectManager')
    # player_iface = None
    # transport_prop_iface = None
    # player_prop = None
    # for path, ifaces in mgr.GetManagedObjects().items():
    #     print(ifaces)
    #     if 'org.bluez.MediaPlayer1' in ifaces:
    #         player_iface = dbus.Interface(bus.get_object('org.bluez', path),
    #                                       'org.bluez.MediaPlayer1')
    #         play_prop = dbus.Interface(bus.get_object('org.bluez', path),
    #                                    'org.freedesktop.DBus.Properties')
    #     elif 'org.bluez.MediaTransport1' in ifaces:
    #         transport_prop_iface = dbus.Interface(
    #             bus.get_object('org.bluez', path),
    #             'org.freedesktop.DBus.Properties')
    # if not player_iface:
    #     sys.exit('Error: Media Player not found.')
    #
    # bus.add_signal_receiver(on_property_changed,
    #                         bus_name='org.bluez',
    #                         signal_name='PropertiesChanged',
    #                         dbus_interface='org.freedesktop.DBus.Properties')
    # # GLib.io_add_watch(sys.stdin, GLib.IO_IN, on_playback_control)
    # glib_thread = threading.Thread(target=GLib.MainLoop().run())
    # glib_thread.daemon = True
    # glib_thread.start()
    print("suppity")
    signal.pause()
