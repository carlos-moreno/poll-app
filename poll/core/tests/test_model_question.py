import datetime

from django.test import TestCase
from django.utils import timezone

from poll.core.models import Question


class QuestionTest(TestCase):
    def setUp(self) -> None:
        self.question = Question.objects.create(
            question_text="What's up?",
            pub_date=timezone.now()
        )

    def test_str(self):
        self.assertEqual("What's up?", str(self.question))

    def test_was_published_recently(self):
        was_published_recently = timezone.now() - datetime.timedelta(days=1)
        self.assertGreaterEqual(self.question.pub_date, was_published_recently)
