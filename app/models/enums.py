import enum

class UserRole(str,enum.Enum):
    ADMIN = "admin"
    USER = "user"
    STAFF = "staff"

class UserTypeEnum(str,enum.Enum):
    student = "student"
    teacher = "teacher"

