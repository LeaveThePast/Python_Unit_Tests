from Task_1 import geo_id, visits, ads_stats
import pytest

class TestFoo():
    @pytest.mark.parametrize(
        'foo, expected', [
            (geo_id(), [98, 35, 15, 213, 54, 119]),
            (visits(), [{'visit1': ['Москва', 'Россия']},
                        {'visit3': ['Владимир', 'Россия']},
                        {'visit7': ['Тула', 'Россия']},
                        {'visit8': ['Тула', 'Россия']},
                        {'visit9': ['Курск', 'Россия']},
                        {'visit10': ['Архангельск', 'Россия']}]),
            (ads_stats(), 'yandex')
        ]
    )

    def test_foo(self, foo, expected):
        result = foo
        assert result == expected