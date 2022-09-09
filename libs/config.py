
class Config:
    class GENERIC:
        SUCCESS = (0, "Success")
        FAILURE = (1, "Oops, Something went wrong!")
        FAILED = (1, "Failed")
        UNAVAILABLE = (1, "This feature is unavailable for sometime will get back soon")
        UNAUTHORIZED = (1, "Unauthorized")
        INVALID_ROLE = (1, "Invalid Role")
        PERMISSION_DENIED = (1, "Permission Denied")