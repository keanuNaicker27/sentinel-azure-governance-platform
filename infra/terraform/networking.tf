# Virtual Network for Data Isolation
resource "azurerm_virtual_network" "sentinel_vnet" {
  name                = "vnet-sentinel-prod"
  address_space       = ["10.0.0.0/16"]
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
}

# Subnet for Data Services (SQL & Private Link)
resource "azurerm_subnet" "data_subnet" {
  name                 = "snet-data-services"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.sentinel_vnet.name
  address_prefixes     = ["10.0.1.0/24"]
  
  enforce_private_link_endpoint_network_policies = true
}

# Private Endpoint for Azure SQL (Ensures no public IP access)
resource "azurerm_private_endpoint" "sql_endpoint" {
  name                = "pe-sentinel-sql"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
  subnet_id           = azurerm_subnet.data_subnet.id

  private_service_connection {
    name                           = "sql-privatelink"
    private_connection_resource_id = azurerm_mssql_server.sql_server.id
    subresource_names              = ["sqlServer"]
    is_manual_connection           = false
  }
}
