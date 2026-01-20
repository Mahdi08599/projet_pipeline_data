{{ config(materialized='table') }} 

WITH stock_history AS (
    SELECT 
        stock_symbol,      
        current_price,     
        recorded_at,
        LAG(current_price) OVER (PARTITION BY stock_symbol ORDER BY recorded_at) as previous_price
    FROM {{ ref('int_stock_cleansed') }}
)
SELECT 
    *,
    ((current_price - previous_price) / NULLIF(previous_price, 0)) * 100 as price_variation_pct
FROM stock_history