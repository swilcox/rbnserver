import uuid
from django.db import models


class Spot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ts = models.DateTimeField(db_index=True)
    receiving_station = models.CharField(db_index=True)
    calling_station = models.CharField(db_index=True)
    frequency = models.DecimalField(max_digits=10, decimal_places=2)
    mode = models.CharField(db_index=True)
    snr_db = models.IntegerField()
    wpm = models.IntegerField()
    msg = models.CharField()
    rbn_ts = models.DateTimeField(db_index=True)

    class Meta:
        ordering = ["-ts"]

    def __str__(self) -> str:
        return (
            f"[{self.ts.isoformat()}] {self.receiving_station} {self.calling_station}"
        )
