from tortoise import fields, Model
from tortoise import timezone
import uuid



class User(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4, editable=False)
    first_name = fields.CharField(50)
    last_name = fields.CharField(50)
    email = fields.CharField(100, unique=True)
    password = fields.CharField(150)
    is_admin = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True)
    is_deleted = fields.BooleanField(default=False)
    permission_groups = fields.JSONField(null=True)

    class Meta:
        table = "users"
        ordering  = ["-created_at", "-updated_at"]

    async def save(self, using_db = None, update_fields = None, force_create = False, force_update = False):
        if self.id:
            self.updated_at = timezone.now()
        return await super().save(using_db, update_fields, force_create, force_update)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"
    
