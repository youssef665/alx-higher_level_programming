-- Displays the average temperature (in Fahrenheit) by city ordered descendicly

SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
