SELECT film.title, film.release_year, category.category_id
FROM film INNER JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
WHERE category.name IN ('Action', 'Comedy', 'Family')