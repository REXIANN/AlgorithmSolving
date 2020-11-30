SELECT agent_code, COUNT(agent_code) 
FROM orders  GROUP BY agent_code 
HAVING COUNT (agent_code)=( 
SELECT MAX(mycount) 
FROM ( 
SELECT agent_code, COUNT(agent_code) mycount 
FROM orders 
GROUP BY agent_code)); 