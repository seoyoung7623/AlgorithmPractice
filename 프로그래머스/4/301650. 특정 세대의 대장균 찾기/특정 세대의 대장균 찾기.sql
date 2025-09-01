-- 코드를 작성해주세요
select a.id from ecoli_data a
join (select c.id from ecoli_data c
     join ecoli_data d on c.parent_id = d.id
     where d.parent_id is null) b on b.id = a.parent_id
order by a.id;