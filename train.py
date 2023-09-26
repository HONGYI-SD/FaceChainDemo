from gradio_client import Client

client = Client("https://modelscope-facechain.hf.space/")

# 上传图片
result = client.predict(
				"./images/facechain-1.png",	# List[str] (List of filepath(s) or URL(s) to files)
				"./images",	# str (path to directory with images and a file associating images with captions called captions.json)
				fn_index=1
)
print('upload file: ',result)

# 选择基模型
result = client.predict(
				"leosamsMoonfilm_filmGrain20",	# str in '基模型选择(Base model list)' Radio component
				fn_index=2
)
print('select base model: ',result)

# 设置人物名称
result = client.predict(
				"./images",	# str (path to directory with images and a file associating images with captions called captions.json)
				"leosamsMoonfilm_filmGrain20",	# str in '基模型选择(Base model list)' Radio component
				"Howdy!",	# str in '人物lora名称(Character lora name)' Textbox component
				fn_index=3
)
print('set lora name: ',result)

print('------------------train over, start create images------------')

