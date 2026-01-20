WITH cleaned AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY stock_symbol, recorded_at ORDER BY recorded_at DESC) as rank
    FROM {{ ref('stg_stock_data') }}
)
SELECT * FROM cleaned WHERE rank = 1