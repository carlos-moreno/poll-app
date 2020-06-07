from django.test import TestCase
from django.utils import timezone

from poll.core.models import Question, Choice


class ChoiceTest(TestCase):
    def setUp(self) -> None:
        self.question = Question.objects.create(
            question_text="What's up?", pub_date=timezone.now()
        )
        self.choice = Choice.objects.create(
            question=self.question, choice_text="Just hacking again.", votes=0
        )

    def test_str(self):
        self.assertEqual("Just hacking again.", str(self.choice))
