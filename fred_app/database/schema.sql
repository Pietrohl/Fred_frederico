create table if not exists lists (
    id serial primary key,
    name text not null,
    location text not null
);