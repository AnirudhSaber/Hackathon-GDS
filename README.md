## Hackathon-GDS

#### Technologies used in the solution:
|S.No|TECH|
|:--:|:---|
|1 |Python|
|2 |AWS Glue|
|3 |AWS Kinesis|
|4 |AWS Lambda|
|5 |AWS DynamoDB|

[ARCHITECTURE](https://github.com/AnirudhSaber/Hackathon-GDS/blob/main/pipeline-design.pdf)

#### STEPS TO BE FOLLOWED:
1. Dimension data is loaded into dynamodb table using lambda where SCD's are handled. - If a new file is placed in S3, data will be loaded into dynamodb.
2. Kinesis streams are created for click-stream-data and conversions-stream-data.
3. Lambda is triggered based on the click-stream-event from kinesis, where the De-normalized data is aggregated and loaded into dynamodb table.
4. For the conversions-stream-event, the existing record is retrieved and updated with conversion-data.
5. Real-time metrics can be gatherered from the Dynamodb table using any Dashboard.
6. AWS Glue is used to off-load the data into Redshift on daily baisis (Can be configured as per the cron).
