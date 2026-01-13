CONFIG = {
    "enable_s3": True,
    "instances": [
        {"name": "web1", "public": True},
        {"name": "web2", "public": True},
        {"name": "worker", "public": False}
    ]
}