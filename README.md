# This app is for Fine tuning the GPT model

* ignore fixHowTo.py i was testing something with fine tuning. It is not used for fine tuning

* By now i hope you went through ga-backend flask and have your account and api Key set up you will need it.

* First we create a csv file with two columns prompt and completion

* This will tell cahtGPT If you get this kind of prompt then return me the corresponding completion.
* Chat GPT will then try to figure out the relation between them.

* In completion i gave a JSON. Now chat GPT will only Return a JSON if make-dish-> <dishName> -> is entered and it will figure out other thing during fine tuning like what the json should look like and its data

* OK so create CSV using pandas.

*  Then convert the csv to a chatGPT understandable file using `openai tools fine_tunes.prepare_data --file openai_train_dataV2.csv `
* Then review new file
* Then upload it for fine tune `openai api fine_tunes.create --training_file openai_train_dataV2_prepared.jsonl --model davinci --suffix "<NAME of your fine tune>"`

* you can then go to  https://platform.openai.com/playground to play around with your model.

* Python commands to generate virtual env
```
python3 -m venv venv --> creat venv
source venv/bin/activate ---> activate it
deactivate   ---> to deactivate venv
```

* OUR DATA GENERATION PROMPT
```

I want to make a dish, Name of the Dish : "Butter Chicken"
Give me response back ONLY in the below JSON format, fill up everything that is enclosed by <..> (angle brackets):
{
    "dishName": "<NAME OF THE DISH>",
    "howTo": "<HOW TO MAKE THE DISH in HTML/TEXT FORMAT YOU CAN SKIP NEW LINE CHARACTER>",
    "ingredients": [
        "<INGREDITENT1 NAME ONLY>",
        "<INGREDITENT2 NAME ONLY>",
        "<INGREDITENT3 NAME ONLY>".... and so on
    ],

    "requiredQuantity": "<INGREDIENT ALONG WITH THEIR QUANTITY IN HTML TABLE AS TEXT YOU CAN SKIP NEW LINE CHARACTER>"
} 
```

* Fine tuning openai cli commands
```
<!-- see models you have -->
openai api fine_tunes.list                   

<!-- create data file -->
openai tools fine_tunes.prepare_data --file openai_train_dataV2.csv 

<!-- finetune run -->
openai api fine_tunes.create --training_file openai_train_dataV2_prepared.jsonl --model davinci --suffix "GrocerryBuddyV2-1"

<!-- follow log -->
openai api fine_tunes.follow -i ft-ge1DhQaGlDXmZ7kWF5HGDRFb

```

* Refer fine tune api on offcial openai website to monitor fien tuning process: https://platform.openai.com/docs/api-reference/fine-tunes







