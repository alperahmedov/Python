#
#print(stock_data)
import yfinance as f
import easygui

company = f.Ticker("TSLA")

stock_data = company.history(period= "1mo")
easygui.msgbox(f"{company.info}", title = "simple gui")

# print(company.info)
# hist = company.history(period='5d')
