# Video Game Sales Analytics Toolkit 🎮

Hi there! I'm a Computer Science student at the University of Wollongong, and this project was part of my Object-Oriented Design and Programming (CSIT121) coursework. I built this tool to practice building robust, object-oriented systems in Python that can handle real-world data processing challenges.

## The Problem & Goal
Working with raw datasets (like video game sales metrics) often comes with "messy" data: missing fields, incorrect types, or unrealistic values. The goal of this project was to design an analytic tool that can ingest CSV data, perform strict data validation to filter out incorrect records, and provide a flexible interface to query and filter the remaining clean data.

## How It Works
This toolkit is built around a single, powerful `Analytic` class that encapsulates the data model and the logic for processing and searching.

*   **Data Ingestion & Validation (`__init__` & `convert_records`)**: When you give it a file, it reads the data row-by-row. If a row is missing information or contains invalid numeric data (e.g., a release year outside of a logical range), it doesn't crash! Instead, it logs the error into `errors.txt` with the exact line number, keeping the application stable.
*   **Encapsulation**: Using private variables (`__total_records`, `__headers`) and methods ensures that the internal state of the analyzer remains protected and consistent, a key principle of good Object-Oriented Design.
*   **Flexible Searching (`match`)**: The `match` method allows for complex, multi-attribute filtering. Whether you are looking for specific platforms or a range of release years, you can chain these requirements together using a simple, readable query syntax.

## Getting Started
To run this tool locally, make sure you have [Python](https://www.python.org/) installed, and simply execute your script via the terminal:

```bash
# Clone this repository and navigate to the project directory
# Run the analysis tool with one of the provided datasets:
python T05F_AdmonWangJianxin_9069884.py
```

### Example Usage
The `Analytic` class is designed for easy integration. You can easily query data after loading it:

```python
from T05F_AdmonWangJianxin_9069884 import Analytic

# Load the file
analytics = Analytic('GamesSales.csv')

# Query games released between 2010 and 2012 on PS4 or Xbox
results = analytics.match(platform=["PS4", "Xbox"], year_of_release=[2010, 2012])
print(results)
```

## Key Takeaways
Throughout this project, I deepened my understanding of several core engineering concepts:
- **Defensive Programming**: I implemented robust error handling to ensure that "bad" data doesn't compromise the entire application.
- **Object-Oriented Design**: I utilized custom exception classes and private methods to make the code cleaner, modular, and easier to debug.
- **Clean File I/O**: Creating an `errors.txt` audit trail provided me with great practice in managing file streams and logging diagnostic information effectively.
- **Data Structuring**: Transforming flat CSV records into structured dictionaries allowed me to build a flexible query interface that feels intuitive to use.
