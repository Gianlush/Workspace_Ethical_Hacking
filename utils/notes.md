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
bypass local security restriction: https://gtfobins.github.io/\
payload: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md\
https://book.hacktricks.xyz/\
intercept and modify requests, public endpoint:
- https://pipedream.com/requestbin\
- https://webhook.site/#!/view/36d22d40-393f-4680-a239-cf0d7488e238\
- https://testt.free.beeceptor.com

# notes
bypass http blacklist filter with `dict://` `gopher://`
## Jinja2 SSTI
bypass blacklisted character: https://ctf.zeyu2001.com/2022/securinets-ctf-finals-2022/strong\
using filter to get arguments from url or headers or form (if it is a post) which contains desidered blacklisted char\
example: https://github.com/Gianlush/Workspace_Ethical_Hacking/tree/main/hack_the_box/htb_challenges/web/DoxPit - `request|attr('args')|list|last`