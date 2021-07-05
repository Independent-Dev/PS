-- problem: https://leetcode.com/problems/consecutive-numbers/ medium
-- solution using self join
select distinct l1.num as consecutivenums
from logs as l1
inner join logs as l2
on l1.id = l2.id + 1
inner join logs as l3
on l2.id = l3.id + 1
where l1.num = l2.num and l2.num = l3.num

-- solution using window function
select num as ConsecutiveNums
from(
    select distinct
        case when num = lag(num) over() and num = lag(num, 2) over() then num
        else null
        end as num
    from logs
) l
where num is not null