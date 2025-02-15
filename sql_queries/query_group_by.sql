-- Count the number of books each author has written
SELECT authors.name AS author_name, COUNT(books.book_id) AS total_books 
FROM books
JOIN authors ON books.author_id = authors.author_id
GROUP BY authors.name
ORDER BY total_books DESC;

-- Count the number of books in each genre
SELECT genre, COUNT(*) AS total_books 
FROM books
GROUP BY genre
ORDER BY total_books DESC;
