DROP TABLE IF EXISTS d_user;

CREATE TABLE d_user (
	user_id VARCHAR(16) PRIMARY KEY,
	firstname VARCHAR(50) NOT NULL,
	middlename VARCHAR(50) NOT NULL,
	lastname VARCHAR(50) NOT NULL,
	email VARCHAR(150) UNIQUE NOT NULL,
	password_hash VARCHAR(250) NOT NULL,
	email_confirmed BOOLEAN DEFAULT false NOT NULL,
	created_at TIMESTAMP NOT NULL
);

CREATE INDEX 
	id_user_email_idx
ON
	d_user (user_id, email);


GRANT pg_read_all_data, pg_write_all_data TO server_pg_user;


CREATE TABLE d_advert (
	advert_id VARCHAR(16) PRIMARY KEY,
	title VARCHAR(50) NOT NULL,
	description VARCHAR(250),
	price FLOAT NOT NULL,
	creation_date TIMESTAMP NOT NULL,
	expires_in TIMESTAMP NOT NULL
);

CREATE TABLE f_user_advert (
	advert_id VARCHAR(16),
	user_id VARCHAR(16),
	conjunction_created TIMESTAMP,
	is_active BOOLEAN,
	PRIMARY KEY (advert_id, user_id)
); 

CREATE INDEX
        id_avert_id_idx
ON
        d_advert (advert_id);

CREATE INDEX
        id_user_avert_idx
ON
        f_user_advert (advert_id, user_id);


CREATE TABLE d_photo (
	filename VARCHAR(25) PRIMARY KEY,
	full_filename VARCHAR(25) NOT NULL,
	filesize_bytes INTEGER NOT NULL
);

CREATE INDEX
        filename_idx
ON
        d_photo (filename);


CREATE TABLE f_advert_photo (
        filename VARCHAR(25) PRIMARY KEY,
        advert_id VARCHAR(16) NOT NULL,
        conjunction_created TIMESTAMP
);

CREATE INDEX
        advert_id_filename_idx
ON
        f_advert_photo (advert_id, filename);




CREATE TABLE d_company (
	company_id VARCHAR(16) PRIMARY KEY,
	company_name VARCHAR(150) NOT NULL,
	company_description VARCHAR(250),
	foundation_date TIMESTAMP NOT NULL,
	itn VARCHAR(10) NOT NULL,
	psm VARCHAR(13) NOT NULL,
	address VARCHAR(250),
	creation_date TIMESTAMP NOT NULL
);

CREATE TABLE f_user_company (
	user_id VARCHAR(16),
	company_id VARCHAR(16),
	conjunction_created TIMESTAMP,
	is_active BOOLEAN,
	PRIMARY KEY (user_id, company_id)
); 

CREATE INDEX
        id_company_id_idx
ON
        d_company (company_id);

CREATE INDEX
        id_company_user_idx
ON
        f_user_company (user_id, company_id);