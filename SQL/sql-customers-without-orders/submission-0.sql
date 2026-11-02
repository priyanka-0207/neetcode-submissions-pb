select name from customers c left join orders o on c.id = o.customer_id 
where c.id not in (select customer_id from orders);
