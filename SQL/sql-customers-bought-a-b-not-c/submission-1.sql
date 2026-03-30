-- Write your query below
SELECT customer_id, customer_name FROM customers
WHERE customer_id IN (
    SELECT customer_id FROM (  
        SELECT customer_id,
            max(CASE WHEN product_name = 'A' THEN 1 ELSE 0 END) AS A,
            max(CASE WHEN product_name = 'B' THEN 1 ELSE 0 END) AS B,
            max(CASE WHEN product_name = 'C' THEN 1 ELSE 0 END) AS C
        FROM orders
        GROUP BY customer_id
    )
    WHERE A = 1 AND B = 1 AND C = 0
)
ORDER BY customer_name