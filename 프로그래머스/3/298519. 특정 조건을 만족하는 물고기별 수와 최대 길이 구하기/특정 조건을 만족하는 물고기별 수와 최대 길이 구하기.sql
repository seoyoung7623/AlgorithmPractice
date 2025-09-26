-- 코드를 작성해주세요
select count(*) as fish_count, max(length) as max_length, fish_type
from (select id,fish_type,if(length=null,10,length) as length
      from fish_info
) fish_info
group by fish_type
having avg(length) > 33
order by fish_type