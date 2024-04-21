from gradio_client import Client

client = Client("http://localhost:7865/", serialize=False)
# You have to use serialize = False otherwise you get other (for me unsolvable problems)

tmp_bild = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
# Some input Parameter requesting a picture, otherwise you get an error, therefore here a standard picture for those inputs

x_model = "juggernautXL_v9Rundiffusionphoto2.safetensors"
# My default

seed = "12345"
seed_b = True
#Didn't checked the function with False

positive = "a cat" #positive prompt
negative = "watermark:1.1, deformed hand"

#client.view_api()
#uncomment to get an overview from all parameters

def write_params():
	result = client.predict(
		False, positive, negative, [], "Speed", "1024×1024",
		1, # Anzhal Bilder
		"png",
		seed,	# str in 'Seed' Textbox component
		True, 2,
		5,  #(numeric value between 1.0 and 30.0)in 'Guidance Scale' Slider component
		x_model, # str 'Base Model (SDXL only)' Dropdown component
		"None", 0.1, 
		False, "None", 0 ,#Lora1
		False, "None", 0 ,#Lora2
		False, "None", 0 ,#Lora3
		False, "None", 0 ,#Lora4
		False, "None", 0 ,#Lora5
		False, "", "Disabled", tmp_bild, ["Left"], tmp_bild, "", tmp_bild, 
		False, # bool in 'Disable Preview' Checkbox component
		False, # bool in 'Disable Intermediate Results' Checkbox component
		seed_b, # bool in 'Disable seed increment' Checkbox component
		1.5, 0.8, 0.3, 7,
		"euler_ancestral", 
		"karras", # str (Option from: ['normal', 'karras', 'exponential', 'sgm_uniform', 'simple', 'ddim_uniform', 'lcm', 'turbo'])
		-1,-1,-1,-1,-1,-1,
		False, False, False, False, 1, 1,
		"joint", # str (Option from: ['joint', 'separate', 'vae'])
		0.25, False, 0, 0, 0, 0, False, False, "None", 0, 0, False, False, 0,
		False, # bool in 'Save Metadata to Images' Checkbox component
		"fooocus", # str in 'Metadata Scheme' Radio component
		tmp_bild, 0, 0,"ImagePrompt",
		tmp_bild, 0, 0,"ImagePrompt",
		tmp_bild, 0, 0,"ImagePrompt",
		tmp_bild, 0, 0,"ImagePrompt",
		fn_index=40
	)
	print(result)

def create_pic():
	result2 = client.predict(fn_index=41)
	print(result2)

#With Entrypoint 26 I asked for all known models
result = client.predict(fn_index=26) 
mydata = result[0]
for model in mydata['choices']:
	if not model.startswith("SD"): #Special for me, I have all SD models which I use for redefine in a Subfolder SD, those are ignored
		print (model) #Print Model name
		x_model = model # Replace default with the currenty model
		write_params() # Set parameter
		create_pic() # Call entrypoint 41 for creating the pic
