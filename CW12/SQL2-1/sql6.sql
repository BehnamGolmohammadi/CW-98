SELECT customer.first_name, customer.last_name, film.title, (rental.return_date - rental.rental_date) AS "rental_duration"
from customer JOIN rental
ON customer.customer_id = rental.customer_id
JOIN inventory
ON rental.inventory_id = inventory.inventory_id
JOIN film
ON inventory.film_id = film.film_id