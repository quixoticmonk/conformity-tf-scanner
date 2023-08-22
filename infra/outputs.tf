output "bucket_arn" {
  value = aws_s3_bucket.bucket_demo.arn
  description = "ARN of the bucket provisioned"
}