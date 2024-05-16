==============
Apache2 Server
==============

Apache2 is a web hosting service that can be used to deploy web 
applications. This is what I am using to deploy my web applications
on this server. Over all it is very easy to work with. This documentation 
will hopefully help me remember what I am doing after months of 
not looking at it.

-----------------------
Apache2 Directory Guide
-----------------------

For configuring apache2 all files are located at :code:`/etc/apache2`.

To add a new configurable webpage go to :code:`sites-available` and 
make a new *.conf* file. Since I am using the same IP for multiple 
web servers and websites use port 80 I need to use a reverse proxy. 
This allows apache2 to direct a specific domain name from port 80 to 
a different port. Below is an example of a reverse proxy from a given 
domain name to :code:`<Port_Num>`. Replacing :code:`<Port_Num>` with 
the port you want your webpage to be running on locally.

.. code:: 

    # Reverse proxy
    <VirtualHost *:80>
        ServerName <subdomain.domain_name>
        ServerName <subdomain.domain_name> # Secondary Domain name

        <Proxy *>
            Order allow,deny
            Allow from all
        </Proxy>

        ProxyPreserveHost On
        ProxyPass / http://localhost:<Port_Num>/
        ProxyPassReverse / http://localhost:<Port_Num>/
    </VirtualHost>


After the reverse proxy is set up we are able to set up multiple sites 
all from port 80. For each website a reverse proxy is needed to be set 
up. After this in the same file or a new *.conf* file and the website 
configurations need to be set up. 

.. code:: 

    # Run website on <Port_Num>
    <VirtualHost *:<Port_Num>>
        ServerName localhost
        DocumentRoot <dir_to_page>

        <Directory "<dir_to_page>">
            Options FollowSymLinks
            AllowOverride All
            Require all granted
        </Directory>
    </VirtualHost>   

After this return back to Apache2s home directory and you will see a 
file named :code:`ports.conf`. In that folder you must add the port 
of your new webpage :code:`Listen <Port_Num>`. Once this is finished 
all configurations are complete

----------------
Apache2 Commands
----------------

.. code:: bash

    a2ensite <conf_file>        # Enable a configfile/website
    a2dissite <conf_file>       # Disabled a configfile/website
    systemctl restart apache2   # Restart Apache2 Services
    systemctl reload apache2    # Reload Apache2 without restarting
