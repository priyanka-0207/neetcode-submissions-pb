with t1 as (select student_id, exam_id, score, rank() over (partition by student_id order by score desc, exam_id asc) as rnk from exam_results)

select student_id, exam_id, score from t1
where rnk = 1
order by student_id;
