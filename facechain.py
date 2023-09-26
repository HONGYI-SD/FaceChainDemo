from gradio_client import Client
import datetime

client = Client("https://modelscope-facechain.hf.space/", serialize=False)

print('start training: ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# 1、选择基模型
result = client.predict(
				"leosamsMoonfilm_filmGrain20",	# str in '基模型选择(Base model list)' Radio component
				fn_index=2
)
print('1、select base model: ',result)

# 2、上传图片
result = client.predict(
				"./images/facechain-1.png",	# List[str] (List of filepath(s) or URL(s) to files)
				"./images",	# str (path to directory with images and a file associating images with captions called captions.json)
				fn_index=1
)
print('upload file: ',result)



# 3、开始训练
job1 = client.submit(
				"./images",	# str (path to directory with images and a file associating images with captions called captions.json)
				"leosamsMoonfilm_filmGrain20",	# str in '基模型选择(Base model list)' Radio component
				"preson1",	# str in '人物lora名称(Character lora name)' Textbox component
				fn_index=3
)
#job1.result(timeout=600)
print('set lora name: ',job1.result(timeout=600))

print('train over, start create images: ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

result = client.predict(
				"leosamsMoonfilm_filmGrain20",	# str in '基模型选择(Base model list)' Radio component
				"preset",	# str (Option from: ['preset'])
				fn_index=12
)
print('选择基模型：', result)


result = client.predict(
				"汉服风(Hanfu)",	# str in '请选择一种风格(Select a style from the pics below):' Textbox component
				fn_index=10
)
print('选择风格：',result)

result = client.predict(
				"raw photo, masterpiece, chinese, wearing beautiful traditional hanfu, upper_body, simple background, high-class pure color background, solo, medium shot, high detail face, looking straight into the camera with shoulders parallel to the frame, slim body, photorealistic, best quality",	# str in '提示语(Prompt)' Textbox component
				"",	# str in '负向提示语(Negative Prompt)' Textbox component
				"leosamsMoonfilm_filmGrain20",	# str in '基模型选择(Base model list)' Radio component
				"preson1",	# str in '人物LoRA列表(Character LoRAs)' Radio component
				1,	# int | float in '生成图片数量(Number of photos)' Number component
				"preset",	# str (Option from: ['preset'])
								#in 'LoRA文件(LoRA file)' Dropdown component
				"汉服风(Hanfu)",	# str in '请选择一种风格(Select a style from the pics below):' Textbox component
				0.35,	# int | float (numeric value between 0 and 1)
								#in '风格权重(Multiplier style)' Slider component
				0.95,	# int | float (numeric value between 0 and 1.2)
								#in '形象权重(Multiplier human)' Slider component
				"无姿态控制(No pose control)",	# str in '姿态控制模型(Pose control model)' Radio component
				'',	# str (filepath or URL to image)
								#in '姿态图片(Pose image)' Image component
				fn_index=14
)

print('set lora name: ',result)
print('create images end: ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
