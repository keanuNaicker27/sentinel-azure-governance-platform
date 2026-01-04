CREATE TABLE [S20].[BC_GLEntry] (
    [S20_Id] INT IDENTITY(1,1) PRIMARY KEY,
    [entry_no] INT NOT NULL,
    [posting_date] DATE NOT NULL,
    [g_l_account_no] NVARCHAR(20),
    [amount] DECIMAL(18,2),
    [HashKey] AS HASHBYTES('SHA2_256', CONCAT([entry_no], [amount], [posting_date])),
    [LoadDate] DATETIME2 DEFAULT GETDATE()
);

-- Index for Sentinel 'Smart Refresh' performance
CREATE INDEX IX_S20_BC_GLEntry_PostingDate ON [S20].[BC_GLEntry]([posting_date]);
