-- Write your query below
SELECT student_id, exam_id, score FROM (
    SELECT student_id, exam_id, score,
        rank() OVER(PARTITION BY student_id ORDER BY score DESC, exam_id ASC) as score_rank
    FROM exam_results
)
WHERE score_rank = 1
ORDER BY student_id 