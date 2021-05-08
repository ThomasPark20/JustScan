# JustScan
Lightweight scanner written in python that scans all Unofficial/Official ports and grabs WHOIS lookup of the domain

# Installation
run pip install -r requirements.txt in the installation folder to install python-whois.

# Example
```
$python3 JustScan.py

Host IP or Domain: Tomhacks.tech
timeout setting (2 is default): 2

OUTPUT:

---PORTS---
22: OPEN
80: OPEN
443: OPEN
---WHOIS---
{
  "domain_name": "TOMHACKS.TECH",
  "registrar": "Dotserve Inc",
  "whois_server": "whois.dotserve.website",
  "referral_url": null,
  "updated_date": "2021-02-15 21:37:29",
  "creation_date": "2020-10-28 23:27:33",
  "expiration_date": "2021-10-28 23:59:59",
  "name_servers": [
    "NS3.DIGITALOCEAN.COM",
    "NS2.DIGITALOCEAN.COM",
    "NS1.DIGITALOCEAN.COM"
  ],
  "status": "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
  "emails": "abuse@dotserve.website",
  "dnssec": "unsigned",
  "name": null,
  "org": "N/A",
  "address": null,
  "city": null,
  "state": "484",
  "zipcode": null,
  "country": "CA"
}
```

# TODO
Socket Fail message pops up occasionally, no issue in functionality
UDP support

