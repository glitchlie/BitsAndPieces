export PGPASSWORD=St0r3C@r3fu11y

cat ./sql/create_roles.sql | sudo -u postgres psql
cat ./sql/create_db.sql | sudo -u postgres psql
cat ./sql/create_tables.sql | psql -h localhost -d ostatki -U admin
cat ./sql/create_dummy_company.sql | psql -h localhost -d ostatki -U admin