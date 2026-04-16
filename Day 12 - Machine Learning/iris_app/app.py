
# let's use the model pickle file
# rb - read binary mode
import pickle

with open("DT_iris_Classifier.pkl", "rb") as file:
    model = pickle.load(file)

def predict_species(sl,sw,pl,pw):

    input_data = [[sl, sw, pl, pw]]

    predictions = model.predict(input_data)

    return predictions[0]

# UI

import gradio as gr 

app = gr.Interface(
    fn = predict_species,
    inputs = [
        gr.Number(label= "Sepal Length", value= 3),

        gr.Dropdown(choices=[2,3,4,4.5], label = "Sepal Width", value= 3),

        gr.Radio(choices=[2,3,4,4.5], label = "Petal Length",value= 3),

        gr.Slider(0, 3, label = "Petal Width",value= 3)
    ],
    outputs= 'text',
    title= "The IRIS species identifier",
    description= "describe everything here about the app",
    article= "*Our website [here](https://gradio.live/)*",
    
    flagging_mode= 'never'

)

app.launch(share= True)



# to deploy write in terminal : gradio deploy
# 