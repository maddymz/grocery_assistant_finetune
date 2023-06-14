import pandas as pd
import openai
import subprocess

df = pd.read_csv("openai_completionV3.csv")

prepared_data = df.loc[:,['sub_prompt','response_txt']]
prepared_data.rename(columns={'sub_prompt':'prompt', 'response_txt':'completion'}, inplace=True)
prepared_data.to_csv('prepared_data_v3.csv',index=False)


## prepared_data.csv --> prepared_data_prepared.json
subprocess.run('openai tools fine_tunes.prepare_data --file prepared_data_v3.csv'.split())

## Start fine-tuning
subprocess.run('openai api fine_tunes.create --training_file prepared_data_v3_prepared.jsonl --model davinci --suffix "GroceryAsst_v9"'.split())
