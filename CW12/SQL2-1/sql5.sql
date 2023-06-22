-- Active: 1687414198532@@127.0.0.1@5432@dvdrental
SELECT film.title, category.name AS category, language.name as language
from film JOIN film_category
on film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
JOIN language
ON language.language_id = film.language_id