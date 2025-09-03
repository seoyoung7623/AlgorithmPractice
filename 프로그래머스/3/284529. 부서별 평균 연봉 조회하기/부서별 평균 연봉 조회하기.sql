-- 코드를 작성해주세요
select de.DEPT_ID, de.dept_name_en, round(AVG(em.sal)) as AVG_SAL
from hr_department de
join hr_employees em on de.dept_id = em.dept_id
group by de.dept_id
order by AVG_SAL desc