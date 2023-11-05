# pythonの仮想環境のリセット、キャッシュの削除を行うスクリプト

deactivate

cd ~/git/sample/playground-mysql &&
rm -rf .venv &&
rm -rf .pytest_cache &&
rm -rf __pycache__ &&
rm -rf .mypy_cache &&
rm poetry.lock

echo "finish reset playground-mysql"

cd ~/git/sample/playground-mysql/api &&
rm -rf .venv &&
rm -rf .pytest_cache &&
rm -rf __pycache__ &&
rm -rf .mypy_cache

echo "finish reset playground-mysql/api"

cd ~/git/sample/playground-mysql/db &&
rm -rf .venv &&
rm -rf .pytest_cache &&
rm -rf __pycache__ &&
rm -rf .mypy_cache

echo "finish reset playground-mysql/db"

cd ~/git/sample/playground-mysql &&
asdf reshim

echo "finish asdf reshim"

cd ~/git/sample/playground-mysql/api &&
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    poetry install &&
    deactivate

echo "finish install playground-mysql/api"

cd ~/git/sample/playground-mysql/db &&
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    poetry install &&
    deactivate

echo "finish install playground-mysql/api"
