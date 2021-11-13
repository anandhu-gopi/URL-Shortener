DROP TABLE IF EXISTS urls;

CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    original_url TEXT NOT NULL,
    short_url TEXT NOT NULL
);


/* creating index on original_url for faster 
   look up  */
CREATE UNIQUE INDEX idx_urls_original_url
ON urls (original_url);

/* creating index on short_url for faster 
   look up  */
CREATE UNIQUE INDEX idx_urls_short_url
ON urls (short_url);