import pandas as pd
import re

input_file = 'data.csv'  # Change this to your input file path
output_file_session_status = 'cleaned_data.csv'  # Change this to your desired output file path

# Function to clean Course Name
def clean_course_name(course_name):
    course_name = course_name.strip()
    course_name = course_name.replace(' - ', ' ')
    parts = [part.strip() for part in course_name.split()]

    if len(parts) > 0 and parts[0].startswith('MM'):
        course_id = parts[0]
    else:
        course_id = None

    student_name = ' '.join(parts[1:]) if len(parts) > 1 else 'No Name'
    return pd.Series([course_id, student_name])

def parse_course_subject(row):
    level = 'Other'
    curriculum = 'Other'
    subject = 'Other'
    manager = 'Other'

    # Extract course level
    level_match = re.search(r'(\b\d+\b|Year \d+|9th Grade)', row, re.IGNORECASE)
    if level_match:
        level = level_match.group(0)

    # Extract curriculum type
    curriculum_match = re.search(r'(CBSE|GCSE|IGCSE|State|British Curriculm|US State|Other)', row, re.IGNORECASE)
    if curriculum_match:
        curriculum = curriculum_match.group(0)

    # Extract subject
    subject_match = re.search(r'(Maths|Science|English|Chemistry|Physics|Maths-Science-English|Maths & English|Other)', row, re.IGNORECASE)
    if subject_match:
        subject = subject_match.group(0)

    # Extract manager
    manager_match = re.search(r'(Manager - [A-Za-z\s]+|Charmi Monani|Richa|Sakshi|Anchal Lodha|Astha|Lavisha)', row, re.IGNORECASE)
    if manager_match:
        manager = re.sub(r'Manager - ', '', manager_match.group(0))

    return pd.Series([level, curriculum, subject, manager])

# Function to clean Topics Covered
def clean_topic(topic):
    if isinstance(topic, str):
        topic = re.sub(r'[^a-zA-Z0-9\s,.-]', '', topic)  # Keep alphanumeric and specific punctuation
        topic = re.sub(r'\s+', ' ', topic)  # Replace multiple spaces with a single space
        topic = topic.strip()  # Remove leading and trailing spaces
        return topic.lower()  # Standardize to lowercase
    else:
        return "Unknown"  # Handle non-string values (like NaN or floats)

# Function to clean Duration
def clean_duration(duration):
    if isinstance(duration, str):
        duration = duration.strip().lower()

        if duration == "missed":
            return 0  # You can return another value like "N/A" if needed

        hours = 0
        minutes = 0

        # Check for hours and minutes
        if 'h' in duration:
            hours_match = re.search(r'(\d+)h', duration)
            if hours_match:
                hours = int(hours_match.group(1))

        if 'm' in duration:
            minutes_match = re.search(r'(\d+)m', duration)
            if minutes_match:
                minutes = int(minutes_match.group(1))

        # Convert everything to minutes
        total_minutes = hours * 60 + minutes
        return total_minutes
    else:
        return 0  # If it's NaN or not a string, return 0 or another placeholder

# Step 1: Read the CSV file
df = pd.read_csv(input_file)

# Apply the cleaning function to extract Course ID and Student Name
df[['Course ID', 'Student Name']] = df['Course Name'].apply(clean_course_name)

# Clean the 'Session Status' column
df['Session Status'] = df['Session Status'].fillna('OTHER').replace('', 'OTHER')

# Filter for Course Subject starting with a number
df_filtered = df[df['Course Subject'].str.match(r'^\d')].copy()
df_filtered[['Level', 'Curriculum', 'Subject', 'Manager']] = df_filtered['Course Subject'].apply(parse_course_subject)

# Clean and standardize the 'Topics Covered' column
df_filtered['Cleaned Topics Covered'] = df_filtered['Topics Covered'].apply(clean_topic)

# Clean the 'Duration' column
df_filtered['Cleaned Duration'] = df_filtered['Duration'].apply(clean_duration)

# Filter out rows where Course ID is None and starts with 'MM'
filtered_df = df_filtered[df_filtered['Course ID'].notnull() & df_filtered['Course ID'].str.startswith('MM')]

# Convert Session Date to datetime
df['Session Date'] = pd.to_datetime(df['Session Date'], errors='coerce')

# Check if the conversion was successful
if df['Session Date'].isnull().all():
    print("Error: All values in 'Session Date' could not be converted to datetime.")
else:
    # Format the dates to a specific format, e.g., 'YYYY-MM-DD'
    df['Session Date'] = df['Session Date'].dt.strftime('%Y-%m-%d')

# Extracting the leading number for sorting
df_filtered['Leading Number'] = df_filtered['Course Subject'].str.extract(r'(\d+)').astype(int)

# Sort the DataFrame based on the leading number
sorted_cleaned_df = df_filtered.sort_values(by='Leading Number')

# Combine the cleaned data: include the cleaned course subject, topics covered, participants, educator, and duration
final_cleaned_df = sorted_cleaned_df[['Course ID', 'Student Name', 'Level', 'Curriculum', 'Subject', 'Manager', 'Cleaned Topics Covered', 'Cleaned Duration', 'Participants', 'Educator', 'Learner Feedback', 'Comments']].copy()
final_cleaned_df['Session Status'] = df['Session Status']
final_cleaned_df['Session Date'] = df['Session Date']

# Save the cleaned data to a CSV file
final_cleaned_df.to_csv(output_file_session_status, index=False)
print(f"Cleaned data saved to {output_file_session_status}.")

