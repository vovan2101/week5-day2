# CREATE TABLE customers(
# 	customers_id SERIAL PRIMARY KEY,
# 	first_name VARCHAR(50),
# 	last_name VARCHAR(50)
# );
#
# CREATE TABLE movies(
# 	films_id SERIAL PRIMARY KEY,
# 	films_name VARCHAR(50),
# 	description VARCHAR(200)
# );
#
#
#
# CREATE TABLE tickets(
# 	customers_id SERIAL PRIMARY KEY,
# 	tickets_id INTEGER,
# 	order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
#
# SELECT *
# FROM tickets;