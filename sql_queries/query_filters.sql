-- Filter books published after the year 2000, sorted from oldest to newest
SELECT title, publication_year 
FROM books 
WHERE publication_year > 2000
ORDER BY publication_year ASC;

-- Find all books in the Fantasy Genre
SELECT title, genre, publication_year 
FROM books 
WHERE genre = 'Fantasy'
ORDER BY publication_year DESC;

-- Find all authors born before 1930
SELECT name, birth_year 
FROM authors 
WHERE birth_year < 1930
ORDER BY birth_year ASC;

-- Find books written by J.K. Rowling 
SELECT books.title, books.publication_year 
FROM books
JOIN authors ON books.author_id = authors.author_id
WHERE authors.name = 'J.K. Rowling'
ORDER BY books.publication_year ASC;
