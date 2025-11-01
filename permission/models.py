from tortoise import fields, Model
from auth.authServices.enums import Action, Module
from tortoise import timezone
import uuid

class Permission(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4, editable=False)
    action = fields.CharEnumField(Action)
    module = fields.CharEnumField(Module)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True)
    is_deleted = fields.BooleanField(default=False)

    class Meta:
        table = "permissions"
        ordering  = ["-created_at", "-updated_at"]

    async def save(self, using_db = None, update_fields = None, force_create = False, force_update = False):
        if self.id:
            self.updated_at = timezone.now()
        return await super().save(using_db, update_fields, force_create, force_update)



class PermissionGroup(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4, editable=False)
    title = fields.CharField(55, unique=True)
    permissions = fields.ManyToManyField("models.Permission", related_name="perm_group")
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True)
    is_deleted = fields.BooleanField(default=False)

    class Meta:
        table = "permission_groups"
        indexes = [('title',)]
        ordering  = ["-created_at", "-updated_at"]

    def __str__(self):
        return self.title
    async def save(self, using_db = None, update_fields = None, force_create = False, force_update = False):
        if self.id:
            self.updated_at = timezone.now()
        return await super().save(using_db, update_fields, force_create, force_update)