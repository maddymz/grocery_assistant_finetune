import openai
import pandas as pd
import csv
import json
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

recepie_list = ["Pasta","Omelet","Scrambled Eggs","Guacamole","Grilled Chicken Avocado Salad",
                "Pesto Sauce","Chimichurri","Pico de Gallo","Pickled Onions","Homemade Ranch Dressing"
                ,"Chicken Adobo","Spanish Garlic Shrimp","Avocado Berry Smoothie","Butter Chicken","Affogato","Roti","Coca-Cola Cake","Grilled Cheese Sandwhich",
                "Tandoori Chicken","Vegetable Biryani","Chicken Tikka Masala","Chicken Madras","Masala Chai"]
# recepie_list = ["Pasta"]
user_preference = ["Vegeterian", "Non vegeterian"]


f_prompt = "I want to make a dish, Name of the Dish : \"{dish_name_var}\""
f_prompt1 = "I want to make a {user_preference} dish"


f_prompt_text = ''', Give me response back ONLY in the below JSON format, fill up everything that is enclosed by <..> (angle brackets):
{
    "dishName": "<NAME OF THE DISH>",
    "howTo": "<HOW TO MAKE THE DISH IN HTML/TEXT FORMAT YOU CAN SKIP NEW LINE CHARACTER>",
    "ingredients": [
        "<INGREDITENT1 NAME ONLY>",
        "<INGREDITENT2 NAME ONLY>",
        "<INGREDITENT3 NAME ONLY>".... and so on
    ],

    "requiredQuantity": "<INGREDIENT ALONG WITH THEIR QUANTITY IN HTML TABLE AS TEXT YOU CAN SKIP NEW LINE CHARACTER>"
}'''


f_sub_prompt = "MAKE-DISH->{dish_name_var}"
f_sub_prompt1 = "MAKE-DISH->{user_preference}"


df = pd.DataFrame()
df_training = pd.DataFrame()

def gpt_3_turbo(prompt):
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            # prompt=prompt,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=2400,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    response_txt = response['choices'][0]['message']['content']
    return response,response_txt

def gpt_davinci(prompt):
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.3,
            max_tokens=2400,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    response_txt = response['choices'][0]['text']
    return response,response_txt

for recepie in recepie_list:
    for i in range(3):  # 3 times each
        prompt = f_prompt.format(dish_name_var=recepie) + f_prompt_text
        sub_prompt = f_sub_prompt.format(dish_name_var=recepie)
        print(sub_prompt)
        # response = gpt_3_turbo(prompt)
        (response,response_txt) = gpt_davinci(prompt)
        finish_reason = response['choices'][0]['finish_reason']
        
        response_txt_dump = response_txt
        # print(response_txt_dump)
        # print(prompt)
        new_row = {
            'dish_name': recepie,
            'prompt': prompt,
            'sub_prompt': sub_prompt,
            'response_txt': response_txt_dump,
            'finish_reason': finish_reason}
        train_row = {
            'prompt': sub_prompt,
            'completion': response_txt_dump +"##EOF##",
        }
        new_row = pd.DataFrame([new_row])
        train_row = pd.DataFrame([train_row])
        df_training = pd.concat(
            [df_training, train_row], axis=0, ignore_index=True)
        df = pd.concat([df, new_row], axis=0, ignore_index=True)

for pref in user_preference:
    for i in range(3):
        prompt1 = f_prompt1.format(user_preference=pref) + f_prompt_text
        sub_prompt1 = f_sub_prompt1.format(user_preference=pref)
        print(sub_prompt1)
        # response = gpt_3_turbo(prompt)
        (response,response_txt) = gpt_davinci(prompt1)
        finish_reason = response['choices'][0]['finish_reason']
        
        response_txt_dump = response_txt
        # print(response_txt_dump)
        # print(prompt)
        new_row = {
            'dish_name': recepie,
            'prompt': prompt1,
            'sub_prompt': sub_prompt1,
            'response_txt': response_txt_dump+"##EOF##",
            'finish_reason': finish_reason
            }
        train_row = {
            'prompt': sub_prompt1,
            'completion': response_txt_dump +"##EOF##",
        }
        new_row = pd.DataFrame([new_row])
        train_row = pd.DataFrame([train_row])
        df_training = pd.concat(
            [df_training, train_row], axis=0, ignore_index=True)
        df = pd.concat([df, new_row], axis=0, ignore_index=True)

df.to_csv("openai_completionV3.csv")
df_training.to_csv("openai_train_dataV3.csv")
