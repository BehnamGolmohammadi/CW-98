-- Active: 1687414198532@@127.0.0.1@5432@dvdrental
SELECT film.title,film.release_year,film_category.category_id
FROM film INNER JOIN film_category
ON film.film_id = film_category.film_id