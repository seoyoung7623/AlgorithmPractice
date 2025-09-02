/*
vars라는 3개의 숫자가 들어있는 임시테이블 생성
*/
with vars as (
    select 
        (select code from skillcodes where name ='Python') as py, -- 파이썬
        (select code from skillcodes where name = 'C#') as cs, -- C#
        (select SUM(code) from skillcodes where category = 'Front End') as fe -- 모든 프론트 개발자
)

# select
#     case
#         when (d.skill_code & v.fe) > 0 and (d.skill_code & v.py) > 0 then 'A'
#         when (d.skill_code & v.cs) > 0 then 'B'
#         when (d.skill_code & v.fe) > 0 then 'C'
#         else null
#     end as GRADE,
#     d.id,
#     d.email
# from developers d
# cross join vars v
# where
#     (d.skill_code & v.fe) > 0 or (d.skill_code & v.py) > 0 or (d.skill_code & v.cs) > 0
#     # GRADE is not null
# order by GRADE, d.id;
        
select * from (
    select 
    case
        when (d.skill_code & v.fe) > 0 and (d.skill_code & v.py) > 0 then 'A'
        when (d.skill_code & v.cs) > 0 then 'B'
        when (d.skill_code & v.fe) > 0 then 'C'
        else null
    end as GRADE,
    d.id, d.email
    from developers d
    cross join vars v -- 교집합!
) x
where GRADE is not null
order by x.grade, x.id;