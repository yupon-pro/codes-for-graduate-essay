FROM continuumio/anaconda3

RUN pip install --upgrade pip

WORKDIR /workdir

ENTRYPOINT ["jupyter-lab", "--NotebookApp.ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token='mNFS7wbnEIm/Cd/PTe4h/cgboVXIUBszH5MxU8o7rFg'", "--NotebookApp.allow_origin='*'"]

CMD ["--notebook-dir=/workdir"]
# 上のコマンドが、作業ディレクトリーの名前を定義するものです。
# 例えば、`import os`して、`print(os.getcwd())`すると、/workdirが出てきます。
