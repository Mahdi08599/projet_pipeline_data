
  create or replace   view BOURSE_DB.GOLD.stg_stock_data
  
   as (
    SELECT 
    TICKER as stock_symbol,   
    PRICE as current_price,
    TIMESTAMP as recorded_at
FROM BOURSE_DB.SILVER.AAPL_DATA
  );

