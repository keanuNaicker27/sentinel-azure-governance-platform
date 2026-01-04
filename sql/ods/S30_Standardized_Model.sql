CREATE VIEW [S30].[Fact_GeneralLedger] AS
SELECT 
    gle.[entry_no] AS [TransactionId],
    gle.[posting_date] AS [Date],
    gle.[g_l_account_no] AS [AccountCode],
    gle.[amount] AS [Amount],
    -- Integrate RGS Mapping from the Datahub layer
    rgs.[RGS_Code],
    rgs.[RGS_Description],
    -- Flag for Continuous Auditor: Only send if mapped
    CASE WHEN rgs.[RGS_Code] IS NOT NULL THEN 1 ELSE 0 END AS [IsAuditReady]
FROM [S20].[BC_GLEntry] gle
LEFT JOIN [Datahub].[Mapping] rgs 
    ON gle.[g_l_account_no] = rgs.[SourceAccountCode];
