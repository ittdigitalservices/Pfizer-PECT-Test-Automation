rem pytest --reruns=0 --alluredir=./result
rem pytest -n0 --alluredir=./result
rem --screenshot=on --screenshot_path=on
rem --driver Firefox --driver-path /webdrivers/geckodriver.exe
rem pytest -n 0 --screenshot=on --screenshot_path=on --alluredir=./result
rem pytest -m slow -s -n 0 --screenshot=on --screenshot_path=./result/screenshot/ --alluredir=./result
rem pytest -ra -q -v -m sequential -s --dist=no --numprocesses=1 -n=0 --screenshot=on --screenshot_path=./result/screenshot/ --alluredir=./result
rem pytest -m sequential -s --screenshot=on --screenshot_path=./result/screenshot/ --alluredir=./result
rem -qq --tb=short
rem pytest -vvv -s -n0 --count=0 -x --screenshot=on --screenshot_path=./result/screenshot/ --alluredir=./result
rem -x for error
rem pytest -vvv -s -n0 --count=0 --screenshot=on --screenshot_path=./result/screenshot/ --alluredir=./result
cd ..
pytest -vvv -s -n0 --screenshot=on --screenshot_path=./result/screenshot/ --alluredir=./result
