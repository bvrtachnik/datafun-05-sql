--Find the most common author nationality
SELECT nationality, COUNT(*) AS nationality_count
FROM authors
GROUP BY nationality
ORDER BY nationality_count DESC
LIMIT 1;

-- Find the number of authors who are British
SELECT COUNT(*) AS british_authors
FROM authors
WHERE nationality = 'British';

-- Find the oldest book in the dataset
SELECT 
    title, 
    publication_year 
FROM books 
ORDER BY publication_year ASC 
LIMIT 1;

-- Find the most recently published book in the dataset
SELECT 
    title, 
    publication_year 
FROM books 
ORDER BY publication_year DESC 
LIMIT 1;

-- Calculate the average publication year
SELECT AVG(publication_year) AS avg_publication_year FROM books;
