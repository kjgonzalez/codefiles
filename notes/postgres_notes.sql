-- NOTE: all notes here are postgres-specific, but some apply to SQL in general
\dt  -- list tables in current db
\l   -- list all available db's
\c <newdb> <newuser> -- connect to newdb as newuser
\q -- quit psql

-- basic creation -------------------
create database mydb;
create user john with encrypted password 'princess';
grant all privileges on mydb to john;
grant all on schema public to john;
---
create table dtypes(
    ind uuid primary key default gen_random_uuid() not null,
    autoinc bigserial not null,
    tstamp timestamp default (now() at time zone 'utc') not null,
    epoch bigint default (EXTRACT(EPOCH from now()) * 1000000)::bigint not null
);
-- for the above table, you can insert all default values simply by typing: 
insert into dtypes default values;
-- insert to specifically named columns
insert into dtypes (epoch) values (12);


-- destruction ------------------------
truncate mytable; -- remove all rows from table, but keep everything else



-- list columns of a table
select column_name from information_schema.columns 
where table_name = 'TABLENAME' 
and table_schema = 'SCHEMANAME'; --schema e.g. 'public'


