from datetime import UTC
import uuid
from django.utils.datetime_safe import datetime
from django.test import TestCase
from ..models import Spot


class SpotModelTests(TestCase):
    def test_create_spot(self):
        # validate uuid is created if not supplied
        ts = datetime.now(UTC)
        spot = Spot.objects.create(
            calling_station="KK4SW",
            receiving_station="KW4WL",
            ts=ts,
            wpm=35,
            snr_db=20,
            frequency=7042.5,
            rbn_ts=ts,
            msg="CQ",
            mode="CW",
        )
        self.assertNotEqual(spot.id, None)
        # validate that __str__ representation works
        self.assertEqual(str(spot), f"[{ts.isoformat()}] KW4WL KK4SW")
        # validate uuid can be manually provided
        _uuid = uuid.uuid4()
        spot2 = Spot.objects.create(
            id=_uuid,
            calling_station="KK4SW",
            receiving_station="KW4WL",
            frequency=14076.2,
            ts=ts,
            wpm=35,
            snr_db=20,
            rbn_ts=ts,
            msg="CQ",
            mode="CW",
        )
        self.assertEqual(spot2.id, _uuid)
