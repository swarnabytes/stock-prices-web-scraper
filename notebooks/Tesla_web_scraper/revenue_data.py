url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

# Parse the html data
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser") 

# Read html data with pandas
read_html_pandas_tesla = pd.read_html(url)[1]

from io import StringIO
read_html_pandas_tesla = pd.read_html(StringIO(str(soup)))

tesla_revenue = read_html_pandas_tesla[1]
tesla_revenue.rename(columns = {"Tesla Quarterly Revenue (Millions of US $)" : "Date", "Tesla Quarterly Revenue (Millions of US $).1" : "Revenue"},inplace=True)

# Remove the comma, dollar sign, NULL or empty strings from the `Revenue` column. 
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(r'[,$]',"",regex=True)

tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

tesla_revenue.head(2)
