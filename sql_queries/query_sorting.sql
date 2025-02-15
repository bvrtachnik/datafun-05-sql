-- Sort books alphabetically by title
SELECT title, genre, publication_year 
FROM books 
ORDER BY title ASC;

-- Sort books oldest to newest
SELECT title, genre, publication_year 
FROM books 
ORDER BY publication_year DESC;

-- Sort authors alphabetically
SELECT name, birth_year, nationality
FROM authors
ORDER BY name ASC;
