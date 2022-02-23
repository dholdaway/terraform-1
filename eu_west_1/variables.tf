

variable "aws_access_key" {
  description = "Access key for AWS access"
  type        = string
  sensitive   = true
}

variable "aws_secret_access_key" {
  description = "Secret access key for AWS access"
  type        = string
  sensitive   = true
}

variable "vpc_id" {
  description = "ID of the VPC that we are building EC2 instances in"
  type        = number
  sensitive   = true
}