from django.test import TestCase
from polls.models import Question
from django.utils import timezone

# Create your tests here.


class QuestionModelTest(TestCase):
    def test_create_question(self):
        count = Question.objects.count()
        Question.objects.create(question_text="Test question", pub_date=timezone.now())
        self.assertEqual(Question.objects.count(), count + 1)

    def test_dummy(self):
        self.assertTrue(False)
