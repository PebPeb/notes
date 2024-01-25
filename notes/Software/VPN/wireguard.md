
# WireGuard

Wireguard is a light weight and "easy" to use VPN service (If you know what you are doing). Lucky for future me I do know what I am doing.

## Getting set up

``` bash
sudo apt install wireguard
```

After installing you should see `/etc/wireguard` now. This is were we are going to keep our keys (for simplicity) and our .conf files for making it easier to bring up and down wireguard.

### General Set Up

These first few steps are pretty general and are going to need to be done on both your Server and Clients. The first step is to generate our public and private key. To do this we can use the following commands. You may need to run `umask 077` before being able to generate the keys.

``` bash
wg genkey > private       # Generate Private Key
wg pubkey < private       # Generate Public Key
```
The public key will be printed out so you can either pipe it into a file or just copy and paste it into `public` (if you are wondering were I go `public` from `touch public`). It is easier to generate these keys in the local user space but would suggest moving them to `/etc/wireguard` after generating them. 

Next a config file will be needed for being able to quickly set up and take down a connection. The standard format is `/etc/wireguard/wg0.conf` though the `.conf` can be named anything. Add the following to the `.conf`.

``` 
[Interface]
PrivateKey = <locally_generated_private_key>
Address = <wg_ip>
ListenPort = <port>
```

Add the locally generated private key to the `PrivateKey` variable. This is the private key for your given machine. In order for external machines to connect they are going to need the public key which will be covered later.

The `Address` is your new wireguard network. A example IP could be `10.8.0.1/24`; remember to include the netmask along with the IP.

### Server Set Up

To allow a connection to the server a `[Peer]` needs to be added. For each Client that is going to be connecting to the server a Peer will need to be created for them. 

```
[Peer]
PublicKey = <public_key_generated_on_client>
AllowedIPs = <client_wg_ip>/32
```

Notice that the PublicKey is that of the client that is trying to connect, therefor it is currently not on the server. The easiest way I have found to get the clients public key on the server is by using *scp* to copy it over. 

Lastly the `AllowedIPs` is the given `Address` to the client. An example address that matches the one given earlier could be `10.8.0.2/24`. Though if you notice the netmask has been changed to `/32`. I am unsure why when adding the clients wireguard IP to the server the netmask is changed. You may also use `0.0.0.0/0` though I have found that this messes with other services running on the machine with this configuration.

### Client Set Up

The Client Set up is the same as the server with one additional configuration. 

```
[Peer]
PublicKey = <public_key_generated_on_server>
AllowedIPs = <server_wg_ip>/32
Endpoint = <server_ip>:<port>
```

### Example of Two Machines

For this example the server can be reached though the given address *my.wireguard.example* (public IP address).

**Server Configuration**
```
[Interface]
PrivateKey = <private_key_generated_on_server>
Address = 10.8.0.1/24
ListenPort = 51820

[Peer]
PublicKey = <public_key_generated_on_client>
AllowedIPs = 10.8.0.2/32
```

**Client Configuration**
```
[Interface]
PrivateKey = <private_key_generated_on_client>
Address = 10.8.0.2/24
ListenPort = 51820

[Peer]
PublicKey = <public_key_generated_on_server>
AllowedIPs = 10.8.0.1/32
Endpoint = my.wireguard.example:51820
```

## Connecting

After everything is set up it is as easy as running the following command to bring it up and down.

``` bash
wg-quick up <name_of_config>          # If wg0.conf then use just wg0
wg-quick down <name_of_config>
```

After this you should have access to the wireguard network defined in the configuration files.

