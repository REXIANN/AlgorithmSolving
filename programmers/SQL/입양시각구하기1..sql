SELECT hour(datetime) as hour , count(*) from animal_outs 
group by hour

having hour > 8 and hour < 20 
order by hour;