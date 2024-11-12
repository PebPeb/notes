===============
Useful Commands
===============

This is a set of commands that I have learned to use and have been helpful to me in my time 
using **Ubuntu**. This list is a hodgepodge of all different kinds of commands though for 
the most part they are made up of server commands. As much of my time has been spent 
learning **Ubuntu** server to help me with my website and minecraft server.

---------------
System Commands
---------------

.. code-block:: bash

    sudo shutdown -r now        # Restart
    sudo shutdown now

.. code-block:: bash

    top             # Allows you to see the resources being used

----------------
Network Commands
----------------

.. code-block:: bash

    ip a							# List ip information
    ip link set dev <device> down				# Turn off a network (wlan0, etc) 
    ip link set dev <device> up				# Turn on a network

.. code-block:: bash

    /etc/hosts						# Stores the names for IP addresses
    curl https://ifconfig.me ; echo				# Show public IP

^^^^^^^^^^^^^^^^^^^^^^^^^
Editting the network file
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: bash

    sudoedit /etc/netplan/50-cloud-init.yaml
    sudo netplan apply				# Apply the changes
    sudo netplan --debug apply			# If issues with command above

--------
ddclient
--------

.. code-block:: bash

    sudoedit /etc/ddclient.conf                     # edit ddclient conf
    sudo ddclient -force /etc/ddclient.conf			# force ddclient to update
    systemctl status ddclient.service			    # show ddclient status
    sudo service ddclient restart				    # restart the service
    sudo systemctl enable ddclient.service			# enable service on start up
    sudoedit /var/cache/ddclient/ddclient.cache		# edit the cache for ddclient


**web** is the domain for ddclient to use to get your current public IP address. **protocol** is 
the associated process for ddclient to interact with your domain host. This is the process for
updating your DNS based on your provider for your domain name.
	

.. code-block:: bash

   ssl=yes
   protocol=googledomains
   use=web
   web=checkip.dyndns.org
   
   login='<login>'
   password='<password>'
   example.com
   
   login='<login>'
   password='<password>'
   subdomain.example.com
   
   login='<login>'
   password='<password>'
   subdomainx.example.com




-----------------------
ReStructuredText Viewer
-----------------------

ReStructuredText viewer is a live editor that works with ReStructuredText. It is a part 
of a python library and very easy to install.

.. code-block:: python

    pip install restview

To use ReStructuredText Viewer simply use the following command

.. code-block:: bash

    restview <file>



