select p.first_name as first_name, p.last_name as last_name, (case when a.city is null then null else a.city end) as city, (case when a.state is null then null else a.state end) as state from person p left join address a 
on p.person_id = a.person_id;
