create table if not EXISTS user_data (
	id uuid primary key,
	first_name varchar(255),
	last_name varchar(255),
	gender varchar(10),
	address text,
	post_code varchar(20),
	email varchar(255),
	dob date,
	registered_date timestamp,
	phone varchar(20),
	picture varchar(255),
	timestamp timestamp,
	labels varchar(50)
)