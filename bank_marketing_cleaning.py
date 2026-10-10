"""DataCamp: Cleaning Bank Marketing Campaign Data.

Place bank_marketing.csv in the notebook's working directory and run this script.
It produces client.csv, campaign.csv, and economics.csv.
"""

import pandas as pd
import numpy as np

# 1. Load the raw dataset
raw = pd.read_csv("bank_marketing.csv")

# 2. Split into three DataFrames with the required columns
client = raw[[
    "client_id", "age", "job", "marital", "education",
    "credit_default", "mortgage"
]].copy()

campaign = raw[[
    "client_id", "number_contacts", "contact_duration",
    "previous_campaign_contacts", "previous_outcome", "campaign_outcome"
]].copy()

economics = raw[[
    "client_id", "cons_price_idx", "euribor_three_months"
]].copy()

# 3. Clean the client data
client["job"] = client["job"].str.replace(".", "_", regex=False)
client["education"] = (
    client["education"]
    .str.replace(".", "_", regex=False)
    .replace("unknown", np.nan)
)
client["credit_default"] = client["credit_default"].eq("yes")
client["mortgage"] = client["mortgage"].eq("yes")

# 4. Clean the campaign data
campaign["previous_outcome"] = campaign["previous_outcome"].eq("success")
campaign["campaign_outcome"] = campaign["campaign_outcome"].eq("yes")

# Build a date using 2022 and the month/day from the raw dataset
raw["year"] = "2022"
contact_date_strings = (
    raw["year"] + "-" + raw["month"] + "-" + raw["day"].astype(str)
)
campaign["last_contact_date"] = pd.to_datetime(
    contact_date_strings, format="%Y-%b-%d"
)

# 5. Enforce the numeric types requested in the project
for col in ["client_id", "age"]:
    client[col] = client[col].astype(int)

for col in [
    "client_id", "number_contacts", "contact_duration",
    "previous_campaign_contacts"
]:
    campaign[col] = campaign[col].astype(int)

economics["client_id"] = economics["client_id"].astype(int)
for col in ["cons_price_idx", "euribor_three_months"]:
    economics[col] = economics[col].astype(float)

# 6. Validate the final structure before saving
assert len(client) == len(campaign) == len(economics)
assert client.shape[1] == 7
assert campaign.shape[1] == 7
assert economics.shape[1] == 3
assert pd.api.types.is_datetime64_any_dtype(campaign["last_contact_date"])
assert client["credit_default"].dtype == bool
assert client["mortgage"].dtype == bool
assert campaign["previous_outcome"].dtype == bool
assert campaign["campaign_outcome"].dtype == bool

# 7. Export as CSV without an extra index column
client.to_csv("client.csv", index=False)
campaign.to_csv("campaign.csv", index=False)
economics.to_csv("economics.csv", index=False)

print("Success! Created client.csv, campaign.csv, and economics.csv")
print("client:", client.shape)
print("campaign:", campaign.shape)
print("economics:", economics.shape)
