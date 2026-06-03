SELECT product_id, COUNT(*) AS supplier_count
FROM product_suppliers
GROUP BY product_id;
