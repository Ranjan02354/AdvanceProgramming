class ScoreProcessor:

    def process_score_file(self, file_path: str) -> int:

        try:
            with open(file_path, "r") as file:
                score = int(file.read().strip())

        except FileNotFoundError:
            print("Error: File not found.")
            raise

        except ValueError:
            print("Error: Invalid number format in file.")
            raise

        else:
            print("Data processed successfully")
            return score * 10

        finally:
            print("File cleanup completed")


if __name__ == "__main__":

    processor = ScoreProcessor()

    file_name = input("Enter file name: ")

    try:
        result = processor.process_score_file(file_name)
        print("Final Result:", result)

    except Exception:
        print("Program ended due to an error.")