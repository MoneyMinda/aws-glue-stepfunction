AWSTemplateFormatVersion: "2010-09-09"

Description: >
  Stack template for creating chicago crime data analysis job

Parameters:
  GlueAssetsBucket:
    Description: "Name of S3 bucket where glue scripts are stored"
    Type: String
  DataBucket:
    Description: "Name of S3 bucket where data is stored"
    Type: String
  EltRole:
    Description: "ARN of role for executing Glue jobs"
    Type: String

Resources:
  GlueJob:
    Type: "AWS::Glue::Job"
    Properties:
      Script: ""
