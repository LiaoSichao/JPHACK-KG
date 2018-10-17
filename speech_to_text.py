from watson_developer_cloud import SpeechToTextV1
import json

#IBMCloudのアカウント
user = "e9af561c-e282-47b8-bb1f-8b0c192341e3"
pswd = "PJxoNAHVgpT2"
#音声のデータの定義
audio_file = open("sample.wav", "rb") #どの音声ファイルを開くか
cont_type = "audio/wav" #wavファイルを指定
lang = "ja-JP_BroadbandModel" #日本語のデータである

#watsonとつなげる
stt = SpeechToTextV1(username=user, password=pswd)#APIにつなげる
result_json = stt.recognize(audio=audio_file, content_type=cont_type, model=lang)#音声データを変換する

#形態素解析済みの言葉をプリントする
for i in range(len(result_json.result["results"])):#形態素解析済み言葉の個数の回数分行う
    print(result_json.result["results"][i]["alternatives"][0]["transcript"])

#ファイルに書き込む
result = json.dumps(result_json.result, indent=2) #json形式に変換する
f = open("speech_to_text.json", "w") #（名前，書きこむ）ファイルに書き込む
f.write(result)
f.close()
