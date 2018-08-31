### img2s3

This seriously just uploads images to an S3 bucket. I got tired of logging in to AWS, and the extra clicks to get public 
URLs for uploaded files.

Create a `.env` file in `img2s3/` with the following:
```shell
S3_KEY_ID
S3_ACCESS_SECRET
S3_BUCKET
S3_BUCKET_DIR # optional S3 folder
```