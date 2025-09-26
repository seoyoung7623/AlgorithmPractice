-- 코드를 작성해주세요
select b.diff_year as year, b.max_size-a.size_of_colony as year_dev, a.id
from ecoli_data a
join (select year(differentiation_date) as diff_year, max(size_of_colony) as max_size
      from ecoli_data 
    group by year(differentiation_date)) b
on b.diff_year = year(a.differentiation_date)
order by year,year_dev




# (select size_of_colony
#         from ecoli_data
#         group by year(differentiation_date)) - a.size_of_colony)
