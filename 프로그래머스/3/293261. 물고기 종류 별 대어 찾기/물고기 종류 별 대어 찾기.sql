-- 코드를 작성해주세요
Select  a.id, b.fish_name, a.length
from fish_info a
join fish_name_info b on a.fish_type = b.fish_type
where (select max(f.length) 
       from fish_info f
       where f.fish_type = a.fish_type) = a.length
order by a.id

