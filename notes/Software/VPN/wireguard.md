
# WireGuard

Wireguard is a light weight and "easy" to use VPN service (If you know what you are doing). Lucky for future me I do know what I am doing.

## Getting set up

``` bash
sudo apt install wireguard
```

After installing you should see `/etc/wireguard` now. This is were we are going to keep our keys (for simplicity) and our .conf files for making it easier to bring up and down wireguard.

## General Set Up

These first few steps are pretty general and are going to need to be done on both your Server and Clients. The first step is to generate our public and private key. To do this we can use the following commands. You may need to run `umask 077` before being able to generate the keys.

``` bash
wg genkey > private       # Generate Private Key
wg pubkey < private       # Generate Public Key
```
The public key will be printed out so you can either pipe it into a file or just copy and paste it into `public` (if you are wondering were I go `public` from `touch public`). It is easier to generate these keys in the local user space but would suggest moving them to `/etc/wireguard` after generating them. 

Next a config file will be needed for being able to quickly set up and take down a connection. The standard format is `/etc/wireguard/wg0.conf` though the `.conf` can be named anything. 

## Server Set Up




