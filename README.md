# Zillow-Data-Analysis-DataEngineering-Project
In this data engineering project, we build and automate a python ETL process that would extract real estate properties data from Zillow Rapid API, loads it unto amazon s3 bucket which then triggers a series of lambda functions which then ultimately transforms the data, converts into a csv file format and load the data into another S3 bucket using Apache Airflow. Apache airflow will utilize an S3KeySensor operator to monitor if the transformed data has been uploaded into the aws S3 bucket before attempting to load the data into an amazon redshift. 
After the data is loaded into aws redshift, then we will connect amazon quicksight to the redshift cluster to then visualize the Zillow (rapid data) data.

# TechStack Used
    - Python
    - Apache Airflow
    - AWS S3
    - AWS Lambda
    - AWS EC2- t2.medium, ubuntu
    - AWS Redshift - ra3.xlplus
    - Zillow RapidAPI

# ArchitectureFlow
![alt text](image.png)

## Steps Followed::
    1. Create EC2 instance - t2.medium, ubuntu
    2. Installing dependencies on ec2 server
        - sudo apt install python3-pip
        - sudo apt install python3-venv
    3. Create virtual environment and activate the environment
        - python3 -m  venv zillowdataanalysis
        - source zillowdataanalysis/bin/activate
    4. Install awscli and apache-airflow
        - pip3 install awscli apache-airflow
        - pip3 install apache-airflow-providers-amazon
    5. Initialize airflow
        - airflow standalone
    6. Login to the airflow UI using the public EC2 IPv4.
    7. Connect the code editor(in this case vscode) to ec2 instance .
        Refer to - https://www.youtube.com/results?search_query=how+to+connect+ec2+instance+to+vscode
    8. Get zillow API from Rapid API hub - https://rapidapi.com/s.mahmoud97/api/zillow56
    9. After connecting VScode to ec2 instance , create folder zillowanalytics.py in airflow/dags     folder
    10. Update zillowanalytics.py by creating following operators :
         - PythonOperator - To extract data from Zillow API
         - BashOperator - To push the output json file to S3 bucket (make sure to provide adequate    function to EC2 server to access S3 bucket)
    11. Create a lambda function to create a copy of raw json record into another s3 bucket.
    12. Create a lambda function to transform the json data to csv and load the into another s3 bucket (Install pre-requisite layers before creating a lambda function)
    13. Create a DAG operator to check whether a csv file is present in S3 bucket or not:
         - S3KeySensor - To check whether csv file is in required S3 bucket or not.(first configure the aws_s3_conn on airflow UI)
    14. Create a redshift cluster.In the redshift cluster create a table schema
        CREATE TABLE IF NOT EXISTS zillowdata(
        bathroom NUMERIC,
        bedroom NUMERIC,
        city VARCHAR(255),
        homeStatus VARCHAR(255),
        livingArea NUMERIC,
        price NUMERIC,
        rentZestimate NUMERIC,
        zipcode INT)
    14. Create following DAG operator to transfer processed file from S3 bucket to redshift cluster.Make sure to update connection parameters on airflow UI .
    15. Add appropriate permission for EC2 to access Redshift cluster.
    16. Make changes to accept Inbound traffic rule in security group of Redshift
    17. Execute the dags from Airflow UI .
    18. Once all the dags are successfully executed , you are see all the data in redshift via
                  select * from zillowdata;
    19. This data in redshift can be used for analysis using PowerBI , Tableau, QuickSight etc.
    

