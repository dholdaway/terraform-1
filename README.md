# terraform
This repo defines the pip module for automating the installation, and running of terraform. 

## Install module 
The module can be installed with the following command: 
```commandline
pip install git+https://github.com/OasisLMF/terraform
```

## Install terraform 
Terraform can be installed on a linux system with the command below:
```commandline
terra-install
```
This will get the latest version of terraform, install in, and add it to your command line profile. It will also 
remove the zip file it downloaded to install terraform.

## Creating infrastructure 
In order to create infrastructure, we need a config file. The config file has to be named ```terra_config.yml```
in the working directory of where we are running the command. Our ```terra_config.yml``` file can take the following 
structure:
```yaml
location: eu_west_1
variables:
    aws_access_key: test_key
    aws_secret_access_key: test_secret_key
    subnet_id: test_subnet_id
    state_bucket: test_bucket
    state_key: test_bucket
```
The ```location``` is where the terraform project is located in the root of the module. For instance, this terraform 
project is rooted in the ```command_engine/eu_west_1``` directory in this repo. The ```variables``` are then 
passed into the terraform program that is being run. To run the terraform program run the command below:
```commandline
terra-apply
```

## Deleting infrastructure 
If you need to delete the infrastructure of a project, we will need a ```terra_config.yml``` in the directory of where 
we are running the command. This can be seen in the creating infrastructure section. We can then delete the 
project from the cloud with the command below:
```commandline
terra-destroy
```
