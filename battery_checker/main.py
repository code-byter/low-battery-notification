import time

import notify2

from battery_checker import battery


def send_notification(title, text, urgency, timeout=notify2.EXPIRES_DEFAULT):
    """
    Send a notification

    :param title: Notification Title
    :param text: Notification Text
    :param urgency: Notification urgency
    :param timeout: Notification timeout
    :return: None
    """
    print(f"Notification {title}")
    n = notify2.Notification(title, text)
    n.set_urgency(urgency)
    n.set_timeout(timeout)
    n.show()


def check_status():
    """
    Check battery status and send a notification if battery is charging or the battery is low

    :return:
    """
    notify2.init('Battery Warning1')
    battery_config = battery.init()
    currrent_battery_status = battery.get_status(battery_config)
    check_status.is_charging = currrent_battery_status['charging']

    while True:
        updated_battery_status = battery.get_status(battery_config)
        # Battery plugged in
        if currrent_battery_status['charging'] is False and updated_battery_status[
                'charging'] is True and check_status.is_charging is False:
            send_notification("Charging", "Your battery is charging", notify2.URGENCY_NORMAL)
            check_status.is_charging = True
            check_status.low = False
            check_status.empty = False
        # Stop charging
        elif check_status.is_charging is True and updated_battery_status['percentage'] < 99:
            check_status.is_charging = updated_battery_status['charging']
        # Battery percentage < 10%
        elif updated_battery_status['percentage'] < 10 and check_status.low is False and updated_battery_status[
                'charging'] is False:
            send_notification("Low battery", f"Battery percentage: {updated_battery_status['percentage']}",
                              notify2.URGENCY_NORMAL)
            check_status.low = True
        # Battery percentage < 3%
        elif updated_battery_status['percentage'] < 3 and check_status.empty is False and updated_battery_status[
                'charging'] is False:
            send_notification("Empty battery", f"Battery percentage: {updated_battery_status['percentage']}",
                              notify2.URGENCY_CRITICAL, timeout=notify2.EXPIRES_NEVER)
            check_status.empty = True

        currrent_battery_status = updated_battery_status
        time.sleep(5)


if __name__ == '__main__':
    check_status()
