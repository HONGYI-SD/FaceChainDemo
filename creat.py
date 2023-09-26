from gradio_client import Client

client = Client("https://modelscope-facechain.hf.space/")
result = client.predict(
				"preset",	# str (Option from: ['preset'])
				"leosamsMoonfilm_filmGrain20",	# str in '基模型选择(Base model list)' Radio component
				fn_index=7
)
print(result)

result = client.predict(
				"Howdy!",	# str in '请选择一种风格(Select a style from the pics below):' Textbox component
				fn_index=10
)
print(result)

result = client.predict(
				"Howdy!",	# str in '提示语(Prompt)' Textbox component
				"Howdy!",	# str in '负向提示语(Negative Prompt)' Textbox component
				"leosamsMoonfilm_filmGrain20",	# str in '基模型选择(Base model list)' Radio component
				"null",	# str in '人物LoRA列表(Character LoRAs)' Radio component
				5,	# int | float in '生成图片数量(Number of photos)' Number component
				"preset",	# str (Option from: ['preset'])
								#in 'LoRA文件(LoRA file)' Dropdown component
				"Howdy!",	# str in '请选择一种风格(Select a style from the pics below):' Textbox component
				0,	# int | float (numeric value between 0 and 1)
								#in '风格权重(Multiplier style)' Slider component
				0,	# int | float (numeric value between 0 and 1.2)
								#in '形象权重(Multiplier human)' Slider component
				"无姿态控制(No pose control)",	# str in '姿态控制模型(Pose control model)' Radio component
				"https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image)
								#in '姿态图片(Pose image)' Image component
				fn_index=14
)
print(result)