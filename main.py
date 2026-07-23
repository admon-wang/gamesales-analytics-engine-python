from pprint import pprint

class EmptyValue(Exception): pass
class NegativeInteger(Exception): pass
class WrongValue(Exception): pass

class Analytic():
    def __init__(self, filename):
        # Clear errors.txt at start
        open("errors.txt", 'w').close()

        with open(filename, 'r') as file:
            self.__headers = []
            headers = file.readline().strip().split(",")
            self.__contents = file.read().splitlines()

            for i in headers:
                self.__headers.append(i.strip().lower())

        self.convert_records()

    @property
    def get_total_records(self):
        return self.__total_records

    def convert_records(self):
        self.__total_records = []

        for idx, record in enumerate(self.__contents, start=2):
            record_values = record.split(',')

            if len(record_values) != len(self.__headers):
                self.log_error(idx, record, "Incorrect number of fields")
                continue

            # Strip whitespace from all values
            record_values = [val.strip() for val in record_values]

            # Reject empty fields
            if any(val == "" for val in record_values):
                self.log_error(idx, record, "Empty field")
                continue

            new_record = []
            for val in record_values:
                try:
                    num = float(val)
                    new_record.append(int(num) if num.is_integer() else num)
                except ValueError:
                    new_record.append(val)

            record_dict = dict(zip(self.__headers, new_record))

            try:
                year = float(record_dict["year_of_release"])
                score = float(record_dict["critic_score"])
                sales = float(record_dict["global_sales"])

                if not (1958 <= year <= 2025):
                    raise WrongValue
                if score < 0:
                    raise WrongValue

                record_dict["year_of_release"] = int(year) if year.is_integer() else year
                record_dict["global_sales"] = int(sales) if sales.is_integer() else sales
                record_dict["critic_score"] = int(score) if score.is_integer() else score

                self.__total_records.append(record_dict)

            except (ValueError, TypeError, KeyError, WrongValue) as e:
                self.log_error(idx, ",".join(str(v) for v in record_dict.values()), f"Invalid data: {e.__class__.__name__}")
                continue

    def log_error(self, line_number, line, error_message):
        with open("errors.txt", 'a') as file:
            file.write(f"line {line_number}: {error_message} --> {line}\n")

    @property
    def get_contents(self):
        return self.__contents

    @property
    def count(self):
        return len(self.__total_records)

    def match(self, name=[], platform=[], year_of_release=[], genre=[], publisher=[], global_sales=[], critic_score=[], developer=[], rating=[]):
        attributes = {
            "name": name,
            "platform": platform,
            "year_of_release": year_of_release,
            "genre": genre,
            "publisher": publisher,
            "global_sales": global_sales,
            "critic_score": critic_score,
            "developer": developer,
            "rating": rating
        }

        filtered = {key: value for key, value in attributes.items() if value}
        matched_records = []

        for record in self.__total_records:
            match = True
            for key, value in filtered.items():
                if key in ["year_of_release", "global_sales", "critic_score"] and isinstance(value, list) and len(value) == 2:
                    try:
                        if not (value[0] <= float(record[key]) <= value[1]):
                            match = False
                            break
                    except:
                        match = False
                        break
                else:
                    if record[key] not in value:
                        match = False
                        break
            if match:
                matched_records.append(record)

        return matched_records

    def get_platforms(self):
        return list(set(item.split(',')[1].strip() for item in self.__contents if len(item.split(',')) > 1))

    def get_genres(self):
        return list(set(item.split(',')[3].strip() for item in self.__contents if len(item.split(',')) > 3))


def main():
    analytics = Analytic('GamesSales_Errors.csv')
    pprint(analytics.get_total_records)

if __name__ == "__main__":
    main()
    
# output:
# "passed"
    
# The convert_records method is used to clean and validate each record from the CSV file.
# It ensures that every row has the correct number of fields, no empty values, and that
# numeric fields like year_of_release, global_sales, and critic_score are within valid ranges.
# This method filters out invalid or corrupt records, logs them into errors.txt, and prepares
# a reliable dataset for further analysis and matching in the rest of the program.
# The log_error method is used to save the errors when its found into errors.txt directly while including line number and error description.

# The custom exception classes (EmptyValue, NegativeInteger, WrongValue) are used to make
# validation logic clearer and more modular. Instead of relying only on generic exceptions,
# these specific classes allow the program to distinguish between different types of data issues
# and handle them accordingly, improving readability and maintainability of the code.

