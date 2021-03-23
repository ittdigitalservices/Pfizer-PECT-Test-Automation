rem pytest --reruns=0 --alluredir=./result
rem pytest -n0 --alluredir=./result
rem --screenshot=on --screenshot_path=on
rem --driver Firefox --driver-path /webdrivers/geckodriver.exe
rem pytest -n 0 --screenshot=on --screenshot_path=on --alluredir=./result
cd ..
pytest --reruns 0 -s -n 0 --screenshot=on --screenshot_path=./result/screenshot/ --alluredir=./result

