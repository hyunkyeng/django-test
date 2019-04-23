# from django.test import TestCase
from test_plus.test import TestCase
from django.conf import settings
from .models import Board

# 1. settings test
class SettingsTest(TestCase):
    def test_01_settings(self):
        self.assertEqual(settings.USE_I18N, True)
        self.assertEqual(settings.USE_TZ, False)
        self.assertEqual(settings.LANGUAGE_CODE, 'ko-kr')
        self.assertEqual(settings.TIME_ZONE, 'Asia/Seoul')
        
# 2. Model test
class BoardModelTest(TestCase):
    def test_01_model(self):
        # board = Board.objects.create(title='test title', content='test content')
        board = Board.objects.create(title='test title', content='test content', user_id=1)
        self.assertEqual(str(board), f'Board{board.pk}', msg='출력 값이 일치하지 않음')
    
# 3. View test
class BoardViewTest(TestCase):
    # create test 에서의 포인트는 form 을 제대로 주느냐이다.
    # 가장 기본은 get_check_200
    def test_01_get_create(self):
        self.get_check_200('boards:create')
        self.assertContains(response, '<form')