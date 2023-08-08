from django.shortcuts import render

# Create your views here.
import seaborn as sns
import matplotlib.pyplot as plt
import io
import urllib, base64

def visualize_data(request):
    # 데이터를 가져온다고 가정
    data = [1, 2, 3, 4, 5]

    # Seaborn으로 시각화
    sns.set_style("darkgrid")
    plt.figure(figsize=(8, 5))
    sns.lineplot(x=range(len(data)), y=data)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Sample Data Visualization")
    
    # 시각화 결과를 이미지로 변환
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # 이미지를 base64 문자열로 인코딩하여 HTML에 삽입
    graphic = urllib.parse.quote(base64.b64encode(image_png))
    
    context = {'graphic': graphic}
    return render(request, 'plot_seaborn/visualization.html', context)
