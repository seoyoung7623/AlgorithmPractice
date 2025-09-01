-- 코드를 작성해주세요
/* 
GENOTYPE 을 2진수로 변환해서 부모와 같은것이 있는 것만 추출 & 로 추출
일단 조인
*/
SELECT a.ID, a.genotype as GENOTYPE, b.genotype as PARENT_GENOTYPE FROM ecoli_data a
join ecoli_data b on a.parent_id = b.id
where (b.genotype & a.genotype) >= b.genotype
order by a.id;