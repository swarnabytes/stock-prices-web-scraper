url_2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

# Parse the html data
html_data_2 = requests.get(url_2).text
soup = BeautifulSoup(html_data_2, 'html.parser')

# Read html data with pandas
read_html_pandas_gme = pd.read_html(url_2)[1]
from io import StringIO

read_html_pandas_gme = pd.read_html(StringIO(str(soup)))
gme_revenue = read_html_pandas_gme[1]

gme_revenue.rename(columns ={"GameStop Quarterly Revenue (Millions of US $)" : "Date", "GameStop Quarterly Revenue (Millions of US $).1" : "Revenue"}, inplace = True)
gme_revenue.head(5)

# Remove the comma , dollar sign,and NULL or empty strings from the Revenue column.
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(r'[,$]',"",regex=True)

gme_revenue.dropna()
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
gme_revenue.head(5)
