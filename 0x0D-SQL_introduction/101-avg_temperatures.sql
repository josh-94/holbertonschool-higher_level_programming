-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG (value) as avg_tmp FROM temperatures GROUP BY  city ORDER BY avg_temp DESC;
