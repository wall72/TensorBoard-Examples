# TensorBoard-Examples
TensorBoard examples updated for **TensorFlow 2.20 (latest stable)**.

## Environment
- Python 3.10+
- TensorFlow 2.20.x (latest stable)
- Dataset: MNIST (`tf.keras.datasets.mnist`)

## Install
```bash
python -m venv .venv
```

Windows (PowerShell):
```bash
.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install required packages:
```bash
python -m pip install -U pip
python -m pip install "setuptools<70.0.0"
pip install "tensorflow==2.20.*" jupyter
```

## Run
```bash
jupyter notebook
```

각 노트북을 실행한 뒤, 아래처럼 TensorBoard를 실행하세요.

```bash
tensorboard --logdir logs/mnist
```

## Examples
1. Softmax (`01-softmax.ipynb`)
2. NN (`02-nn.ipynb`)
3. NN with Xavier/Glorot initializer (`03-nn-xavier.ipynb`)
4. NN with Xavier/Glorot initializer + Dropout (`04-nn-xavier-dropout.ipynb`)
5. CNN (`05-cnn.ipynb`)


## Notebook execution results 보기
아래 명령으로 노트북을 실제 실행하고 HTML 결과물을 만들 수 있습니다.

```bash
python scripts/execute_notebooks.py
```

생성된 결과 파일은 `results/*.html`에서 확인할 수 있습니다.
