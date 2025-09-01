-- 코드를 작성해주세요
/*
자식이 없는 개체 수와 세대
바로 다음 세대에서 이어지지 않는것의 수
*/

with recursive gen as (
    select id, parent_id, 1 as g
    from ecoli_data
    where parent_id is null
    
    union all
    
    select e.id, e.parent_id, g.g+1
    from ecoli_data e
    join gen g on e.parent_id = g.id
)

select count(*) as COUNT, a.g as GENERATION
from gen a
left join gen b on b.parent_id = a.id
where b.id is null
group by a.g;