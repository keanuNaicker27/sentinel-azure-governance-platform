CREATE PROCEDURE [S40].[usp_GetAuditorPayload]
    @AdministrationId NVARCHAR(50),
    @FiscalYear INT
AS
BEGIN
    SET NOCOUNT ON;

    -- Aggregate results as required by the Solution Design
    SELECT 
        @AdministrationId AS [AdministrationId],
        YEAR([Date]) AS [FiscalYear],
        COUNT([TransactionId]) AS [TransactionCount],
        SUM([Amount]) AS [TotalResult],
        MAX([LoadDate]) AS [LastValidatedRefresh]
    FROM [S30].[Fact_GeneralLedger]
    WHERE YEAR([Date]) = @FiscalYear
      AND [IsAuditReady] = 1
    GROUP BY YEAR([Date]);

    -- Trigger the success flag for Sentinel/Webhooks
    EXEC [Sentinel].[usp_LogSuccessfulValidation] @AdministrationId, 'S40_READY';
END
