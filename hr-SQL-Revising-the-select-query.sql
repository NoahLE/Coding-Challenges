/*! https://www.hackerrank.com/challenges/revising-the-select-query/problem */

select id, name, countrycode, district, population from city where population > 100000 and countrycode = 'USA';