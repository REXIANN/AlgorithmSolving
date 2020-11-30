SET @HOUR_IT := -1;
SELECT @HOUR_IT := @HOUR_IT + 1 as hour, 
    ( select count(*) from animal_outs
      where hour(datetime) = @HOUR_IT) as count
from animal_outs
where @HOUR_IT < 23;