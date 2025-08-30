import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define options
regions = ['North', 'South', 'East', 'West']
roles = ['Manager', 'Analyst', 'Support Lead']
challenges = ['A', 'B', 'C', 'D', 'E']
tools = ['Excel', 'Power BI', 'Tableau', 'None']
yes_no = ['Yes', 'No']

# Generate 1200 rows
data = []
for i in range(1, 1201):
    respondent_id = i
    region = random.choice(regions)
    role = random.choices(roles, weights=[0.4, 0.4, 0.2])[0]
    challenge_selected = random.choices(challenges, weights=[0.35, 0.3, 0.2, 0.1, 0.05])[0]
    uses_dashboard = random.choices(yes_no, weights=[0.6, 0.4])[0]
    reporting_tool = random.choices(tools, weights=[0.5, 0.25, 0.15, 0.1])[0]
    monthly_reporting_time = int(np.random.normal(loc=10, scale=3))  # Avg 10 hours
    interest_in_solution = random.choices(yes_no, weights=[0.85, 0.15])[0]

    data.append([
        respondent_id, region, role, challenge_selected,
        uses_dashboard, reporting_tool, monthly_reporting_time,
        interest_in_solution
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'respondent_id', 'region', 'role', 'challenge_selected',
    'uses_dashboard', 'reporting_tool', 'monthly_reporting_time',
    'interest_in_solution'
])

# Save to CSV
df.to_csv('amazon_survey_data.csv', index=False)
print("✅ Dataset saved as 'amazon_survey_data.csv'")
