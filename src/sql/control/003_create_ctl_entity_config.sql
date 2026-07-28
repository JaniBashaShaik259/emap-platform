
INSERT INTO ctl_entity_config (
    source_id,
    entity_type,
    entity_code,
    entity_name,
    entity_group,
    exchange_code,
    is_active,
    created_date,
    created_by
) VALUES 
(1, 'Stock', 'AAPL', 'Apple Inc.', 'US_Equities', 'NASDAQ', 1, current_timestamp(), 'SparkSQL_User'),
(1, 'Stock', 'MSFT', 'Microsoft Corporation', 'US_Equities', 'NASDAQ', 1, current_timestamp(), 'SparkSQL_User'),
(1, 'Stock', 'NVDA', 'NVIDIA Corporation', 'US_Equities', 'NASDAQ', 1, current_timestamp(), 'SparkSQL_User'),
(1, 'Crypto', 'BTC-USD', 'Bitcoin USD', 'Cryptocurrency', 'CCY', 1, current_timestamp(), 'SparkSQL_User');
