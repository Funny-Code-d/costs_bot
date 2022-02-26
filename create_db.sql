-- create table with configuration info bot

CREATE TABLE conf (
	token text NOT NULL,
	name_bot text NOT NULL,
	password text NOT NULL,
	PRIMARY KEY (token)
	);

-- create table with ID users

CREATE TABLE list_users (
	telegram_id integer NOT NULL,
	PRIMARY KEY (telegram_id)
	);

-- create table with information of buy

CREATE TABLE table_costs (
	id_cost serial PRIMARY KEY,
	user_id integer NOT NULL,
	sum integer NOT NULL,
	category text NOT NULL,
	date_cost date NOT NULL,
	description text,
	FOREIGN KEY (user_id)
		REFERENCES list_users(telegram_id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
	);

-- create table with debtors

CREATE TABLE table_duty (
	deptor_id serial PRIMARY KEY,
	user_id integer NOT NULL,
	deptor_name text NOT NULL,
	type_group text NOT NULL,
	deptor_sum integer NOT NULL DEFAULT 0,
	FOREIGN KEY (user_id)
		REFERENCES list_users(telegram_id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
	);

-- create table with history debtors

CREATE TABLE table_duty_history (
	dept_id serial PRIMARY KEY,
	user_id integer NOT NULL,
	deptor_name text NOT NULL,
	summa integer NOT NULL,
	description text,
	date_registration date NOT NULL,
	type_group text NOT NULL,
	FOREIGN KEY(user_id)
		REFERENCES list_users(telegram_id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
	);



-- create personal categories
CREATE TABLE category (
    ID serial PRIMARY KEY, 
    user_id integer, 
    name_category text, 
    FOREIGN KEY (user_id) 
        REFERENCES list_users(telegram_id) 
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- create personal view
CREATE TABLE personal_views (
	user_id integer,
	category_id integer array,
	name_view varchar(30),
	number_days integer,
	PRIMARY KEY (user_id, category_id, name_view, number_days),
	FOREIGN KEY (user_id)
		REFERENCES list_users(telegram_id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);