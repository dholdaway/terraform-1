

provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_access_key
  region     = "eu-west-1"
}

terraform {
    backend "s3" {
    bucket = var.state_bucket
    key    = var.state_key
    region = "eu-west-1"
  }
}


resource "aws_network_interface" "network_interface" {
  subnet_id   = var.vpc_id
#   private_ips = ["172.16.10.100"]

  tags = {
    Name = "primary_network_interface"
  }
}

resource "aws_instance" "test_instance" {
  ami           = "ami-08ca3fed11864d6bb"
  instance_type = "t2.medium"
  key_name = "test_terraform"

  network_interface {
    network_interface_id = aws_network_interface.network_interface.id
    device_index         = 0
  }

  user_data = file("server_build.sh")
}


# # creates the EBS volume 
# resource "aws_ebs_volume" "ebs_volume" {
#   availability_zone = aws_instance.myin2.availability_zone
#   size = 10
#   tags = {
#     Name = "cerberus dev EBS"
#   }
# }

# # attach the volume to the EC2 instance 
# resource "aws_volume_attachment" "ebs_att" {
#   device_name = "/dev/sdd"
#   volume_id = aws_ebs_volume.ebs_volume.id
#   instance_id = aws_instance.auth-dev-server.id
#   force_detach = true
# } 

# # return the IP of the server created
# output "ec2_global_ips" {
#   value = ["${aws_instance.auth-dev-server.*.public_ip}"]
# }