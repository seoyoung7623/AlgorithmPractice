-- 코드를 작성해주세요
/*
기준점수 별로 등급이 나워지고 등급별로 성과금이 추가됨
*/
with grade_table as(
    select gr.emp_no, 
        case
            when avg(gr.score) >= 96 then 'S'
            when avg(gr.score) >= 90 then 'A'
            when avg(gr.score) >= 80 then 'B'
            else 'C'
        end as GRADE
    from hr_grade gr
    group by gr.emp_no
)

select em.EMP_NO, em.EMP_NAME, gr.GRADE,
    case 
        when gr.GRADE = 'S' then em.sal * 0.2
        when gr.GRADE = 'A' then em.sal * 0.15
        when gr.GRADE = 'B' then em.sal * 0.1
        else 0
    end as BONUS
from hr_employees em
join grade_table gr on gr.emp_no = em.emp_no
order by em.emp_no