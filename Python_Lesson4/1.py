import pandas as pd
train_df= pd.read_csv('./train.csv')
test_df= pd.read_csv('./test.csv')

print(train_df['Survived'].value_counts(dropna='False'))


print(train_df.isnull().sum())

train_df[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)

print(train_df)

