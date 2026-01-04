# The "Brain" Identity - Used by Sentinel Engine
resource "azurerm_user_assigned_identity" "sentinel_identity" {
  name                = "id-sentinel-engine"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
}

# Grant Sentinel Key Vault Secrets User (Least Privilege)
resource "azurerm_role_assignment" "kv_secrets_reader" {
  scope                = azurerm_key_vault.main.id
  role_definition_name = "Key Vault Secrets User"
  principal_id         = azurerm_user_assigned_identity.sentinel_identity.principal_id
}

# Grant Sentinel SQL Contributor for S10-S50 processing
resource "azurerm_role_assignment" "sql_data_contributor" {
  scope                = azurerm_mssql_database.sentinel_db.id
  role_definition_name = "SQL DB Contributor"
  principal_id         = azurerm_user_assigned_identity.sentinel_identity.principal_id
}
