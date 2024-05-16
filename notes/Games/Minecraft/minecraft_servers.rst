================
Minecaft Service
================

------------
Server Setup
------------

A service has been setup for all minecraft servers including modded servers. All minecraft 
servers are stored at /opt/minecraft/**\<server_folder\>**. To start a service you can use 
the following commands. The service has been set up to make it easy to differentiate between 
the different minecraft servers running on the same system.

.. code-block:: bash
	
	systemctl start minecraft@<server_folder>	# Start the service
	systemctl enable minecraft@<server_folder>	# Enables the service on start up
	systemctl status minecraft@<server_folder>	# Status of the service

-------------
Server Memory
-------------

To edit the amount of RAM the server uses a file named server.conf must be made in the 
\<server_folder\> directory. Adding the following lines will set up the server to run 
with 4 GB of RAM. Remember 1 GB is equivalent to 1024 MB therefor if you would like 
to change the amount of memory the server uses it is simply multiplying the amount of 
gigabytes you want to use times 1024.

.. code-block:: 

	MCMINMEM=4096M
	MCMAXMEM=4096M

----------
Monitoring
----------

After staring the minecraft service the server starts running in the background. More 
specifically it is put on what is known as a screen. To view this screen and interact with 
you can use the following few commands. Entering the screen will allow you to see the terminal 
for the minecraft server and from there you can interact with it.

.. code-block:: bash

	screen -ls				# Show all the screens in the background
	screen -r <id>.<screen_name>		# To enter the screen 

.. note::
	**IMPORTANT** -- To exit the screen you must do ctrl+A then D


