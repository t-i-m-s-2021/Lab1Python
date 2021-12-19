from homework9 import delete_duplicates, count_chars, check_molecules


class TestHomework:
    def test_delete_duplicates(self):
        test_data = [5, 5, 5, 4, 3, 8, 1, 1, 2, 3]
        assert delete_duplicates(test_data) == [1, 2, 3, 4, 5, 8]

    def test_count_chars(self):
        test_result_data = {"Б": 2, "а": 3, "н": 2, "з": 1, "у": 1, "к": 1, "А": 1}
        assert count_chars("БананБазукА") == test_result_data

    def test_check_molecules(self):
        # Доработали функцию: пишет в файл "Impossible", если невозможно составить молекулу
        with open(file="input.txt", mode="w", encoding="UTF-8") as f:
            f.write("1 1 1")
        check_molecules()
        with open(file="output.txt", mode="r", encoding="UTF-8") as f:
            assert "Impossible" == f.readline()
