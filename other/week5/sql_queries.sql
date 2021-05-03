-- Please select all columns of the table large_countries and order the entries by population size in descending order
SELECT *
FROM large_countries 
ORDER BY population DESC;


-- Please write a query that returns the average population per continent
SELECT ROUND(AVG(population)) AS average_population, continent
FROM large_countries 
GROUP BY continent;

-- Please write a query that returns the average population per continent and orders the continents by average population size. Combine the two concepts
SELECT ROUND(AVG(population)) as average_population, continent 
FROM large_countries 
GROUP BY continent 
ORDER BY average_population DESC; 


-- Please select all columns of the table large_countries but only the first 3 rows 
SELECT * 
FROM large_countries 
LIMIT 3; 

-- Please write a query that returns the average population per continent
SELECT AVG(population), continent 
FROM large_countries 
GROUP BY continent;

-- Please write a query that returns the average population per continent but only return the first 3 rows. Combine the two concepts
SELECT AVG(population), continent FROM large_countries GROUP BY continent LIMIT 3;


-- Please select all columns of the table large_countries for countries that have a population of more than 200_000_000.
SELECT * 
FROM large_countries 
WHERE population > 200000000;


-- Please write a query that returns the average population per continent
SELECT continent, AVG(population) 
FROM large_countries 
GROUP BY continent; 


-- Please write a query that returns the average population per continent for all countries with more than 200_000_000 inhabitants. Combine the two concepts
SELECT continent, AVG(population) as average_population
FROM large_countries 
-- where population > 200000000 if we want to filter on country level
GROUP BY continent
HAVING AVG(population) > 200000000;



-- Select only the columns country and population and order in descending order by population size




--  Select all countries with more than 200,000,000 inhabitants




-- Select the three countries with the highest fertility rate; combination of order by and limit




-- Select all countries which start with "I"
select *
from large_countries
where country like 'I%';



-- Select all countries which start with "I" and have more than 300,000,000 inhabitants
select *
from large_countries
where country like 'I%' OR population > 300000000;



-- Update South America and North America to The Americas
update large_countries
set continent = case 
					when continent = 'South America' then 'The Americas'
					when continent = 'North America' then 'The Americas'
					-- when continent like '%America' then 'The Americas'
					-- when continent in ('South America', 'North America') then 'The Americas'
					-- when continent = 'South America' or continent = 'North America' then 'The Americas'
					else continent
				end;

select * from large_countries as lc ;

-- Show the largest and the smallest country by number of inhabitants



-- Truncate tables; the table is still there, only the values are gone
truncate table large_countries;

select * from large_countries as lc ;


-- Delete the table; the table will be gone


drop table large_countries;

select * from large_countries as lc ;
