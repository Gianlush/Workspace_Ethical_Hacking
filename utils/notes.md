## paths
/etc/nginx/nginx.conf\
/etc/nginx/sites-enabled/(deafult)\
/etc/nginx/sites-available\
/etc/hosts\
$HOME/.shh/id_rsa\
/proc/self/environ\
/proc/self/cmdline

Nella root della webApp:\
index.js/html\
main.js/html

## commands
netstat -antp\
sudo -l\
whoami\
linpeas - WINpeas\

Bypass ip filter or perform SSRF to localhost:
- http://localtest.me
- Append to url: .nip.io

ngrok tcp 80\
`dig` to resolve your tunnel hostname and use ip instead

## websites
bypass local security restriction: https://gtfobins.github.io/ \
payload: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md \
https://book.hacktricks.xyz/ \
intercept and modify requests, public endpoint:
- https://pipedream.com/requestbin 
- https://webhook.site/#!/view/36d22d40-393f-4680-a239-cf0d7488e238 
- https://testt.free.beeceptor.com

# notes
bypass http blacklist filter with `dict://` `gopher://`
test antivirus or signature check using EICAR Files

## Implanting SSH keys
`echo "Your SSH public key here (id_rsa.pub)" > /home/<user>/.ssh/authorized_keys`

## Transferring files with SCP
from destination to source:
`scp path_file_to_send dest_user@dest_ip:/path_to_receive`

from source to destination:
`scp dest_user@dest_ip:/path_to_receive files_received `

## Reverse Shell Upgrade
quando si ottiene la shell, comunque non è possibile usare le frecce ecc perché escono caratteri strani quindi serve fare un "upgrade" della shell tramite 

    python3 -c 'import pty; pty.spawn("/bin/bash")' 
    ctrl + z 
    stty raw -echo; fg 
    doppio invio 
 
in aggiunta: 

    export TERM=xterm 
in aggiunta: (per sistemare le stringhe lunghe) 

    stty -a sulla propria macchina 
    stty rows ** columns **  (copiando i valori del result della propria macchina al passo 6 
## CSS Injection
when page header are set like font: None *
## Jinja2 SSTI
bypass blacklisted character: https://ctf.zeyu2001.com/2022/securinets-ctf-finals-2022/strong \
using filter to get arguments from url or headers or form (if it is a post) which contains desidered blacklisted char\
example: https://github.com/Gianlush/Workspace_Ethical_Hacking/tree/main/hack_the_box/htb_challenges/web/DoxPit - `request|attr('args')|list|last`