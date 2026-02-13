# TensorBoard-Examples
TensorBoard examples updated for **TensorFlow 2.20 (latest stable)**.

## Environment
- Python 3.10+
- TensorFlow 2.20.x (latest stable)
- Dataset: MNIST (`tf.keras.datasets.mnist`)

## Run
```bash
pip install "tensorflow==2.20.*"
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

## 설치 에러 해결 (tensorflow==2.20.* not found)
`ERROR: Could not find a version that satisfies the requirement tensorflow==2.20.*` 에러는 보통 아래 케이스입니다.

- 사내/미러 인덱스에 2.20 패키지가 아직 동기화되지 않음
- Python 버전과 TensorFlow wheel 호환성 문제
- 네트워크/프록시 제한으로 PyPI 접근 실패

권장 순서:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install "tensorflow==2.20.*"
```

위 명령이 계속 실패하면 대안:

```bash
# 1) 공식 PyPI 직접 지정
pip install -i https://pypi.org/simple "tensorflow==2.20.*"

# 2) 인덱스에서 제공하는 최신 안정화 버전 사용
pip install tensorflow
```
