-- Join the orders table with the customers table
-- select count(*)
select c.companyname, c.customerid, o.orderdate
from customers as c
join orders as o on o.customerid = c.customerid
-- by default, if you just write join it is an inner join


-- Create a table from a SQL Query
create table new_table as
select c.companyname, c.customerid, o.orderdate 
from customers as c
join orders as o on o.customerid = c.customerid


-- Create a view from SQL Query -- does not actually store anything 
create view new_view as
select c.companyname, c.customerid, o.orderdate 
from customers as c
join orders as o on o.customerid = c.customerid


-- Select * from view
select * from new_view


-- Write a left join
select c.companyname, c.customerid, o.orderdate 
from customers as c
left join orders as o on o.customerid = c.customerid
where orderdate is null 


-- Write a right join
select c.companyname, c.customerid, o.orderdate 
from customers as c
right join orders as o on o.customerid = c.customerid


-- Write a full outer join
select c.companyname, c.customerid, o.orderdate 
from customers as c
full join orders as o on o.customerid = c.customerid


-- How do I add order_details now? 
select c.companyname, c.customerid, sum(od.quantity * od.unitprice) as revenue 
from customers as c
join orders as o on o.customerid = c.customerid
join order_details as od on od.orderid = o.orderid
group by c.companyname, c.customerid
order by revenue desc