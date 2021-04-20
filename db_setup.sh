#!/bin/sh

dbHost="localhost"
dbUsername="upg"
dbPassword=""
dbName="upg_fivem"

query="
CREATE USER '${dbUsername}'@'${dbHost}' IDENTIFIED VIA|WITH mysql_native_password USING '${dbPassword}';
GRANT ALL privileges ON \`${dbName}\`.* TO 'upg'@'${dbHost}';
FLUSH PRIVILEGES;
"

echo -e ${query} | /usr/bin/mysql -u root -p