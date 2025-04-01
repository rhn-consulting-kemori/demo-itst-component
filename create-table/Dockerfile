# Use postgres
FROM postgres
COPY create_table.sql /tmp
CMD /usr/bin/psql postgres://$DB_USER:$DB_PASSWORD@$DB_SERVERNAME:$DB_PORTNUMBER -f /tmp/create_table.sql
