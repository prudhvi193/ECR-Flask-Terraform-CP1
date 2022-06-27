output "alb_dns_name" {
    description = "The Application Load Balancer DNS Name"
    value = aws_lb.main.*.dns_name[0]
}
