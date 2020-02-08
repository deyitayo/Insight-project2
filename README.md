# Insight-project2

This repo contains python scripts written as part of a consulting project to estimate the length of time it takes dialysis access patients to develop complications that would necessitate another dialysis access procedure. The dataset was obtained from a dialysis access facility with entries depicting variables such as the interval between Dialysis Access interventions (DAI), and procedure information for dialysis access patients. This information include data on the age of the patient, the type and subtypes of access procedures performed, whether or not the patient had complications such as narrowing of the blood vessels (stenosis), and amount of anaesthesia used to name a few.

The analysis entailed data cleaning, requiring removing columns of data with only missing values, duplicated data and those indicating payment codes. I also had to remove special characters such as double quotes from the row entries, and ensure variables are of the correct data type. For example, I had to transform the age variable from character strings to numeric data type.

Subsequently, I performed data exploration, which showed the response variable- interval between dialysis access interventions to be skewed and depicting outlier values. So, I did a natural log transformation to take care of the assymmetry in the response variable. Then I used one-hot encoding to break up the individual classes within each categorical variable into seperate columns, and also used simple imputer to replace missing values in numeric predictor variables with the mean value for each column.

Finally, I used a Random Forest model to predict interval between dialysis access interventions. The value in such prediction is that dialysis access facilities/physicians can schedule detailed clinical examination of the patient to detect complications before they become severe. I then embedded the final random forest model into a Web app I built for dialysis facilities to use in estimating appropriate dates for scheduled clininal checkup.

You can take a look at the web app via: https://next-check.herokuapp.com/

PS: I'm unable to share the dataset for this project as I'm bound by a signed confidentiality agreement protecting the privacy of patient health information.
