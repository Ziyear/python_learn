from django.test import TestCase

# Create your tests here.
from django.utils import timezone as datetime

from test2.booktest.models import *

create = BookInfo.create("倚天屠龙记", datetime.now())
create.save()
