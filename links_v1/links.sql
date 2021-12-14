-- These SQL commands are for SQLite database engine
-- For MySQL, PostgreSQL etc. they might be different 

CREATE TABLE IF NOT EXISTS 'link' (
	'short'	VARCHAR NOT NULL UNIQUE PRIMARY KEY,
	'long'	VARCHAR NOT NULL,
	'hits'	INTEGER DEFAULT 0
);
