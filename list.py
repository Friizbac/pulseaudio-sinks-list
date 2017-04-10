import dbus
import os

def connect():
    if 'PULSE_DBUS_SERVER' in os.environ:
        address = os.environ['PULSE_DBUS_SERVER']
    else:
        bus = dbus.SessionBus()
        server_lookup = bus.get_object("org.PulseAudio1", "/org/pulseaudio/serv$
        address = server_lookup.Get("org.PulseAudio.ServerLookup1", "Address", $

    return dbus.connection.Connection(address)

conn = connect()
core = conn.get_object(object_path="/org/pulseaudio/core1")

print (core.Get("org.PulseAudio.Core1", "Sinks", dbus_interface="org.freedeskto$
