use sakila; 
SELECT * FROM city
SELECT * FROM address

SELECT address, city
From address a
JOIN city c
ON(a.city_id=c.city_id);