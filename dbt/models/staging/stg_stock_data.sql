SELECT 
    TICKER as stock_symbol,   
    PRICE as current_price,
    TIMESTAMP as recorded_at
FROM {{ source('raw_data', 'AAPL_DATA') }}