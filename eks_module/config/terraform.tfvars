
aws_eks_cluster_config = {

      "demo-cluster" = {

        eks_cluster_name         = "demo-cluster1"
        eks_subnet_ids = ["subnet-05b506108d6449a2e","subnet-054b3837f338379a1","subnet-0545a806e3d76548a","subnet-0ded330f307f93d65"]
        tags = {
             "Name" =  "demo-cluster"
         }  
      }
}

eks_node_group_config = {

  "node1" = {

        eks_cluster_name         = "demo-cluster"
        node_group_name          = "myeksnode"
        nodes_iam_role           = "eks-node-group-general1"
        node_subnet_ids          = ["subnet-05b506108d6449a2e","subnet-054b3837f338379a1","subnet-0545a806e3d76548a","subnet-0ded330f307f93d65"]

        tags = {
             "Name" =  "node1"
         } 
  }
}