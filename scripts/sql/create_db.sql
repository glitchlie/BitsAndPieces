DROP DATABASE IF EXISTS ostatki;

CREATE DATABASE
	ostatki
OWNER
	admin;

GRANT CONNECT ON DATABASE ostatki TO server_pg_user;	
