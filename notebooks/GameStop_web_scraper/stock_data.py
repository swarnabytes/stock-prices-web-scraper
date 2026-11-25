# create a ticker object. The stock is GameStop and its ticker symbol is `GME`
gamestop = yf.Ticker("GME")

# Extract the stock `history` details for the maximum amount of time 
gme_data = gamestop.history(period ="max")
gme_data

#Reset the index
gme_data.reset_index(inplace= True)
