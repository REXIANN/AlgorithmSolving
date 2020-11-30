SELECT name, count(name) from animal_ins 
where name is not null
group by name
having count(name) >= 2
order by name;