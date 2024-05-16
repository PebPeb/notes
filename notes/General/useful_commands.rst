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


-------------------
SSH Keys and Access
-------------------



Setting up an **ssh** key can help make signing into a remote server much faster and easier.
To do this both the server and client side must share a key. This key can be generated on 
the client side and then shared with the server with very few commands need.

To start lets talk about what directories we are going to be working in. On default ssh sets 
up two directories to be used, one as a global use and another local one.

.. code-block:: bash

    ~/.ssh/                 # Local Directory
    /etc/ssh/               # Global Directory

In each directory there is a config file. The host only needs to be configured in one of these 
directories depending on the needs. If configured in the global directory all uses can access that
host. Though if configured in the local directory only that user on the client side can access the
host. For both the global and local config files follow the same configuration in the config.

.. code-block::

    Host <alias>
        HostName <IP/Domain>
        User <Username>
        IdentityFile <pathToKey>

Within the config file the *IdentityFile* tag is referring to the ssh key on the local host.
If a key has already been generated then you should be able to find it in either the local
or global ssh directories. If there is no key then a key will need to be generated. After 
the key is generated it will need to be shared with the server.

.. code-block:: bash

    ssh-keygen                              # Generates the key
    ssh-copy-id -i <pathToKey> user@host    # Copy key to server

After a key has been shared with the server it is as simple as using the ssh command to 
connect.

.. code-block:: bash

    ssh <alias>



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



