-- These SQL commands are for SQLite database engine
-- For MySQL, PostgreSQL etc. they might be different 

CREATE TABLE IF NOT EXISTS 'task' (
  'id' INTEGER NOT NULL PRIMARY KEY,
  'title' VARCHAR NOT NULL,
  'complete' BOOLEAN NOT NULL DEFAULT 0
);
