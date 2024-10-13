# 📊 LendingClub Loan Analysis with Python

### 📄 Project Overview:
As a data analyst for **LendingClub**, the goal of this project was to build a simple model to predict whether a borrower would pay back their loan in full. The analysis is based on various borrower details such as loan purpose, FICO score, debt-to-income ratio, interest rate, and more. Additionally, I developed visualizations to help understand loan trends, borrower profiles, and the relationship between different loan variables.

### 📂 Data:
The datasets used in this project include:
- **loandataset.xlsx**: Contains detailed information about loans and borrowers.
- **customer_data.csv**: Provides customer-level data including credit scores and debt ratios.

### 🛠 Tools & Libraries:
- **Python**: The core language used for analysis and modeling.
- **Pandas**: For data cleaning and manipulation.
- **NumPy**: For efficient numerical operations.
- **Matplotlib** and **Seaborn**: For visualizing data trends and relationships.
- **Scikit-learn**: Used for creating predictive models.

### 🔍 Key Insights:
1. **Loan Purpose Distribution**:
   - The most common purpose for loans is **debt consolidation**, followed by **credit card** and **home improvement**.
   - Smaller purposes, such as **educational** loans, have fewer occurrences in the dataset.

2. **FICO Score Distribution**:
   - The FICO scores of borrowers range from 625 to 825, with a peak around 700, indicating most borrowers have a **good** credit score.

3. **Interest Rate vs. Risk**:
   - Borrowers classified as **high risk** tend to receive higher interest rates, as depicted in the box plot.

4. **Debt-to-Income Ratio vs. FICO Score**:
   - The scatter plot highlights a broad range of debt-to-income (DTI) ratios across various FICO scores, with no clear linear correlation.

5. **Interest Rate vs. Loan Risk**:
   - The box plot clearly shows how **low-risk** borrowers have a median interest rate much lower than **high-risk** borrowers, aligning with typical loan underwriting principles.

### 📊 Visualizations:
1. **Loan Purpose Distribution**: Bar chart showing the number of loans for each purpose category.
![fig 4](https://github.com/user-attachments/assets/5e301586-2894-48a7-b7ff-b2a0f1fd48e0)

2. **Debt-to-Income Ratio vs. FICO Score**: Scatter plot showing the relationship between debt-to-income ratios and credit scores.
![fig 3](https://github.com/user-attachments/assets/5741127b-d396-4cdf-8dae-61de92cc8659)

3. **FICO Score Distribution**: Histogram showing the distribution of FICO scores among borrowers.
![fig 2](https://github.com/user-attachments/assets/e772ba51-f919-49b9-a4e7-1fea6db84592)

4. **Risk vs. Interest Rate**: Box plot showing how interest rates vary between low-risk and high-risk borrowers.
![fig 5](https://github.com/user-attachments/assets/ab666cf4-43c5-4546-9b8c-7cc553dbc450)

