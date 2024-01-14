SELECT DISTINCT ship_city, ship_country
FROM orders
WHERE ship_city LIKE('%burg')