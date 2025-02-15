class SSCCGLMarks:
    @staticmethod
    def calculate_marks(correct: int, wrong: int, not_attempted: int):
        correct_marks = correct * 2  # ✅ Each correct answer gives 2 marks
        wrong_marks = wrong * 0.5  # ❌ Each wrong answer deducts 0.5 marks
        unattempted_marks = 0  # ⚪ No marks for unattempted questions
        return correct_marks - wrong_marks + unattempted_marks  # ✅ Total marks for section

    @staticmethod
    def calculate_MTS_total_marks(correct: int, wrong: int, not_attempted: int):
        correct_marks = correct * 1  # ✅ Each correct answer gives 2 marks
        wrong_marks = wrong * 0.25  # ❌ Each wrong answer deducts 0.5 marks
        unattempted_marks = 0  # ⚪ No marks for unattempted questions
        return correct_marks - wrong_marks + unattempted_marks  # ✅ Total marks for section
