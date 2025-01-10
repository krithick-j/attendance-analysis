Here's a README file tailored for your project:

---

# Attendance Analysis

This repository contains a Python-based attendance analysis tool that processes attendance data from a CSV file, cleans it, and outputs the cleaned data to another CSV file. The project also integrates visual analysis using **Tableau Public** to create charts for better understanding and visualization of the attendance data.

## Project Structure

```
krithick-j-attendance-analysis/
├── README.md            # Project overview and documentation
├── cleaned_data.csv     # Cleaned attendance data (output)
├── data.csv             # Raw attendance data (input)
├── main.py              # Python script that performs the cleaning and analysis
└── charts/              # Folder containing Tableau Public charts
```

### Files

- **`README.md`**: This file, which provides an overview of the project and usage instructions.
- **`cleaned_data.csv`**: The output CSV file after cleaning and processing the attendance data.
- **`data.csv`**: The raw input CSV file that contains the initial attendance data.
- **`main.py`**: The Python script that cleans and processes the data. It includes functions to clean course names, topics, durations, and other columns, then generates the cleaned data as `cleaned_data.csv`.
- **`charts/`**: Contains any Tableau charts or exported visualizations, created using **Tableau Public**, to visualize the cleaned data.

## Features

1. **Data Cleaning**: The Python script cleans various columns in the raw data:
    - **Course Name**: Extracts Course ID and Student Name.
    - **Session Status**: Fills missing values and replaces empty strings.
    - **Course Subject**: Identifies level, curriculum, subject, and manager using regular expressions.
    - **Topics Covered**: Standardizes topics by removing unwanted characters and extra spaces.
    - **Duration**: Converts session durations to minutes, handling various formats.

2. **Data Filtering**: The script filters out rows with certain conditions, like missing or invalid course IDs.

3. **Date Formatting**: The session date is converted into a standard format (`YYYY-MM-DD`).

4. **Sorting**: The data is sorted by the leading number in the course subject.

5. **Export Cleaned Data**: The final cleaned data is saved as `cleaned_data.csv`.

6. **Visual Analysis**: The cleaned data is used to generate charts on **Tableau Public** for visual analysis. The charts help in understanding attendance patterns, subject-wise participation, and other trends.

## Requirements

Before running the Python script, ensure you have the following dependencies installed:

- Python 3.x
- pandas
- re (for regular expressions)

You can install the required dependencies by running:

```bash
pip install pandas
```

## Usage

1. **Prepare the Data**:
   - Ensure your raw attendance data is in a CSV file, named `data.csv`. This file should have columns like `Course Name`, `Session Status`, `Course Subject`, `Topics Covered`, `Duration`, etc.

2. **Run the Python Script**:
   - Run the Python script `main.py` to clean the raw data and generate the cleaned output.

   ```bash
   python main.py
   ```

3. **View the Cleaned Data**:
   - After the script completes, the cleaned data will be saved to `cleaned_data.csv`.

4. **Visualize with Tableau**:
   - Import `cleaned_data.csv` into **Tableau Public** for visual analysis.
   - Use Tableau’s drag-and-drop interface to create charts such as:
     - Attendance trends by date
     - Course participation analysis
     - Duration of sessions
     - Other relevant visualizations

5. **Charts Folder**:
   - Check the `charts/` directory for any Tableau workbook files or images of your charts.

## Example Output

The cleaned data file `cleaned_data.csv` will contain columns such as:

- `Course ID`
- `Student Name`
- `Level`
- `Curriculum`
- `Subject`
- `Manager`
- `Cleaned Topics Covered`
- `Cleaned Duration`
- `Participants`
- `Educator`
- `Learner Feedback`
- `Comments`
- `Session Status`
- `Session Date`

## Contributing

Feel free to fork this repository, create issues, and submit pull requests if you have suggestions or improvements.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

This README provides a comprehensive guide to understanding your project and how to use it effectively. Let me know if you need any further modifications!
