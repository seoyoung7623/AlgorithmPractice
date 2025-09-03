-- 코드를 작성해주세요
/*
최대 값만 출력하는 방법..?
1등 점수가 한명이 아닐 수 있잖아
*/
select x.score, x.emp_no, x.emp_name, x.position, x.email from (
select sum(gr.score) as SCORE, em.emp_no, em.emp_name, em.position, em.email,
    rank() over (order by sum(gr.score) desc) as rnk
from hr_department de
join hr_employees em on de.dept_id = em.dept_id
join hr_grade gr on gr.emp_no = em.emp_no
group by em.emp_no
) x where x.rnk = 1;
# limit 1;