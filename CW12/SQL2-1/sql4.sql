-- Active: 1687414198532@@127.0.0.1@5432@dvdrental
SELECT category.name, COUNT(film.film_id) AS "Total Films"
FROM film JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
GROUP BY category.name
HAVING COUNT(film.film_id) BETWEEN 60 AND 68