
- [Introduction](#introduction)
- [Project description](#project-description)
- [Step 1 - Project set up \& data cleaning](#step-1---project-set-up--data-cleaning)
- [Step 2 - Postgres DB in AWS RDS](#step-2---postgres-db-in-aws-rds)
- [Step 3 - How to interact with S3](#step-3---how-to-interact-with-s3)
- [Step 4 - Export RDS to S3 + Create Dimensional Model](#step-4---export-rds-to-s3--create-dimensional-model)
- [Step 5 - Understand AWS Glue](#step-5---understand-aws-glue)
- [Step 6 - Create redshift cluster](#step-6---create-redshift-cluster)
- [Step 7 - ETL Pipeline from S3 to Redshift](#step-7---etl-pipeline-from-s3-to-redshift)


## Introduction

The main objective of the project is to explore and understand the different services provided by Amazon Web Services (AWS) and how they interact with each other. This is achieved through the implementation of a comprehensive workflow for data management. The project begins with diverse .csv files containing information about books, users, and ratings. The focus lies on the complete process, starting from the initial data cleaning and structuring to migrating and modeling in an optimal cloud-based analysis environment. Combining services such as Amazon RDS, S3, Redshift, and AWS Glue enables effective data management, transformation, and integration, facilitating advanced analysis for informed decision-making.

## Project description

## Step 1 - Project set up & data cleaning

In the project's initial phase, I've curated the datasets sourced from Kaggle for use. Subsequently, I've established the Python project structure, encompassing essential scripts for data cleansing, PostgreSQL ingestion, and seamless interaction with AWS S3.

## Step 2 - Postgres DB in AWS RDS

The second stage involves data ingestion into the PostgreSQL database. Initially, it's necessary to create the database on Amazon RDS. Once the database is created, we can ingest our three meticulously cleaned datasets (users, books, ratings) seamlessly. This can be achieved using either a PostgreSQL administrator or the psycopg2 library in Python. In my case, I choose the latter option, although I will also use the administrator to verify the data ingestion.

## Step 3 - How to interact with S3

The third stage, prior to exporting the data from RDS to S3, involved understanding interactions with S3. To accomplish this, I utilized the Python library boto3 and conducted several tests to comprehend creating an AWS session, generating a bucket, viewing its contents, and importing files from my local environment.

## Step 4 - Export RDS to S3 + Create Dimensional Model

Having understood the functionality of S3, it's now time to export our data from RDS. Once again, there are two options: using Boto3 or the Data Migration Service. I will continue to utilize the Python library for this purpose, although I will also explore the second method.

## Step 5 - Understand AWS Glue

The next stage involves understanding what Glue is and the various components involved in the workflow:

- **Data Catalog:** It's a central metadata repository in AWS Glue where information about datasets and their properties is stored, facilitating data discovery and management.
- **Classifier:** These are pre-built or custom classifiers used to categorize or identify the schema of your data (e.g., CSV, JSON) for easier processing.
- **Connection:** It defines the connection properties required to connect to different data sources or targets, such as databases, S3, or JDBC connections.
- **Crawler:** A crawler is an automated tool in AWS Glue that scans data sources to infer the schema and structure of the data, enabling the creation of metadata in the Data Catalog.
- **Database & Table:** These are organizational units in the Data Catalog. Databases contain tables, and tables represent the structured data entities.
- **Job:** It's a script or code written in AWS Glue to perform ETL (Extract, Transform, Load) tasks on your data. Jobs define the transformations to be applied to the data.
- **Job Scheduler:** This schedules and manages the execution of AWS Glue jobs based on defined triggers or on a predefined schedule.
- **Trigger:** Triggers are event-based or time-based conditions that initiate the execution of AWS Glue jobs. They can be set to start a job when specific events occur.
- **Data Source and Data Target:** Data Source refers to the source from which data is extracted, while Data Target is the destination where transformed data is loaded after processing.

Understanding these components within AWS Glue is essential for orchestrating and executing ETL processes effectively and efficiently, providing the groundwork for data transformation and integration workflows.

Furthermore, this article '[Introduction to AWS Glue for ETL Data Pipeline from S3, MySQL to AWS Redshift'](https://medium.com/@arlene.r/introduction-to-aws-glue-for-etl-data-pipeline-from-s3-mysql-to-aws-redshift-aad0c89edc26)  has been particularly helpful in deepening my understanding of these Glue components.

## Step 6 - Create redshift cluster

Next, it's time to create the cluster in Redshift, along with the corresponding database and tables for our data modeling. In this instance, we will have four tables: one fact table and three dimensional tables (location, users, books).

## Step 7 - ETL Pipeline from S3 to Redshift

The final stage involves creating an ETL (Extract, Transform, Load) process that transitions from the three tables we have in S3 (users, ratings, and books) to the four tables defined in our model and created in Redshift (fact table + dimensional tables). To achieve this, the initial step is to set up Glue by configuring the crawler, choosing data sources, defining crawlers, configuring security settings, and setting up the output destination.

Subsequently, we will utilize the Visual ETL tool to define all the stages of the pipeline. This involves structuring the sequence of Extract, Transform, and Load tasks necessary to transform and transfer data from the source tables in S3 to the destination tables in Redshift.