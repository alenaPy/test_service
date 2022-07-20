# Solution description

![alt text](https://github.com/alenaPy/test_service/blob/main/schema.png?raw=true)

API Gateway provides all necessary facilities for REST API creation, configuring, and securing. In addition, caching could be enabled to reduce the amount of lambda function calls.
The next step is to add authorization. API Keys are enabled for now. If we have a lot of users, the best option is AWS Cognito as it is convenient to use and cheaper than other providers.

### Scalability

The serverless application offers more scalability and flexibility as it isn’t needed to worry about managing and purchasing backend servers. Also, we pay only for the resources we use. However, AWS Lambda has some limitations which should be taken into account: disk space, memory range, execution time, request and response body payload size 
DynamoDB can be expensive for fast-growing data sets. Also, DynamoDB isn’t a good choice for multi-regional apps.

### Performance
Serverless solutions are usually performant due to concurrency and parallelization. Also, it is possible to improve Lambda throughput by enabling Provisioned Concurrency.

### Cost
- DynamoDB charges per GB of disk space a table consumes. The first 25 GB consumed per month is free, and prices start at $0.25 per GB-month thereafter. AWS calculates the cost of writes using “Write Capacity Units.” Each WCU provides up to one write per second, enough for 2.6 million writes per month. The first 25 WCUs per month are free. AWS calculates the cost of reads using “Read Capacity Units.” Each RCU provides up to two reads per second, enough for 5.2 million reads per month. The first 25 RCUs per month are free. The announcement item is tiny, and the writes/reads amount unlikely exceeds the limits.
- Lambda cost is also quite low as memory consumption and time of execution are minor.
- The API Gateway free tier includes one million HTTP API calls, one million REST API calls, one million messages, and 750,000 connection minutes per month or up to 12 months. Also, as an option, it is possible to reduce costs by switching to HTTP API
- AWS Cognito: 50000 monthly active users (MAUs) for free.

### Monitoring
As we don’t have a huge amount of logs, it would be reasonable to configure metrics in CloudWatch and create several Alarms (free tier - 10 Alarm metrics)
