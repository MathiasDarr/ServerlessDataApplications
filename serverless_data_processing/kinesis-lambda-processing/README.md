### Processing Kinesis Stream With Lambda Function ###

The Cloudformation  application defined in this directory defines the following resources
* Kinesis Stream
* Lambda function 
    - reads the kinesis payload
    - logs the payload
* Eventstream mapping 

docker-compose -f localstack-compose.yaml up --build 

## How to deploy the application? ## 
* This application has the following dependencies
    * awscli
    * python3
    * boto3  
    * aws SAM (Even though at the moment I'm just using standard cloudformation)
    * docker-compose & docker (if running locally)
    * pytest (for running the test suite)
* Run the localstack environment (from the root directory)
    * docker-compose -f localstack-compose.yaml up --build

### package & build the SAM template to local ###
* bash deploy.sh local (deploying locally)
* bash deploy.sh aws (deploying to the cloud)


### Write to kinesis stream using boto3, triggering lambda function ###
* python3 write_to_kinesis_stream.py local/aws 

### Accessing lambda logs from CLI  ###
* bash scripts/get_most_recent_logstream.sh local 


### test the application ### 
* bash deploy.sh local
* pytest