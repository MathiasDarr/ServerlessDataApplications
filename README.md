### Serverless Data Applications ###
This repository contains serverless applications.  The applications in this repository are able to be deployed to the AWS cloud as well as locally using localstack.   

* firehose-s3
    - this application   
* kinesis-lambda-processing
    - cloudformation template defines a Kinesis stream a
* sqs-lambda
    - cloudformation template defines an SQS queue and a lambda function that reads the messages.
    
### Running the applications locally ###
* docker-compose -f localstack-compose.yaml up 