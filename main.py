import base64
import json
import os


class SkidChecker:
    def __init__(self, data: dict) -> None:
        self.data = data

    def _is_correct(self, _input: str, answer: str) -> bool:
        return base64.b64decode(answer.encode()).decode() in _input

    def main(self) -> None:
        for hitler in self.data:
            question = hitler["question"]
            answer = hitler["answer"]

            print(question)
            my_input = input("[>] ")

            if self._is_correct(my_input, answer):
                print("correct\n")
            else:
                print("incorrect\n")


if __name__ == "__main__":
    checker = SkidChecker(json.load(open("data.json", "r")))
    checker.main()

    print("\nDone")
    os.system("pause >nul")
