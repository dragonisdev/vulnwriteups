### Iterating through important wireshark commands that might become useful later on

All protocols we gotta remember:
- frame
- http
- dns
- ftp
- smtp
- icmp
- arp
- tcp
- udp
- data-text-lines

We can use regex for matches `[A-Za-z0-9+/]{30,}={0,2}`


`http.request.method == "POST"`

finds all HTTP request with method "POST"

`tcp.port == 443`

finds TCP port 443 requests which is HTTPS

`tls.handshake.type == 1`

ClientHello handshakes

`http.request.uri contains "text"`

get all http requests with plaintext "text"

`dns contains "text"`

dns name contains text

`icmp containst text`

pings

`frame contains "text"`

all global request frames


Get rid of noise:

`!arp && !icmp && !dns && ip.len > 100 && frame.len > 200`

- !arp → exclude ARP packets

- !icmp → exclude ICMP packets

- !dns → exclude DNS packets

- ip.len > 100 → only IP packets larger than 100 bytes

- frame.len > 200 → only frames larger than 200 bytes