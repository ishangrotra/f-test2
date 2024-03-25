# copied from https://tricks.one/post/get-fooocus-gradio-api-working-for-uov/
from gradio_client import Client

client = Client("http://127.0.0.1:7865/")

# Textbox: string
# Checkbox: bool
# Radio: string
# Dropdown: string
# Slider: float | int
# Checkboxgroup: list[string]
# Image: filepath or URL to image

result = client.predict(
	False,	# 'Generate Image Grid for Each Batch' Checkbox
	"",	# 'Prompt' Textbox
	"",	# 'Negative Prompt' Textbox
        # 'Selected Styles' Checkboxgroup
	["Fooocus V2", "Fooocus Semi Realistic", "Fooocus Masterpiece"],
	"Speed",	# 'Performance' Radio
	"1280×768",	# 'Aspect Ratios' Radio
	1,		# 'Image Number' Slider [1,32]
	"png",	# 'Output Format' Radio
	"0",	# 'Seed' Textbox
        False,	# 'Read wildcards in order' Checkbox
	2,		# 'Image Sharpness' Slider [0.0,30.0]
	7,		#  'Guidance Scale' Slider [1.0,30.0]
	"animaPencilXL_v100.safetensors",	# 'Base Model (SDXL only)' Dropdown
	"None",	# 'Refiner (SDXL or SD 1.5)' Dropdown
	0.5,	# 'Refiner Switch At' Slider [0.1,1.0]
	True,	# 'LoRA 1 Enable' Checkbox
	"None",	# 'LoRA 1' Dropdown
	1,	# 'LoRA 1 Weight' Slider [-2,2]
	True,	# 'LoRA 2 Enable' Checkbox
	"None",	# 'LoRA 2' Dropdown
	1,		# 'LoRA 2 Weight' Slider [-2,2]
	True,	# 'LoRA 3 Enable' Checkbox
	"None",	# 'LoRA 3' Dropdown
	1,		# 'LoRA 3 Weight' Slider [-2,2]
	True,	# 'LoRA 4 Enable' Checkbox
	"None",	# 'LoRA 4' Dropdown
	1,		# 'LoRA 4 Weight' Slider [-2,2]
	True,	# 'LoRA 5 Enable' Checkbox
	"None",	# 'LoRA 5' Dropdown component
	1,		# 'LoRA 5 Weight' Slider [-2,2]
	True,	#'Input Image' Checkbox
	"uov",		# 'current tab' Textbox ["uov", "ip", "inpaint"]
	"Vary (Subtle)",	# 'Upscale or Variation:' Radio
	"20240322214141.jpg",			# 'Upscale or Variation' Image
	["Left"],	# 'Outpaint Direction' Checkboxgroup
	"",		# 'Inpaint or Outpaint' Image
	"",		# 'Inpaint Additional Prompt' Textbox
	"",		# 'Inpaint or Outpaint Mask Upload' Image
	True,	# 'Developer Debug Mode: Disable Preview' Checkbox
	True,	# 'Developer Debug Mode: Disable Intermediate Results' Checkbox
	True,	# 'Developer Debug Mode: Disable seed increment' Checkbox
	1.5,	# 'Developer Debug Mode: Positive ADM Guidance Scaler' Slider [0.1,3.0]
	0.8,	# 'Developer Debug Mode: Negative ADM Guidance Scaler' Slider [0.1,3.0]
	0.3,	# 'Developer Debug Mode: ADM Guidance End At Step' Slider [0.0,1.0]
	7,		# 'Developer Debug Mode: CFG Mimicking from TSNR' Slider [1.0,30.0]
	"dpmpp_2m_sde_gpu",	# 'Developer Debug Mode: Sampler' Dropdown
	"karras",	# 'Developer Debug Mode: Scheduler' Dropdown
	-1,	# 'Developer Debug Mode: Forced Overwrite of Sampling Step' Slider [-1,200]
	-1,	# 'Developer Debug Mode: Forced Overwrite of Refiner Switch Step' Slider [-1,200]
	-1,	# 'Developer Debug Mode: Forced Overwrite of Generating Width' Slider [-1,2048]
	-1,	# 'Developer Debug Mode: Forced Overwrite of Generating Height' Slider [-1,2048]
	-1,	# 'Developer Debug Mode: Forced Overwrite of Denoising Strength of "Vary"' Slider [-1,1.0]
	-1,	# 'Developer Debug Mode: Forced Overwrite of Denoising Strength of "Upscale"' Slider [-1,1.0]
	False,	# 'Developer Debug Mode: Mixing Image Prompt and Vary/Upscale' Checkbox
	False,	# 'Developer Debug Mode: Mixing Image Prompt and Inpaint' Checkbox
	False,	# 'Developer Debug Mode: Debug Preprocessors' Checkbox
	False,	# 'Developer Debug Mode: Skip Preprocessors' Checkbox
	64,		# 'Developer Debug Mode: Canny Low Threshold' Slider [1,255]
	128,	# 'Developer Debug Mode: Canny High Threshold' Slider [1,255]
	"joint",	# 'Developer Debug Mode: Refiner swap method' Dropdown
	0.25,	# 'Developer Debug Mode: Softness of ControlNet' Slider [0.0,1.0]
	False,	# 'Developer Debug Mode: FreeU Enabled' Checkbox
	1.01,	# 'Developer Debug Mode: FreeU B1' Slider [0,2]
	1.02,	# 'Developer Debug Mode: FreeU B2' Slider [0,2]
	0.99,	# 'Developer Debug Mode: FreeU S1' Slider [0,4]
	0.95,	# 'Developer Debug Mode: FreeU S2' Slider [0,4]
	False,	# 'Developer Debug Mode: Debug Inpaint Preprocessing' Checkbox
	False,	# 'Developer Debug Mode: Disable initial latent in inpaint' Checkbox
	"v2.6",	# 'Developer Debug Mode: Inpaint Engine' Dropdown
	1,		# 'Developer Debug Mode: Inpaint Denoising Strength' Slider [0.0,1.0]
	0.618,	# 'Developer Debug Mode: Inpaint Respective Field' Slider [0.0,1.0]
	False,	# 'Developer Debug Mode: Enable Mask Upload' Checkbox
	False,	# 'Developer Debug Mode: Invert Mask' Checkbox
	0,		# 'Developer Debug Mode: Mask Erode or Dilate' Slider [-64,64]
	False,	# 'Developer Debug Mode: Save Metadata to Images' Checkbox
	"fooocus",	# 'Metadata Scheme' Radio
	"",				# 'Image Prompt Image 1' Image component
	0,				# 'Image Prompt Image 1 Stop At' Slider [0.0-1.0]
	0,				# 'Image Prompt Image 1 Weight' Slider [0.0-2.0]
	"ImagePrompt",	# 'Image Prompt Image 1 Type' Radio
	"",				# 'Image Prompt Image 2' Image component
	0,				# 'Image Prompt Image 2 Stop At' Slider [0.0-1.0]
	0,				# 'Image Prompt Image 2 Weight' Slider [0.0-2.0]
	"ImagePrompt",	# 'Image Prompt Image 2 Type' Radio
	"",				# 'Image Prompt Image 3' Image component
	0,				# 'Image Prompt Image 3 Stop At' Slider [0.0-1.0]
	0,				# 'Image Prompt Image 3 Weight' Slider [0.0-2.0]
	"ImagePrompt",	# 'Image Prompt Image 3 Type' Radio
	"",				# 'Image Prompt Image 4' Image component
	0,				# 'Image Prompt Image 4 Stop At' Slider [0.0-1.0]
	0,				# 'Image Prompt Image 4 Weight' Slider [0.0-2.0]
	"ImagePrompt",	# 'Image Prompt Image 4 Type' Radio
	fn_index=40
)
print(result)
result= client.predict(fn_index=41)
