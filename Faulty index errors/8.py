import unittest
from unittest.mock import patch, mock_open
import json

from your_module import convert_evaluation_datapoints_to_vlm_qa_datapoints
from your_module import EvaluationDatapoint, QADatapoint

question_to_randomized_question_dict = {
    "What color is the car?": ["What is the color of the car?"]
}
question_answer_to_randomized_answer_str = {
    "What color is the car?": {
        "red": ["crimson"]
    }
}

class TestConvertEvaluationDatapoints(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"What color is the car?": "red"}))
    @patch("your_module.random.randint", return_value=0)
    @patch("your_module.question_to_randomized_question_dict", question_to_randomized_question_dict)
    @patch("your_module.question_answer_to_randomized_answer_str", question_answer_to_randomized_answer_str)
    def test_basic_conversion(self, mock_randint, mock_open_func):
        eval_dp = EvaluationDatapoint("metadata.json", "image.jpg")
        expected = QADatapoint("image.jpg", [{"Q": "What is the color of the car?", "A": "crimson"}])
        
        result = convert_evaluation_datapoints_to_vlm_qa_datapoints([eval_dp])
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], expected)

if __name__ == "__main__":
    unittest.main()
