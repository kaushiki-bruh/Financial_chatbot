import pandas as pd
df = pd.read_csv("Cleaned_Financials_Microsoft_Tesla_Apple_2022_2024.csv")

companies = ['Microsoft', 'Tesla', 'Apple']
metrics = {
    "revenue": "Total Revenue",
    "net income": "Net Income",
    "assets": "Total Assets",
    "liabilities": "Total Liabilities",
    "cash flow": "Cash Flow from Operating Activities"
}

def format_millions(value):
    return f"${value:,} million"

def keyword_chatbot(query):
    query = query.lower()
    
    company = next((c for c in companies if c.lower() in query), None)
    if not company:
        return "Please specify a valid company (Microsoft, Tesla, or Apple)."
    
    year = next((int(y) for y in ['2022', '2023', '2024'] if y in query), None)
    if not year:
        return "Please specify a fiscal year (2022, 2023, or 2024)."
    
    for keyword, column in metrics.items():
        if keyword in query:
            try:
                value = df.loc[(df['Company'] == company) & (df['Fiscal Year'] == year), column].values[0]
                return f"{company}'s {column} in {year} was {format_millions(value)}."
            except IndexError:
                return f"Data not available for {company} in {year}."
    
    return "I can answer questions about revenue, net income, assets, liabilities, or cash flow. Please try again."

print("Welcome to the Financial Chatbot! Ask about Microsoft, Tesla, or Apple (type 'exit' to quit).")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = keyword_chatbot(user_input)
    print("Bot:", response)