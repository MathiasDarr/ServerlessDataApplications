// const axios = require('axios')
// const url = 'http://checkip.amazonaws.com/';
let response;

const AWS = require('aws-sdk');

const dynamoDB = new AWS.DynamoDB({region: 'us-west-2'});



exports.lambdaHandler = async (event, context) => {
    try {
        // const ret = await axios(url);

        var AWS = require('aws-sdk');
        // Set the region 
        AWS.config.update({region: 'us-west-2'});
        
        // Create the DynamoDB service object
        var ddb = new AWS.DynamoDB({apiVersion: '2012-08-10'});
        
        var params = {
          TableName: 'SeaSideTest',
          Item: {
            'category' : {S: 'dd Roe'}
          }
        };
        
        // Call DynamoDB to add the item to the table
        ddb.putItem(params, function(err, data) {
          if (err) {
            console.log("Error", err);
          } else {
            console.log("Success", data);
          }
        });
        




        response = {
            'statusCode': 200,
            'body': JSON.stringify({
                message: "yes",
            })
        }
    } catch (err) {
        console.log(err);
        return err;
    }

    return response
};
