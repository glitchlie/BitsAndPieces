DO
$do$
BEGIN
   IF EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE  rolname = 'admin') THEN

      RAISE NOTICE 'Role "admin" already exists. Skipping.';
   ELSE
      CREATE ROLE admin LOGIN PASSWORD 'St0r3C@r3fu11y';
   END IF;
END
$do$;

ALTER USER admin WITH SUPERUSER;

DO
$do$
BEGIN
   IF EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE  rolname = 'server_pg_user') THEN

      RAISE NOTICE 'Role "server_pg_user" already exists. Skipping.';
   ELSE
      CREATE ROLE server_pg_user LOGIN PASSWORD 'St0r3C@r3fu11y';
   END IF;
END
$do$;

