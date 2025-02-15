-- List all books along with their authors
SELECT books.title, books.publication_year, authors.name AS author_name
FROM books
INNER JOIN authors ON books.author_id = authors.author_id
ORDER BY books.publication_year ASC;

-- Find the earliest and latest book written by each author
SELECT authors.name AS author_name, 
       MIN(books.publication_year) AS first_book_year, 
       MAX(books.publication_year) AS last_book_year
FROM books
INNER JOIN authors ON books.author_id = authors.author_id
GROUP BY authors.name
ORDER BY first_book_year ASC;

