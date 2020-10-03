import sys

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import GLib, Gtk

DELAY = 5_000


def app_notification_demo(app):
    builder = Gtk.Builder()
    builder.add_from_file("app-notification.glade")

    # notification_message = builder.get_object("notification-message")

    builder.connect_signals(
        {
            "show-notification": show_notification,
            "close-notification": close_notification,
        }
    )

    main_window = builder.get_object("main-window")
    main_window.set_application(app)
    main_window.show()


def show_notification(notification_revealer):
    notification_revealer.set_reveal_child(True)
    notification_revealer.auto_hide_id = GLib.timeout_add(
        DELAY, close_notification, notification_revealer
    )


def close_notification(notification_revealer):
    notification_revealer.set_reveal_child(False)
    GLib.source_remove(notification_revealer.auto_hide_id)
    del notification_revealer.auto_hide_id


if __name__ == "__main__":
    app = Gtk.Application(application_id="org.gaphor.AppNotificationDemo")
    app.connect("activate", app_notification_demo)
    app.run(sys.argv)
