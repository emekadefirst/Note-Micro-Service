from tortoise import Model, fields
import uuid
from tortoise import timezone

class Note(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4, editable=False)
    title = fields.CharField(150, null=True)
    body = fields.TextField(null=True)
    user_id = fields.UUIDField()
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True)
    is_deleted = fields.BooleanField(default=False)

    class Meta:
        table = "notes"
        ordering  = ["-created_at", "-updated_at"]

    async def save(self, using_db = None, update_fields = None, force_create = False, force_update = False):
        if self.id:
            self.updated_at = timezone.now()
        return await super().save(using_db, update_fields, force_create, force_update)
