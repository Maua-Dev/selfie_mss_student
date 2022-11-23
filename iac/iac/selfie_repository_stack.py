from aws_cdk import (
    aws_s3, aws_s3_notifications, aws_lambda,
    aws_stepfunctions,
    aws_stepfunctions_tasks,
    aws_events, aws_events_targets,
    aws_cloudfront, aws_cloudfront_origins, RemovalPolicy
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration


class SelfieRepositoryStack(Construct):
    s3_bucket: aws_s3.Bucket
    selfie_validation_step_function: aws_stepfunctions.StateMachine
    cloudfront_distribution: aws_cloudfront.Distribution

    def __init__(self, scope: Construct, construct_id: str, create_selfie_lambda_function: aws_lambda.Function, validate_selfie_lambda_function: aws_lambda.Function, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        self.s3_bucket = aws_s3.Bucket(self, "Selfie_S3_Bucket",
                                       versioned=True,
                                       block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
                                       event_bridge_enabled=True,
                                       cors=[aws_s3.CorsRule(
                                             allowed_methods=[aws_s3.HttpMethods.GET, aws_s3.HttpMethods.PUT, aws_s3.HttpMethods.POST],
                                                allowed_origins=["*"],
                                                allowed_headers=["*"],
                                                max_age=3000
                                            )],
                                       removal_policy=RemovalPolicy.DESTROY
                                       )

        oai = aws_cloudfront.OriginAccessIdentity(self, "Selfie_OAI")

        self.s3_bucket.grant_read(oai)

        self.cloudfront_distribution = aws_cloudfront.Distribution(self, "Selfie_CloudFront_Distribution",
                                                                                default_behavior=aws_cloudfront.BehaviorOptions(
                                                                                    origin=aws_cloudfront_origins.S3Origin(
                                                                                        self.s3_bucket,
                                                                                        origin_access_identity=oai),
                                                                                    origin_request_policy=aws_cloudfront.OriginRequestPolicy.CORS_S3_ORIGIN,
                                                                                    viewer_protocol_policy=aws_cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                                                                                    response_headers_policy=aws_cloudfront.ResponseHeadersPolicy.CORS_ALLOW_ALL_ORIGINS,
                                                                                    cache_policy=aws_cloudfront.CachePolicy.CACHING_OPTIMIZED,
                                                                                    allowed_methods=aws_cloudfront.AllowedMethods.ALLOW_ALL
                                                                                )
        )


        get_image_metadata_task = aws_stepfunctions_tasks.CallAwsService(self, "Get Image Metadata",
                                                                         service="s3",
                                                                         action="headObject",
                                                                         iam_resources=[self.s3_bucket.arn_for_objects("*")],
                                                                         parameters={
                                                                             "Bucket": self.s3_bucket.bucket_name,
                                                                             "Key": aws_stepfunctions.JsonPath.string_at(
                                                                                 '$.detail.object.key'),
                                                                         },
                                                                         result_path="$.bucketMetadataResult"
                                                                         )

        detect_labels_task = aws_stepfunctions_tasks.CallAwsService(self, "Get Image",
                                                                    service="rekognition",
                                                                    action="detectLabels",
                                                                    iam_resources=["*"],
                                                                    parameters={
                                                                        "Image": {
                                                                            "S3Object": {
                                                                                "Bucket": self.s3_bucket.bucket_name,
                                                                                "Name": aws_stepfunctions.JsonPath.string_at(
                                                                                    '$.detail.object.key')
                                                                            }
                                                                        }
                                                                    },
                                                                    result_path="$.rekognitionResult"
                                                                    )

        validate_selfie_task = aws_stepfunctions_tasks.LambdaInvoke(self, "Validate Selfie",
                                                                    lambda_function=validate_selfie_lambda_function,
                                                                    result_path="$.validateSelfieResult"
                                                                    )

        create_selfie_task = aws_stepfunctions_tasks.LambdaInvoke(self, "Create Selfie",
                                                                    lambda_function=create_selfie_lambda_function,
                                                                    input_path="$.validateSelfieResult.Payload",
                                                                    result_path="$.createSelfieResult"
                                                                  )

        self.selfie_validation_step_function = aws_stepfunctions.StateMachine(self, "Selfie_Validation_Step_Function",
                                                                              definition=get_image_metadata_task.next(
                                                                                  detect_labels_task).next(
                                                                                    validate_selfie_task).next(
                                                                                    create_selfie_task)
                                                                              )

        self.s3_bucket.grant_read(self.selfie_validation_step_function.role)

        # self.event_bridge_bus = aws_events.EventBus(self, "Selfie_Event_Bus",
        #                                             event_bus_name="Selfie_Event_Bus"
        #                                             )

        self.upload_file_to_s3_event_rule = aws_events.Rule(self, "Upload_File_To_S3_Event_Rule",
                                                            # event_bus=self.event_bridge_bus,
                                                            event_pattern=aws_events.EventPattern(
                                                                source=["aws.s3"],
                                                                detail_type=["Object Created"],
                                                                detail={
                                                                    "bucket": {
                                                                        "name": [self.s3_bucket.bucket_name]
                                                                    }
                                                                }
                                                            ),
                                                            targets=[
                                                                aws_events_targets.SfnStateMachine(self.selfie_validation_step_function)

                                                            ]
                                                            )





        # self.s3_bucket.add_event_notification(event=aws_s3.EventType.OBJECT_CREATED, dest=aws_s3_notifications.)
