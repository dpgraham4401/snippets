alter table users
drop column if exists state;

alter table addresses
    add column if not exists state varchar(255) null;