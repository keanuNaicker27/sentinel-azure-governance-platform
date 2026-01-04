# Key Vault for D365 Business Central API Secrets
resource "azurerm_key_vault" "main" {
  name                        = "kv-sentinel-prod"
  location                    = var.location
  resource_group_name         = azurerm_resource_group.rg.name
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  sku_name                    = "premium"
  soft_delete_retention_days  = 7
  purge_protection_enabled    = true

  network_acls {
    default_action = "Deny"
    bypass         = "AzureServices"
  }
}

# Azure SQL Server - Hosting S10 through S50 layers
resource "azurerm_mssql_server" "sql_server" {
  name                         = "sql-sentinel-platform"
  resource_group_name          = azurerm_resource_group.rg.name
  location                     = var.location
  version                      = "12.0"
  administrator_login          = var.admin_username
  administrator_login_password = var.admin_password
  
  azuread_administrator {
    login_username = "AzureAD Admin"
    object_id      = data.azurerm_client_config.current.object_id
  }
}

# Observability Hub
resource "azurerm_log_analytics_workspace" "logs" {
  name                = "log-sentinel-observability"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}
