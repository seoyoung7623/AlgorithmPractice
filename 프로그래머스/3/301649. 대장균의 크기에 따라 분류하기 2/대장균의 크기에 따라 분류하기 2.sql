-- 코드를 작성해주세요
select a.id,
case
    when ps <= 0.25 then 'CRITICAL'
    when ps <= 0.5 then 'HIGH'
    when ps <= 0.75 then 'MEDIUM'
    when ps <= 1 then 'LOW'
end as COLONY_NAME
from (
    select id, percent_rank() over (order by size_of_colony desc) as ps from ecoli_data
    order by size_of_colony desc
) a
order by a.id