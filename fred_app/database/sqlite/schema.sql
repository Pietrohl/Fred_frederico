CREATE TABLE IF NOT EXISTS lists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    created_at integer(4) not null default (strftime('%s', CURRENT_TIMESTAMP)) NOT NULL,
    owner INTEGER,
    done BOOLEAN
);