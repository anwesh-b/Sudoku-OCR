output "function_name" {
  value = azurerm_function_app.funcdeploy.name
}

output "function_url" {
  value = azurerm_function_app.funcdeploy.default_hostname
}

output "function_resource_group" {
  value = azurerm_resource_group.funcdeploy.name
}
