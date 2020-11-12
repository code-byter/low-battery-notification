================================
Low Battery notifications for i3
================================

This python package checks the current battery status and sends a notification if the battery. Notifications are sent for the following events:

- Battery percentage < 10%
- Battery percentage < 3%
- Battery is charging

Installation
------------

First install notify2.

.. code::

    sudo apt-get update
    sudo apt-get install -y python3-notify2

Next, clone the repository and install the python package

.. code::

    git clone https://github.com/code-byter/low-battery-notification.git
    cd low-battery-notification
    pip3 install .

Replace ``codebyter`` in the ``battery_checker.service`` file with user username and copy it to ``/etc/systemd/system/``.

.. code::

    sudo cp battery_checker.service /etc/systemd/system/battery_checker.service

Enable the service and start automatically when booting.

.. code::

    sudo systemctl enable battery_checker.service
    sudo systemctl start battery_checker.service