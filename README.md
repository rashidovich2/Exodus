

Python 3.7+ is required. Make sure your default python version is >=3.7
by typing `python3`.

If you are behind a NAT, it can be difficult for peers outside your subnet to
reach you when they start up. You can enable
[UPnP](https://www.homenethowto.com/ports-and-nat/upnp-automatic-port-forward/)
on your router or add a NAT (for IPv4 but not IPv6) and firewall rules to allow
TCP port 8444 access to your peer.
These methods tend to be router make/model specific.

Most should only install harvesters, farmers, plotter, full nodes, and wallets.
Building timelords and VDFs is for sophisticated users in most environments.
Exodus Network and additional volunteers are running sufficient Timelords
for testnet consensus.

# Installing
. ./activate
pip install -r requirement.dev.txt

# Running
exodus --help

