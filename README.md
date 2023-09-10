## Hackathon-GDS
This solution is for the team Striking Gyarados

#### Technologies used in the solution:
|S.No|TECH|
|:--:|:---|
|1   |Python|
|2 |AWS Glue|
|3 |AWS Kinesis|
|4 |AWS Athena|
|5 |SQL|

[ARCHITECTURE](https://github.com/AnirudhSaber/Hackathon-GDS/blob/main/ad-campaign-pipelie.pdf)

#### STEPS TO BE FOLLOWED:
1. Raw data should be generated based on the scenario.
2. Load the dimension data into s3 bucket respectively.
3. Create a new database in Catalog
4. Use crawlers to create the tables for the dimesntions data.
5. For the real time data ingestion. Data should be routed to Kinesis
6. Using Firehose, the batch files per 5 min which is Near Real Time should be generated and dumped into S3 bucket respectively.
7. Schedule the crawlers to read the newly added files into the bucket to create table and read the real time data into catalog tables.
8. Use Athena to build analysis queries.
