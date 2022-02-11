# Change the CSVs to HTML

import pandas as pd
df = "Resources/cities.csv"

# Convert to HTML
df.to_html('data.html', index=False)

data= df.to_html()

#Export df to the Resources folder
print(data)
