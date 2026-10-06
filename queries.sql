SELECT 
    category,
    COUNT(cc_num) AS total_transactions,
    ROUND(SUM(amt), 2) AS total_transaction_volume,
    ROUND(AVG(amt), 2) AS average_transaction_amount
FROM credit_data
GROUP BY category
ORDER BY total_transaction_volume DESC;