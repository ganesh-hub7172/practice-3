# Write your MySQL query statement below
WITH ranked AS (
    SELECT
        store_id,
        product_name,
        quantity,
        price,
        ROW_NUMBER() OVER (
            PARTITION BY store_id
            ORDER BY price DESC, inventory_id
        ) AS rn_max,
        ROW_NUMBER() OVER (
            PARTITION BY store_id
            ORDER BY price ASC, inventory_id
        ) AS rn_min,
        COUNT(*) OVER (
            PARTITION BY store_id
        ) AS product_count
    FROM inventory
)

SELECT
    s.store_id,
    s.store_name,
    s.location,
    mx.product_name AS most_exp_product,
    mn.product_name AS cheapest_product,
    ROUND(mn.quantity / mx.quantity, 2) AS imbalance_ratio
FROM stores s
JOIN ranked mx
    ON s.store_id = mx.store_id
   AND mx.rn_max = 1
JOIN ranked mn
    ON s.store_id = mn.store_id
   AND mn.rn_min = 1
WHERE mx.product_count >= 3
  AND mx.quantity < mn.quantity
ORDER BY imbalance_ratio DESC,
         s.store_name ASC;