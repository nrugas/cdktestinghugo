from aws_cdk import (
    core, aws_s3 as s3)


class StaticSiteStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self, "staticsitebucket", bucket_name="cdkstatictut2020", public_read_access=True, website_index_document="index.html")
        core.CfnOutput(self, "sitebucketname", value=bucket.bucket_name)
        core.CfnOutput(self, "siteBucketWebsite", value=bucket.bucket_website_url)



