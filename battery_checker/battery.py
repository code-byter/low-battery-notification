import os


def init():
    """
    Load IDs of all available batteries and their capacity

    :return: battery_config (Dict containing the battery id and its size
    """
    battery_config = {}
    for item in os.listdir('/sys/class/power_supply/'):
        if os.path.isdir(os.path.join('/sys/class/power_supply/', item)) and item.startswith("BAT"):
            battery_config[item] = get_battery_energy_full(item)
    return battery_config


def get_status(battery_config):
    """
    Get the current battery status (percentage and charging status) for all internal batteries combined

    :param battery_config: dict containing the battery IDs and their capacity
    :return: dict containing the percentage and the charging status
    """
    battery_status = {'charging': False, 'percentage': 0}

    for battery_id in battery_config.keys():
        battery_status['charging'] = battery_status['charging'] | get_charging_status(battery_id)
        battery_status['percentage'] += get_battery_charge(battery_id) * battery_config[battery_id]

    battery_status['percentage'] = int(battery_status['percentage'] / sum(battery_config.values()))

    return battery_status


def get_charging_status(battery_id):
    """
    Check if the battery is currently charging

    :param battery_id: Battery ID/Number e.g. BAT0
    :return: bool, True is battery is charging
    """
    with open(f'/sys/class/power_supply/{battery_id}/status') as f:
        if 'Charging' in f.read():
            return True
    return False


def get_battery_charge(battery_id):
    """
    Get the current battery percentage

    :param battery_id: Battery ID/Number e.g. BAT0
    :return: current charge level in percent
    """
    with open(f'/sys/class/power_supply/{battery_id}/capacity') as f:
        battery_percentage = int(f.read())
    return battery_percentage


def get_battery_energy_full(battery_id):
    """
    Get the maximum energy stored in the battery

    :param battery_id: Battery ID/Number e.g. BAT0
    :return: maximum energy (int)
    """
    with open(f'/sys/class/power_supply/{battery_id}/energy_full') as f:
        battery_percentage = int(f.read())
    return battery_percentage
