terraform {
  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = ">= 1.0.0"
    }
  }
}

provider "databricks" {
  host  = "https://<your-databricks-instance>.azuredatabricks.net"
  token = "<your-databricks-personal-access-token>"
}

resource "databricks_cluster" "my_cluster" {
  cluster_name = "my-autoscaling-cluster"
  spark_version = "13.2.x-scala2.12"
  node_type_id = "Standard_DS3_v2"

  autoscale {
    min_workers = 2
    max_workers = 5
  }

  autotermination_minutes = 30
}
