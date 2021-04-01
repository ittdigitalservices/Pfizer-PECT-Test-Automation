rem py.test --generate-missing --feature features tests/functional
rem pytest-bdd generate ./tests/features/PECT_TC001.feature > ./tests/steps/PECT_001.txt
rem pytest-bdd generate ./tests/features/PECT_TC002.feature > ./tests/steps/PECT_002.txt
rem pytest-bdd generate ./tests/features/PECT_TC003.feature > ./tests/steps/PECT_003.txt
cd ..

pytest-bdd generate ./tests/features/PECT_TC000_Generate.feature > ./tests/steps/PECT_TC000_Generated.py

