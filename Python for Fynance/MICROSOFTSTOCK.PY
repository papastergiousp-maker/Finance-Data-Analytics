import pandas as pd

# Load the dataset from the provided URL
df = pd.read_csv("https://storage.googleapis.com/courses_data/Python%20for%20Finance/MSFT_2000_2017.csv")

# Display the first few rows
print(df.head())
max_close = df['Close'].max()
min_close = df['Close'].min()
closing_range = max_close - min_close
final_result = round(closing_range, 2)
print(f"Maximum Close: {max_close}")
print(f"Minimum Close: {min_close}")
print(f"The range of the closing values is: {final_result}")
# 1. Δημιουργία της στήλης με τη διαφορά (High - Low)
df['Difference'] = df['High'] - df['Low']

# 2. Υπολογισμός της μέσης τιμής (mean) αυτής της διαφοράς
mean_difference = df['Difference'].mean()

# 3. Στρογγυλοποίηση στο δεύτερο δεκαδικό
result = round(mean_difference, 2)

# Εκτύπωση του αποτελέσματος
print(f"The mean value of the difference between High and Low is: {result}")
# 1. Κανονικοποίηση της στήλης 'High'
high_min = df['High'].min()
high_max = df['High'].max()
df['High_norm'] = (df['High'] - high_min) / (high_max - high_min)

# 2. Κανονικοποίηση της στήλης 'Low'
low_min = df['Low'].min()
low_max = df['Low'].max()
df['Low_norm'] = (df['Low'] - low_min) / (low_max - low_min)

# 3. Υπολογισμός των διάμεσων τιμών (median)
median_high = df['High_norm'].median()
median_low = df['Low_norm'].median()

# 4. Στρογγυλοποίηση σε 4 δεκαδικά ψηφία και δημιουργία tuple
result = (round(median_high, 4), round(median_low, 4))

# Εκτύπωση του αποτελέσματος
print(result)
# 1. Υπολογισμός της ποσοστιαίας μεταβολής για τη στήλη 'Adj Close'
# Η μέθοδος pct_change() υπολογίζει τη μεταβολή μεταξύ της τρέχουσας και της προηγούμενης τιμής
pct_changes = df['Adj Close'].pct_change()

# 2. Εύρεση της μέγιστης τιμής από τις μεταβολές
max_pct_change = pct_changes.max()

# 3. Στρογγυλοποίηση του αποτελέσματος σε τέσσερα δεκαδικά ψηφία
result = round(max_pct_change, 4)

# Εκτύπωση του αποτελέσματος
print(f"The maximum percentage change for Adj Close is: {result}")
# 1. Υπολογισμός του Moving Average (SMA) με παράθυρο 5
# Η μέθοδος rolling(window=5) ομαδοποιεί τις τιμές ανά 5 και η .mean() βγάζει τον μέσο όρο
sma_5 = df['Close'].rolling(window=5).mean()

# 2. Εύρεση της μέγιστης τιμής του SMA
max_sma = sma_5.max()

# 3. Στρογγυλοποίηση σε ένα δεκαδικό ψηφίο
result = round(max_sma, 1)

# Εκτύπωση αποτελέσματος
print(f"The maximum 5-day SMA is: {result}")
# 1. Μετατροπή της στήλης Date σε τύπο datetime
df['Date'] = pd.to_datetime(df['Date'])

# 2. Φιλτράρισμα των δεδομένων μόνο για το έτος 2010
# Δημιουργούμε ένα νέο DataFrame που περιέχει μόνο τις εγγραφές του 2010
data_2010 = df[df['Date'].dt.year == 2010]

# 3. Καταμέτρηση των ημερών (γραμμών)
# Η len() θα μας δώσει το πλήθος των εγγραφών
working_days_2010 = int(len(data_2010))

# Εκτύπωση αποτελέσματος
print(working_days_2010)
# 1. Υπολογισμός της συσχέτισης μεταξύ των στηλών 'Close' και 'Volume'
# Χρησιμοποιούμε τη μέθοδο corr() η οποία από προεπιλογή υπολογίζει τον συντελεστή Pearson
correlation = df['Close'].corr(df['Volume'])

# 2. Στρογγυλοποίηση του αποτελέσματος σε πέντε δεκαδικά ψηφία
result = round(correlation, 5)

# Εκτύπωση του αποτελέσματος
print(f"The correlation between Close and Volume is: {result}")
from scipy import stats

# 1. Ορισμός των μεταβλητών
# Ανεξάρτητη μεταβλητή (Independent variable): Close
x = df['Close']
# Εξαρτημένη μεταβλητή (Dependent variable): Volume
y = df['Volume']

# 2. Εφαρμογή του μοντέλου γραμμικής παλινδρόμησης
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# 3. Μετατροπή των αποτελεσμάτων σε ακεραίους (integers)
slope_int = int(slope)
intercept_int = int(intercept)

# Εμφάνιση των αποτελεσμάτων
print(f"Slope: {slope_int}")
print(f"Intercept: {intercept_int}")